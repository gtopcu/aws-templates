import os
import logging
import json
import boto3
from pymediainfo import MediaInfo

# Utilizes MediaInfo as lambda layer
# https://pymediainfo.readthedocs.io/en/stable/pymediainfo.html
# https://aws.amazon.com/blogs/media/running-mediainfo-as-an-aws-lambda-function/
# https://github.com/iandow/mediainfo_aws_lambda

# Guardrails Lambda Required setup - !!! Do not forget to add S3 read access role to the lambda execution policy !!!
# 1. Set lambda environmet variables (TTL is for S3 signed URLs, in seconds): 
#   region -> us-east-2
#   env -> dev/test/prod
#   ttl -> 300 
# 2. Create & attach mediaInfo layer (https://aws.amazon.com/blogs/media/running-mediainfo-as-an-aws-lambda-function/)
# 3. Set Parameter Store Params - i.e.:
#   /{env}/guardrails/max_size

logger = logging.getLogger()
logger.setLevel(logging.INFO)

env = os.getenv("env")
if env is None:
    raise Exception("env environment variable not set")
region = os.getenv("region")
if region is None:
    raise Exception("region environment variable not set")
ttl = os.getenv("ttl")
if ttl is None:
    raise Exception("ttl environment variable not set")

ssm_client = boto3.client('ssm')
s3_client = boto3.client('s3',region_name=region,config=boto3.session.Config(signature_version='s3v4',))

logging.info("SSM Parameters:")

#Get max object size config from SSM
try: 
    maxSize = ssm_client.get_parameter(
            Name=f'/{env}/guardrails/max_size',
            WithDecryption=False
        )["Parameter"]["Value"]
except Exception as e:
    raise Exception("Max size param not set in SSM")
paramMaxSize = int(maxSize)
logging.info("Max object size: " + maxSize)


def lambda_handler(event, context):
    
    #print(event)
    #print(context)
    logging.info("In Lambda")
        
    logging.info("Checking object size")
    _checkObjectSize(event)
    
    logging.info("Creating S3 signed URL")
    s3_signed_url = _get_signed_url(event)
    
    logging.info("Calling MediaInfo")
    media_info = _getMediaInfo(s3_signed_url)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": str(media_info.to_json())
        }),
    }

def _checkObjectSize(event:dict) -> None:
    
    bucket_size = event["Records"][0]["s3"]["object"]["size"]
    if bucket_size is None:
        raise Exception("Bucket size is not present in the event details")

    #Get object size from S3 event 
    s3_obj_size = int(bucket_size)
    logging.info("Object Size: " + str(s3_obj_size))
    
    if s3_obj_size > paramMaxSize:
        raise Exception("Object exceeds max allowed size")


def _get_signed_url(event:dict) -> str:
    
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    if bucket_name is None:
        raise Exception("Bucket name is not present in the event details")
        
    object_name = event["Records"][0]["s3"]["object"]["key"]
    if object_name is None:
        raise Exception("S3 object key is not present in the event details")
    
    expiration=int(ttl)
    logging.info("Bucket name: " + bucket_name + " Object Name: " + object_name + " TTL: " + ttl)
    url = _create_presigned_url(bucket_name, object_name, ttl)
    logging.info(url)
    
    return url
    
def _create_presigned_url(bucket_name, object_name, expiration) -> str:
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        logging.error("Error generating pre-signed S3 URL: " + str(e))
        raise e
    return response
    
def _getMediaInfo(s3_signed_url:str) -> dict:
    try:
        --urlencode
        media_info = MediaInfo.parse(s3_signed_url, mediainfo_options="{"Language": "raw"}" library_file='/opt/libmediainfo.so.0')
        for track in media_info.tracks:
            if track.track_type == 'Video':
                print("track info: " + str(track.bit_rate) + " " + str(track.bit_rate_mode)  + " " + str(track.codec))
        
    except Exception as e:
        logging.error("Error calling MediaInfo: " + str(e))
        raise e
    return media_info