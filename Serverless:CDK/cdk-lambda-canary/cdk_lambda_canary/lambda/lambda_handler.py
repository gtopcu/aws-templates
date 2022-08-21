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

    logger.info("Starting lambda handler, env: " + os.environ("env") + " path: " + os.path())
    try:
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from CDK!')
        }
        logger.info("Lambda handler done")
    except KeyError as e:
        logger.error("Error occured, details: %s", "lambda error", exc_info=1)
        raise e
