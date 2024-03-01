# Code whisperer: Option + C
import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

with open('test.jpg', 'rb') as data:
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)


# with open('FILE_NAME', 'wb') as f:
#     s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)

# def upload_to_S3(bucketName, fileName, filePath):
#     s3 = boto3.client('s3')
#     try:
#         s3.upload_file(filePath, bucketName, fileName)
#     except Exception as e:
#         raise (f"S3 Upload Error: {e}")

# def download_from_S3(bucketName, fileName, filePath) -> None:
#     s3 = boto3.client('s3')
#     try:
#         s3.download_file(bucketName, fileName, filePath)
#     except Exception as e:
#         raise (f"S3 Download Error: {e}")
