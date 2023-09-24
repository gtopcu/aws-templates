# Code whisperer: Option + C

import boto3

def upload_to_S3(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# upload file to s3 bucket
def uploadToS3(bucketName, fileName, filePath):
    s3 = boto3.client('s3')
    s3.upload_file(filePath, bucketName, fileName)

# write to dynamodb
def writeToDynamo(tableName, item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    table.put_item(Item=item)

# read from dynamodb
def readFromDynamo(tableName, key):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    response = table.get_item(Key=key)
    return response


