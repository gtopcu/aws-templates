#import logging
import json
import boto3

from aws_lambda_powertools import Tracer, Logger, Metrics

#from botocore.exceptions import ClientError

serviceName = "infraops-cdkPowerToolsTestService"
tracer = Tracer(serviceName)
logger = Logger(serviceName)
metrics = Metrics(serviceName)

@logger.inject_lambda_context
def handler(event, context):

    #logger = logging.getLogger(__name__)
    #logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


   