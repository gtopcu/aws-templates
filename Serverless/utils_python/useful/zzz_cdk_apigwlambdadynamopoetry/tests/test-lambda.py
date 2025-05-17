import json
import pytest
from unittest.mock import MagicMock, patch
import os
import sys
from pathlib import Path

# pytest --version
# python -m pytest -vs
# python -m pytest tests/test-lambda.py -vs

# Add the project root to Python path so we can import the lambda code
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set environment variables for testing
os.environ["TABLE_NAME"] = "users-test"

# Import the Lambda handler after setting environment variables
# sys.path.append("D:/VSCode/aws-templates/Serverless/utils_python/useful/zzz_cdk_apigwlambdadynamopoetry/lambda_fn>")
# from lambda_fn.apigw_lambda import lambda_handler, app, table
from lambda_fn.apigw_lambda import lambda_handler


# Mock APIGatewayProxyEvent
@pytest.fixture
def apigw_event():
    return {
        "version": "2.0",
        "routeKey": "GET /users",
        "rawPath": "/users",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "content-length": "0",
            "host": "api-id.execute-api.region.amazonaws.com",
            "user-agent": "curl/7.64.1",
            "x-amzn-trace-id": "Root=1-trace-id",
            "x-forwarded-for": "127.0.0.1",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "domainName": "api-id.execute-api.region.amazonaws.com",
            "domainPrefix": "api-id",
            "http": {
                "method": "GET",
                "path": "/users",
                "protocol": "HTTP/1.1",
                "sourceIp": "127.0.0.1",
                "userAgent": "curl/7.64.1"
            },
            "requestId": "request-id",
            "routeKey": "GET /users",
            "stage": "$default",
            "time": "10/Feb/2023:13:30:00 +0000",
            "timeEpoch": 1644500000000
        },
        "isBase64Encoded": False
    }

# @pytest.fixture
# def context():
#     return MagicMock()

# @fixture(scope="module")
@pytest.fixture
def context():
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

@pytest.fixture
def mock_table():
    with patch('boto3.resource') as mock_boto3:
        mock_table = MagicMock()
        mock_boto3.return_value.Table.return_value = mock_table
        yield mock_table

def test_list_users(apigw_event, context, mock_table):
    # Setup mock response
    mock_table.scan.return_value = {
        "Items": [
            {"id": "user1", "name": "John Doe", "email": "john@example.com"},
            {"id": "user2", "name": "Jane Smith", "email": "jane@example.com"}
        ]
    }
    
    # Call lambda handler
    response = lambda_handler(apigw_event, context)
    
    # Verify response
    assert response["statusCode"] == 200
    assert response["body"] == [
        {"id": "user1", "name": "John Doe", "email": "john@example.com"},
        {"id": "user2", "name": "Jane Smith", "email": "jane@example.com"}
    ]
    mock_table.scan.assert_called_once()

def test_get_user(apigw_event, context, mock_table):
    # Modify event for GET /users/{id}
    apigw_event["routeKey"] = "GET /users/{id}"
    apigw_event["pathParameters"] = {"id": "user1"}
    apigw_event["rawPath"] = "/users/user1"
    
    # Setup mock response
    mock_table.query.return_value = {
        "Items": [
            {"id": "user1", "name": "John Doe", "email": "john@example.com"}
        ]
    }
    
    # Call lambda handler
    response = lambda_handler(apigw_event, context)
    
    # Verify response
    assert response["statusCode"] == 200
    assert response["body"] == [{"id": "user1", "name": "John Doe", "email": "john@example.com"}]
    mock_table.query.assert_called_once_with(KeyConditionExpression=None)  # The Key condition will be mocked

def test_create_user(apigw_event, context, mock_table):
    # Modify event for POST /users
    apigw_event["routeKey"] = "POST /users"
    apigw_event["rawPath"] = "/users"
    apigw_event["requestContext"]["http"]["method"] = "POST"
    apigw_event["body"] = json.dumps({
        "id": "user3",
        "name": "Bob Johnson",
        "email": "bob@example.com"
    })
    
    # Call lambda handler
    response = lambda_handler(apigw_event, context)
    
    # Verify response
    assert response["statusCode"] == 201
    assert response["body"]["id"] == "user3"
    assert response["body"]["name"] == "Bob Johnson"
    assert response["body"]["email"] == "bob@example.com"
    
    # Verify that put_item was called with the right item
    mock_table.put_item.assert_called_once_with(
        Item={"id": "user3", "name": "Bob Johnson", "email": "bob@example.com"}
    )

def test_update_user(apigw_event, context, mock_table):
    # Modify event for PUT /users/{id}
    apigw_event["routeKey"] = "PUT /users/{id}"
    apigw_event["pathParameters"] = {"id": "user1"}
    apigw_event["rawPath"] = "/users/user1"
    apigw_event["requestContext"]["http"]["method"] = "PUT"
    apigw_event["body"] = json.dumps({
        "name": "John Doe",
        "email": "john.updated@example.com"
    })
    
    # Setup mock get_item response (for checking if user exists)
    mock_table.get_item.return_value = {
        "Item": {"id": "user1", "name": "John Doe", "email": "john@example.com"}
    }
    
    # Call lambda handler
    response = lambda_handler(apigw_event, context)
    
    # Verify response
    assert response["statusCode"] == 200
    
    # Verify that update_item was called with the right parameters
    mock_table.update_item.assert_called_once()

def test_delete_user(apigw_event, context, mock_table):
    # Modify event for DELETE /users/{id}
    apigw_event["routeKey"] = "DELETE /users/{id}"
    apigw_event["pathParameters"] = {"id": "user1"}
    apigw_event["rawPath"] = "/users/user1"
    apigw_event["requestContext"]["http"]["method"] = "DELETE"
    apigw_event["queryStringParameters"] = {"name": "John Doe"}
    
    # Call lambda handler
    response = lambda_handler(apigw_event, context)
    
    # Verify response
    assert response["statusCode"] == 204
    
    # Verify that delete_item was called with the right key
    mock_table.delete_item.assert_called_once_with(
        Key={"id": "user1", "name": "John Doe"}
    )