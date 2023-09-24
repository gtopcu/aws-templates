# Code whisperer: Option + C
import boto3

s3 = boto3.client('s3')

def uploadToS3(local_file, bucket, s3_file):
    
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

"""
# upload file to s3 bucket
def uploadToS3(bucketName, fileName, filePath):
    s3 = boto3.client('s3')
    s3.upload_file(filePath, bucketName, fileName)
"""