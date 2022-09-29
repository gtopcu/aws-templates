import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
s3_client = boto3.client('s3')

try:
    object_key = (
        f"recordings/{video_id}.mp4"
    )
    s3_client.put_object(
        Body=content,
        Bucket=S3_STORAGE_BUCKET_NAME,
        Key=object_key,
        Metadata={
            "filetype": "VIDEO",
            "download_url": recording["download_url"],
        },
    )
except ClientError as exc:
    logger.exception(exc)
    raise exc