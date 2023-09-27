#import logging
import json
import boto3
import os

from aws_lambda_powertools import Tracer, Logger, Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator

#from botocore.exceptions import ClientError

serviceName = "infraops-cdkPowerToolsTestService"
logger = Logger(service=serviceName)
tracer = Tracer(service=serviceName)
metrics = Metrics(service=serviceName, namespace=serviceName)

# ENV VARs
# POWERTOOLS_SERVICE_NAME=infraops-cdkPowerToolsTestService
# POWERTOOLS_LOGGER_SAMPLE_RATE=0.1
# POWERTOOLS_LOGGER_LOG_EVENT=true
# POWERTOOLS_METRICS_NAMESPACE=infraops-cdkPowerToolsTestService
# POWERTOOLS_TRACE_DISABLED=false
# LOG_LEVEL=info

@lambda_handler_decorator(trace_execution=True)
def lambda_middleware(handler, event, context):
    print("lambda_middleware: Running before lambda execution")
    response = handler(event, context)
    print("lambda_middleware: Running after successful lambda execution")
    return response

@lambda_middleware
@logger.inject_lambda_context
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True) #async
def handler(event, context):

    #logger = logging.getLogger(__name__)
    #logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))
    metrics.add_metric(name="MyCustomMetric", unit=MetricUnit.Count, value=1)

    """
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
    """

    try:
        raise ValueError("Got a value error")
    except ValueError as e:
        logger.exception(e)
        raise


   