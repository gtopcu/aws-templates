# Code whisperer: Option + C
import boto3

s3 = boto3.client('s3')

def uploadToS3(local_file, bucket, s3_file) -> None:
    try:
        s3.upload_file(local_file, bucket, s3_file)
    except Exception as e:
        raise Exception(f"S3 Upload Error: {e}")

"""
# upload file to s3 bucket
def uploadToS3(bucketName, fileName, filePath):
    s3 = boto3.client('s3')
    s3.upload_file(filePath, bucketName, fileName)
"""

def downloadFromS3(bucketName, fileName, filePath) -> None:
    try:
        s3.download_file(bucketName, fileName, filePath)
    except Exception as e:
        raise(f"S3 Download Error: {e}")