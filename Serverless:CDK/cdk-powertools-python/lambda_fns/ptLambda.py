#import logging
import json
import boto3

from aws_lambda_powertools import Tracer, Logger, Metrics

#from botocore.exceptions import ClientError

serviceName = "infraops-cdkPowerToolsTestService"
logger = Logger(serviceName)
tracer = Tracer(serviceName)
metrics = Metrics(serviceName)

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@metrics.log_metrics #async
def handler(event, context):

    #logger = logging.getLogger(__name__)
    #logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


   