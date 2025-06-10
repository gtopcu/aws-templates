
import json
import os
from dataclasses import dataclass
from pathlib import Path
from unittest import mock

import boto3
import pytest
import moto
from moto import mock_aws

#-----------------------------------------------------------------------------------------------------------
# https://pypi.org/project/mypy-boto3/

# https://pypi.org/project/mypy-boto3-s3/
# pip install mypy_boto3_s3
# from mypy_boto3_s3 import S3ServiceResource
# from mypy_boto3_s3.service_resource import ServiceResourceBucketsCollection

# pip install mypy_boto3_dynamodb
# from mypy_boto3_dynamodb import DynamoDBClient, DynamoDBServiceResource

# pip install mypy_boto3_cognito_idp
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
#-----------------------------------------------------------------------------------------------------------

# from .lambda import lambda_handler

USER_POOL_ID = "xxxxxxx"
FILE_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def lambda_environment():
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    os.environ["ENVIRONMENT"] = "local-test"
    os.environ["BUCKET_NAME"] = "my-bucket"


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            "arn:aws:lambda:eu-west-1:123456789012:function:test"
        )
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"
    return LambdaContext()


@pytest.fixture
def cognito_context():
    with moto.mock_aws():
        cognito_client: CognitoIdentityProviderClient = boto3.client("cognito-idp")
        user_pool_id = cognito_client.create_user_pool(PoolName="TestUserPool")[
            "UserPool"
        ]["Id"]
        cognito_client.create_group(UserPoolId=user_pool_id, GroupName="admin")
        os.environ[USER_POOL_ID] = user_pool_id

        yield user_pool_id


# @mock_aws
# class TestCompanyService:

#     def test_create_company(self, lambda_environment, lambda_context, cognito_context):
#         event = json.loads(Path(FILE_PATH + "/test/create_company_event.json").read_text())
#         result: dict = lambda_handler(event, lambda_context)

#         assert result["companyName"] == "Test Company"
#         assert result["location"] == "here"
#         assert result["s3BucketName"] == "data-bucket"
