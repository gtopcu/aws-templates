import logging
import boto3
import botocore
from botocore.exceptions import ClientError

# !!!! GIVE S3 ACCESS TO LAMBDA !!!!!

def create_presigned_url(region, bucket_name, object_name, expiration):
    # Choose AWS CLI profile, If not mentioned, it would take default
    # boto3.setup_default_session(profile_name='personal')
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3',region_name=region,config=boto3.session.Config(signature_version='s3v4',))
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        logging.error("Error generating pre-signed S3 URL: " + str(e))
        raise e
    # The response contains the presigned URL
    #print(response)
    return response

create_presigned_url("us-east-2", '00-infraops-testbucket','short.mp4', 600)


