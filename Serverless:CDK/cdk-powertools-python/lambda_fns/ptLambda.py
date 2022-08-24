import logging
import json
import boto3

#from botocore.exceptions import ClientError

def handler(event, context):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


   