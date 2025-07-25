
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

# from mypy_boto3_ses import Client, SESClient
# from mypy_boto3_cognito_idp import CognitoIdentityProviderClient

#-----------------------------------------------------------------------------------------------------------

USER_POOL_ID = "xxxxxxx"
FILE_PATH = os.path.dirname(os.path.realpath(__file__))

# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     """Remove requests.sessions.Session.request for all tests."""
#     monkeypatch.delattr("requests.sessions.Session.request")

# https://docs.pytest.org/en/stable/how-to/monkeypatch.html
@pytest.fixture(scope="class", autouse=False)
def aws_env(monkeypatch):
    """
    setattr("requests.get", lambda x: MockResponse())
    setattr(obj, name, value): Set an attribute on an object for the duration of the test
    delattr(obj, name): Delete an attribute from an object
    setitem(mapping, name, value): Set a key-value pair in a dictionary
    delitem(mapping, name): Remove a key from a dictionary
    setenv(name, value): Set an environment variable
    delenv(name): Remove an environment variable
    syspath_prepend(path): Add a path to sys.path
    chdir(path): Change the current working directory
    context(): Apply patches in a controlled scope
    """
    monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'testing')
    assert monkeypatch.getenv('AWS_DEFAULT_REGION') == 'us-east-1'

# with monkeypatch.context() as mp:
#     mp.setattr(functools, "partial", 3)

@pytest.fixture
def aws_credentials():
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    # os.environ["AWS_ACCESS_KEY_ID"] = "test"
    # os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    # os.environ["AWS_SESSION_TOKEN"] = "test"
    # os.environ["AWS_SECURITY_TOKEN"] = "testing"

@pytest.fixture
def mock_logger():
    with patch("lambda_module.logger") as logger:
        yield logger

# @pytest.fixture(scope="module")
# @pytest.fixture
# def lambda_context():
#     @dataclass
#     class LambdaContext:
#         def __init__(self):
#             self.function_name = "test_function"
#             self.function_version = "1.0"
#             self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
#             self.memory_limit_in_mb = 128
#             self.aws_request_id = "1234567890abcdef"
#             self.log_group_name = "/aws/lambda/test_function"
#             self.log_stream_name = "2023/10/01/[$LATEST]abcdef1234567890abcdef1234567890"
#             self.identity = None
#             self.client_context = None
#     return LambdaContext()

@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test_lambda"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            "arn:aws:lambda:eu-west-1:123456789012:function:test"
        )
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"
    return LambdaContext()

@pytest.fixture
def cognito_context():
    with moto.mock_aws():
        from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
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
        from mypy_boto3_ses import Client
        ses_client:Client = boto3.client("ses")
        ses_client.verify_email_identity(EmailAddress="support@app.com")
        yield

# @patch("lambda_module.handler")
# def test_func(mock_handler): # mock_handler -> MagicMock
#     print("Test func")
#     mock_handler.side_effect = KeyError
#     mock_handler.return_value = "{ "response": "success" }"

# @mock_aws
# class TestCompanyService:
#     def test_create_company(self, aws_credentials, lambda_context, cognito_context):
#         event = json.loads(Path(FILE_PATH + "/test/create_company_event.json").read_text())
#         result: dict = lambda_handler(event, lambda_context)

#         assert result["companyName"] == "Test Company"
#         assert result["location"] == "here"
#         assert result["s3BucketName"] == "data-bucket"

# @mock_aws
# def test_lambda(aws_credentials, mock_logger, lambda_context, lambda_event):

#     with patch(
#         "ddb_company.get_company",
#         return_value="dummy_class",
#     ):
#         # Assert that the response has been generated in result correctly.
#         result = lambda_handler(lambda_event, lambda_context)

#         # Check that the logger.info was called with the expected message
#         mock_logger.info.assert_called_with(
#             "### This is a dummy log for assertion ###"
#         )

#         # Ensure the event is returned correctly
#         assert result == lambda_event


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
    
# # Cognito claims
# @pytest.fixture
# def mock_cognito_identity():
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

# # Cognito user created lambda event
# @pytest.fixture
# def lambda_event():
#     # event = json.loads(Path(FILE_PATH + "/test/test_event.json").read_text())
#     return {
#         "triggerSource": "CustomMessage_AdminCreateUser",
#         "request": {
#             "userAttributes": {
#                 "custom:company_id": "a1b718e5-b0b7-40c9-a9e6-00804d44af25",
#                 "email": "test@test.com",
#             },
#             "codeParameter": "12345",
#             "usernameParameter": "test@test.com",
#         },
#         "response": {},
#     }