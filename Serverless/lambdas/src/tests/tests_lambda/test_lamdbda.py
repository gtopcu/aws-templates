
import pytest
from dataclasses import dataclass
from lambdas import lambda_fn

import os, sys
import json
from http import HTTPStatus

# Add the parent directory to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# sys.path.append(parent_dir)


def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        function_version:str = "$LATEST"
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        memory_limit_in_mb: int = 128
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"
        log_group_name = "/aws/lambda/test"
        log_stream_name = "2024/01/01/[$LATEST]123456789"

        def get_remaining_time_in_millis(self):
            return 30000

    return LambdaContext()

# @pytest.fixture(scope="function")
# def set_env(monkeypatch):
#     print("Setting monkeypatch..")
#     monkeypatch.setenv("DDB_TABLE_NAME", 'table-1')
#     # assert os.getenv("DDB_TABLE_NAME") == 'table-1'
#     # assert os.getenv("AWS_DEFAULT_REGION") == 'us-east-1'
#     return monkeypatch

def test_enviroment():
    assert os.getenv("DDB_TABLE_NAME") == 'table-1'

@pytest.mark.unit
def test_lambda_handler(event_apigw_lambda):

    event = { "body": json.dumps("Hello to Lambda") }
    response = lambda_fn.handler(event, lambda_context())
    assert response['statusCode'] == HTTPStatus.OK

    response = lambda_fn.handler({"zzz":1}, lambda_context())
    assert response['statusCode'] == HTTPStatus.BAD_REQUEST

    event = json.loads(event_apigw_lambda)
    # print(event["body"])
    # body = json.loads(event["body"])
    response = lambda_fn.handler(event, lambda_context())
    assert response['statusCode'] == HTTPStatus.OK
    
    # assert response['statusCode'] == 200
    # assert response['body'] == 'Hello from Lambda!'

    