
import boto3

def upload_to_S3(local_file, bucket, s3_file):
    """
    Uploads a file to an S3 bucket
    """
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
