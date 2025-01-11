import json
import os, sys
from datetime import datetime
import time
import logging

from http import HTTPStatus
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.basicConfig( level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')

# print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
# print(time().strftime("%Y-%m-%d %H:%M:%S"))

# aws lambda invoke \
# --function-name my-function \
# --cli-binary-format raw-in-base64-out \
# --payload '{"name": "Alice", "birthday": "1990-01-01", "email": "alice@gmail.com"}' \
# output.json && cat output.json


# dynamodb = boto3.resource(
#     "dynamodb",
#     endpoint_url="http://localhost:8000",
#     region_name=REGION,
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=ACCESS_KEY_SECRET,
# )

# dynamodb = boto3.resource("dynamodb')
# table = dynamodb.Table(os.environ['DDB_TABLE_NAME'])
ddb_table_name = os.environ["DDB_TABLE_NAME"]


def handler(event: dict, context: dict):
    request_id = context.aws_request_id

    logger.info(f"request_id: {request_id}, context: {context}")

    try:
        if not event:
            raise ValueError("event is empty")

        logger.info(f"request_id: {request_id}, event: {repr(event)}")

        # method = event["httpMethod"]
        # headers = event["headers"]
        # raw_path = event["rawPath"]
        # path = event["path"]
        # path_params = event["pathParameters"]
        # query_params = event["queryStringParameters"]
        # request_context = event["requestContext"]
        # body = event["body"]

        # Input Validation
        body = event.get("body")
        if not body:
            raise ValueError("Request body cannot be empty")
        # size = sys.getsizeof(body)
        # if size > 1:
        #     raise ValueError("Request body size exceeds the limit: %d bytes" % size)
        if not isinstance(body, str):
            raise ValueError("Request body must be valid a JSON string")
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in request body")

        return {
            "statusCode": HTTPStatus.OK,
            # "statusCode": HTTPStatus.CREATED,
            # "statusCode": HTTPStatus.ACCEPTED,
            # "statusCode": HTTPStatus.BAD_REQUEST,
            # "statusCode": HTTPStatus.UNAUTHORIZED,
            # "statusCode": HTTPStatus.FORBIDDEN,
            # "statusCode": HTTPStatus.NOT_FOUND,
            # "statusCode": HTTPStatus.METHOD_NOT_ALLOWED
            # "statusCode": HTTPStatus.CONTENT_TOO_LARGE,
            # "statusCode": HTTPStatus.TOO_MANY_REQUESTS,
            # "statusCode": HTTPStatus.UNPROCESSABLE_ENTITY,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Hello from Lambda!"}),
        }
    except ValueError as e:
        logger.warning(f"Error - request_id: {request_id}\nerror: {str(e)}", exc_info=True)
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": json.dumps({"message": f"error: {str(e)}"}),
        }
    except Exception as e:
        logger.error(f"Internal error - request_id: {request_id}\nerror: {str(e)}", exc_info=True)
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": json.dumps({"message": f"Internal Error - request_id: {request_id}"}),
        }
