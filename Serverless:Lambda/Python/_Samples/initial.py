import os
import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    print("In lambda handler")
    
    logger.info("Env Vars: \r" + json.dumps(dict(**os.environ)))
    logger.info("Event: \r" + json.dumps(event))
    logger.info("Context: \r" + str(context))

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Hello World"
    }

    return resp



