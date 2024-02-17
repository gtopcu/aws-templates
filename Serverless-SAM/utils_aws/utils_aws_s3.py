# Code whisperer: Option + C
import boto3


def upload_to_S3(bucketName, fileName, filePath):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(filePath, bucketName, fileName)
    except Exception as e:
        raise (f"S3 Upload Error: {e}")

def download_from_S3(bucketName, fileName, filePath) -> None:
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucketName, fileName, filePath)
    except Exception as e:
        raise (f"S3 Download Error: {e}")
