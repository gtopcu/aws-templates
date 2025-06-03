import json

from aws_lambda_powertools import logging, Tracer
from aws_lambda_powertools.utilities.data_classes import event_source, SNSEvent

tracer = Tracer()
logger = logging.Logger()


@event_source(data_class=SNSEvent)
@tracer.capture_lambda_handler
def lambda_handler(event: SNSEvent, context):
    for record in event.records:
        message = record.sns.message
        logger.info(f"Received SNS message: {message}")

        result = handle_sns(**json.loads(message))
        logger.info(f"Handled notification, result: {result}")

def handle_sns():
    pass