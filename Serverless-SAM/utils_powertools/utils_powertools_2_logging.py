# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/logger/

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent

import requests

logger = Logger()
#logger = Logger(level="DEBUG INFO WARNING ERROR CRITICAL")
#logger = Logger(serialize_stacktrace=True)


ENDPOINT = "http://httpbin.org/status/500"

@logger.inject_lambda_context(log_event=True, #beware of sensitive data!
                              clear_state=True, #logger is global scope
                              correlation_id_path=correlation_paths.API_GATEWAY_REST)
def lambda_handler(event: dict, context: LambdaContext) -> str:
    

    #request = APIGatewayProxyEvent(event)
    #logger.set_correlation_id(request.request_context.request_id)
    logger.debug(f"Correlation ID => {logger.get_correlation_id()}")
    
    logger.info("Collecting payment", request_id="1123")
    logger.info({"operation": "collect_payment", "charge_id": event["charge_id"]})
    
    order_id = event.get("order_id")
    logger.append_keys(order_id=order_id)

    try:
        resp = requests.get(ENDPOINT)
        resp.raise_for_status()
    except requests.HTTPError as e:
        #logger.exception(e)
        logger.exception("Received a HTTP 5xx error")
        raise RuntimeError("Unable to fullfil request") from e

    return "hello world"


# When unit testing your code that makes use of inject_lambda_context decorator, you need to pass a dummy Lambda Context, 
# or else Logger will fail. This is a Pytest sample that provides the minimum information necessary for Logger to succeed:

# from dataclasses import dataclass
# import fake_lambda_context_for_logger_module  # sample module for completeness
# import pytest
# from dataclasses import dataclass

# @pytest.fixture
# def lambda_context():
#     @dataclass
#     class LambdaContext:
#         function_name: str = "test"
#         memory_limit_in_mb: int = 128
#         invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
#         aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

#     return LambdaContext()


# def test_lambda_handler(lambda_context):
#     test_event = {"test": "event"}
#     fake_lambda_context_for_logger_module.handler(test_event, lambda_context)