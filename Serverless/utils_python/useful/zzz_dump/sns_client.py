
import json
from functools import lru_cache
from pydantic import BaseModel

import boto3
from aws_lambda_powertools import Logger

# pip install mypy_boto3_sns
from mypy_boto3_sns import Client


logger = Logger()


class SnsWrapper:
    """Encapsulates Amazon SNS topic functions."""

    __sns_client: Client

    def __init__(self):
        self.__sns_client = boto3.client("sns")

    def publish(self, target: str, request: BaseModel) -> str:
        """
        Publish request to target arn.
        Request must be a Pydantic model which will be serialized to the message.

        :return str: MessageId for the message
        """
        try:
            response = self.__sns_client.publish(
                TargetArn=target,
                Message=json.dumps({"default": request.model_dump_json()}),
                MessageStructure="json",
            )
        except Exception:
            logger.exception(f"Couldn't publish message to topic arn: {target}")
            raise
        else:
            logger.info(
                f"Published message {response['MessageId']} to topic arn: {target}"
            )
            return response["MessageId"]


@lru_cache(maxsize=1)
def get_sns_wrapper():
    return SnsWrapper()
