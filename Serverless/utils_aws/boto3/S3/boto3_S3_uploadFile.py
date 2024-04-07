import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def upload_file(content, video_id, bucket_name):
    s3_client = boto3.client('s3')
    try:
        object_key = (
            f"recordings/{video_id}.mp4"
        )
        s3_client.put_object(
            Body=content,
            Bucket=bucket_name,
            Key=object_key,
            Metadata={
                "filetype": "VIDEO",
            }
        )
    except ClientError as exc:
        logger.exception(exc)
        raise exc

