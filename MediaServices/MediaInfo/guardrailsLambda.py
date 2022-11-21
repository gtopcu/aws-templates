import json
import boto3
import os
from boto3.dynamodb.conditions import Key
import logging
from decimal import Decimal


ddb = boto3.resource("dynamodb")
ssm_client = boto3.client("ssm")
lambda_client = boto3.client("lambda")

MEDIAINFO_HANDLER_FUNC_ARN = os.environ["MEDIAINFO_HANDLER_FUNC_ARN"]

VIDEO_FILE_TYPE = ssm_client.get_parameter(Name=os.environ["VIDEO_FILE_TYPE"])[
    "Parameter"
]["Value"]

VIDEO_CODEC = ssm_client.get_parameter(Name=os.environ["VIDEO_CODEC"])[
    "Parameter"
]["Value"]

VIDEO_DURATION_MIN = ssm_client.get_parameter(
    Name=os.environ["VIDEO_DURATION_MIN"]
)["Parameter"]["Value"]

VIDEO_DURATION_MAX = ssm_client.get_parameter(
    Name=os.environ["VIDEO_DURATION_MAX"]
)["Parameter"]["Value"]

VIDEO_FPS = ssm_client.get_parameter(Name=os.environ["VIDEO_FPS"])[
    "Parameter"
]["Value"]

VIDEO_BIT_RATE = ssm_client.get_parameter(Name=os.environ["VIDEO_BIT_RATE"])[
    "Parameter"
]["Value"]

VIDEO_WIDTH_MIN = ssm_client.get_parameter(Name=os.environ["VIDEO_WIDTH_MIN"])[
    "Parameter"
]["Value"]

VIDEO_HEIGHT_MIN = ssm_client.get_parameter(
    Name=os.environ["VIDEO_HEIGHT_MIN"]
)["Parameter"]["Value"]

video_metadata_table = ddb.Table(os.environ["VIDEO_METADATA_TABLE"])

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_or_create_video_metadata(bucket_name, object_key):
    video_id = object_key.split("/")[-1].split(".")[0]

    ddb_response = video_metadata_table.query(
        KeyConditionExpression=Key("videoID").eq(video_id)
    )

    if ddb_response["Count"] > 0:
        logger.info(f"Object with id:{video_id} already has metadata.")
        return {
            "statusCode": 200,
            "body": ddb_response["Items"][0],
        }

    try:
        payload = {"bucket_name": bucket_name, "s3_key": object_key}
        response = lambda_client.invoke(
            FunctionName=MEDIAINFO_HANDLER_FUNC_ARN,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload),
        )
        response = json.load(response["Payload"])

        if response["statusCode"] == 200:
            mediainfo_data = (
                [
                    track
                    for track in response["body"]
                    if track["track_type"] == "Video"
                ]
            )[0]

            is_valid_metadata = (
                check_existence_for_type(
                    VIDEO_FILE_TYPE, mediainfo_data["internet_media_type"]
                )
                and check_existence_for_type(
                    VIDEO_CODEC, mediainfo_data["format"]
                )
                and check_min_value(
                    VIDEO_DURATION_MIN, mediainfo_data["duration"] / 1000
                )
                and check_min_value(VIDEO_FPS, mediainfo_data["frame_rate"])
                and check_min_value(
                    VIDEO_BIT_RATE, mediainfo_data["bit_rate"] / 8000
                )
                and check_min_value(VIDEO_HEIGHT_MIN, mediainfo_data["height"])
                and check_min_value(VIDEO_WIDTH_MIN, mediainfo_data["width"])
                and check_max_value(
                    VIDEO_DURATION_MAX, mediainfo_data["duration"] / 1000
                )
            )

            if not is_valid_metadata:
                return {
                    "statusCode": 400,
                    "body": {
                        "message": (
                            "Video requirements are not met for object with"
                            f" id: {object_key}"
                        )
                    },
                }

            # Writing record to db
            return save_metadata_to_db(mediainfo_data, video_id)

        else:
            logger.error(
                f"Error calling mediainfo function for {object_key} from"
                f" {bucket_name}"
            )

    except Exception as e:
        logger.error("Error while calling mediainfo handler. Error:", e)

    return {
        "statusCode": 502,
        "body": {
            "message": "Something went wrong connecting to other services",
        },
    }


def check_min_value(min_value, current_value):
    return float(min_value) <= float(current_value)


def check_max_value(max_value, current_value):
    return float(max_value) >= float(current_value)


def check_existence_for_type(valid_types: str, current_value: str) -> bool:
    return current_value in valid_types.split(",")


def save_metadata_to_db(mediainfo_data, video_id):
    record = {"videoID": video_id}
    record["type"] = mediainfo_data["internet_media_type"]
    record["duration"] = mediainfo_data["duration"] / 1000
    record["metadata"] = mediainfo_data

    record = json.loads(json.dumps(record), parse_float=Decimal)

    video_metadata_table.put_item(Item=record)
    logger.info(f"Created metadata for video with id: {video_id}")

    return {
        "statusCode": 200,
        "body": record,
    }


def handler(event, context):
    logger.info(f"Recieved event: {event}")

    bucket_name = event["bucketName"]
    object_key = event["objectKey"]

    return get_or_create_video_metadata(bucket_name, object_key)
