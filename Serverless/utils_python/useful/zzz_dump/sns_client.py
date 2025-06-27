
import json

import boto3
from aws_lambda_powertools import Logger
from mypy_boto3_sns import Client
from pydantic import BaseModel

logger = Logger()
sns_client:Client = boto3.client("sns")

class SnsWrapper:
    """Encapsulates Amazon SNS topic functions."""

    def __init__(self):
        self.__sns_client = sns_client

    def publish(self, topic_arn: str, request: BaseModel) -> str:
        """
        Publishes the request to the SNS topic with the target arn.
        Request must be a Pydantic model which will be serialized to the message.

        :return str: MessageId for the message
        """
        try:
            response = self.__sns_client.publish(
                TargetArn=topic_arn,
                Message=json.dumps({"default": request.model_dump_json()}),
                MessageStructure="json",
            )
        except Exception:
            logger.exception(f"Couldn't publish message to topic arn: {topic_arn}")
            raise
        else:
            logger.info(
                f"Published message {response['MessageId']} to topic arn: {topic_arn}"
            )
            return response["MessageId"]