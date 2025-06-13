
import json
import os
from dataclasses import dataclass
from pathlib import Path
from unittest import mock
from unittest.mock import Mock, patch

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

# https://pypi.org/project/mypy-boto3-dynamodb/
# pip install mypy_boto3_dynamodb
# from mypy_boto3_dynamodb import DynamoDBClient, DynamoDBServiceResource
# from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter
# from mypy_boto3_dynamodb.paginator import (
#     ListBackupsPaginator,
#     ListTablesPaginator,
#     ListTagsOfResourcePaginator,
#     QueryPaginator,
#     ScanPaginator,
# )
# from boto3.session import Session
# from mypy_boto3_dynamodb import DynamoDBServiceResource
# resource: DynamoDBServiceResource = Session().resource("dynamodb")
# ddb_table = resource.Table("my-table")

# pip install mypy_boto3_cognito_idp
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
#-----------------------------------------------------------------------------------------------------------

# from .lambda import lambda_handler
def lambda_handler(event, context): ...

USER_POOL_ID = "xxxxxxx"
FILE_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    # os.environ["AWS_ACCESS_KEY_ID"] = "test"
    # os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    # os.environ["AWS_SESSION_TOKEN"] = "test"
    # os.environ["AWS_SECURITY_TOKEN"] = "testing"

@pytest.fixture
def mock_logger():
    with patch("lambda_module.logger") as logger:
        yield logger

@pytest.fixture
def lambda_event():
    # event = json.loads(Path(FILE_PATH + "/test/test_event.json").read_text())
    """Generates a mock cognito user created lambda event"""
    return {
        "triggerSource": "CustomMessage_AdminCreateUser",
        "request": {
            "userAttributes": {
                "custom:company_id": "a1b718e5-b0b7-40c9-a9e6-00804d44af25",
                "email": "test@test.com",
            },
            "codeParameter": "12345",
            "usernameParameter": "test@test.com",
        },
        "response": {},
    }

# @pytest.fixture(scope="module")
@pytest.fixture
def lambda_context():
    class LambdaContext:
        def __init__(self):
            self.function_name = "test_function"
            self.function_version = "1.0"
            self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
            self.memory_limit_in_mb = 128
            self.aws_request_id = "1234567890abcdef"
            self.log_group_name = "/aws/lambda/test_function"
            self.log_stream_name = "2023/10/01/[$LATEST]abcdef1234567890abcdef1234567890"
            self.identity = None
            self.client_context = None
    return LambdaContext()

# @pytest.fixture
# def lambda_context():
#     @dataclass
#     class LambdaContext:
#         function_name: str = "test_lambda"
#         memory_limit_in_mb: int = 128
#         invoked_function_arn: str = (
#             "arn:aws:lambda:eu-west-1:123456789012:function:test"
#         )
#         aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"
#     return LambdaContext()

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

@pytest.fixture()
def ses_context():
    with mock_aws():
        ses_client = boto3.client("ses", region_name="eu-west-2")
        ses_client.verify_email_identity(EmailAddress="support@app.com")
        yield


# @mock_aws
# class TestCompanyService:
#     def test_create_company(self, aws_credentials, lambda_context, cognito_context):
#         event = json.loads(Path(FILE_PATH + "/test/create_company_event.json").read_text())
#         result: dict = lambda_handler(event, lambda_context)

#         assert result["companyName"] == "Test Company"
#         assert result["location"] == "here"
#         assert result["s3BucketName"] == "data-bucket"

@mock_aws
def test_lambda(aws_credentials, mock_logger, lambda_context, lambda_event):

    with patch(
        "ddb_company.get_company",
        return_value="dummy_class",
    ):
        # Assert that the response has been generated in result correctly.
        result = lambda_handler(lambda_event, lambda_context)

        # Check that the logger.info was called with the expected message
        mock_logger.info.assert_called_with(
            "### This is a dummy log for assertion ###"
        )

        # Ensure the event is returned correctly
        assert result == lambda_event


# cognito appsync
# @pytest.fixture
# def mock_event():
#     return {
#         "identity": {
#             "claims": {
#                 "custom:company_id": "test-company-id",
#                 "email": "test@example.com",
#                 "given_name": "Test",
#                 "family_name": "User"
#             }
#         }
#     }

# @pytest.fixture
# def mock_context():
#     return Mock()

# @patch('lambda_module.send_email')
# def test_update_status_success(mock_send_email, mock_event, mock_context):
#     mock_send_email.return_value = mock_supplier
#     # Setup
#     mock_supplier = Mock(
#         id="supplier-1",
#         supplier_email="supplier@test.com",
#         supplier_name="Test Supplier",
#         company_id="test-company-id"
#     )
#     assert mock_send_email.called
    