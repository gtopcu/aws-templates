import os
import sys
import logging
import json
import requests
import uuid
import time
import datetime
import random

logger = logging.getLogger()

def lambda_handler(event, context):

    return None
    """
    logger.info("Starting lambda handler")
    #logger.info("env: " + os.getenv("env"))
    #logger.info("path: " + os.path())
    try:
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from CDK!')
        }
        logger.info("Lambda handler done")
    except Exception as e:
        logger.error("Error occured, details: %s", "lambda error", exc_info=1)
        raise e
    """