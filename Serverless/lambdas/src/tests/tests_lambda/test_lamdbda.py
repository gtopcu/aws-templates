
# import pytest
# from dataclasses import dataclass
# from lambdas import lambda_fn

# import os, sys
# import json
# from http import HTTPStatus

# Add the parent directory to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# sys.path.append(parent_dir)


# @pytest.fixture
# def lambda_context():
#     @dataclass
#     class LambdaContext:
#         function_name: str = "test-function"
#         function_version: str = "$LATEST"
#         invoked_function_arn: str = "arn:aws:lambda:us-east-1:123456789012:function:test"
#         memory_limit_in_mb: int = 128
#         aws_request_id: str = "test-request-id-1234"
#         log_group_name: str = "/aws/lambda/test"
#         log_stream_name: str = "2024/01/01/[$LATEST]123456789"

#         def get_remaining_time_in_millis(self):
#             return 30000
    
#     return LambdaContext()

# @pytest.fixture(scope="function")
# def set_env(monkeypatch):
#     print("Setting monkeypatch..")
#     monkeypatch.setenv("DDB_TABLE_NAME", 'table-1')
#     # assert os.getenv("DDB_TABLE_NAME") == 'table-1'
#     # assert os.getenv("AWS_DEFAULT_REGION") == 'us-east-1'
#     return monkeypatch

# def test_enviroment():
#     assert os.getenv("DDB_TABLE_NAME") == 'table-1'

# @pytest.mark.unit
# def test_lambda_handler(event_apigw_lambda):

#     event = { "body": json.dumps("Hello to Lambda") }
#     event = { "body": json.dumps({
#                                   "name": "John Doe",
#                                   "email": "john@example.com"
#                               })}
#     response = lambda_fn.handler(event, lambda_context())
#     assert response['statusCode'] == HTTPStatus.OK

#     response = lambda_fn.handler({"zzz":1}, lambda_context())
#     assert response['statusCode'] == HTTPStatus.BAD_REQUEST

#     event = json.loads(event_apigw_lambda)
#     # print(event["body"])
#     # body = json.loads(event["body"])
#     response = lambda_fn.handler(event, lambda_context())
#     assert response['statusCode'] == HTTPStatus.OK
    
#     # assert response['statusCode'] == 200
#     # assert response["headers"]["Content-Type"] == "application/json"
#     # assert response['body'] == 'Hello from Lambda!'


# ---------------------------------------------------------------------------------------------------------    

import pytest
import json
import os
from http import HTTPStatus
from dataclasses import dataclass
import logging

# Add the correct import path
# import sys
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# sys.path.append(parent_dir)

#from lambda_fn import handler
from lambdas.lambda_fn import handler

# Fixtures
@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test-function"
        function_version: str = "$LATEST"
        invoked_function_arn: str = "arn:aws:lambda:us-east-1:123456789012:function:test"
        memory_limit_in_mb: int = 128
        aws_request_id: str = "test-request-id-1234"
        log_group_name: str = "/aws/lambda/test"
        log_stream_name: str = "2024/01/01/[$LATEST]123456789"

        def get_remaining_time_in_millis(self):
            return 30000
    
    return LambdaContext()

@pytest.fixture
def valid_event():
    return {
        "body": json.dumps({
            "name": "John Doe",
            "email": "john@example.com"
        })
    }

@pytest.fixture(scope="session", autouse=True)
def set_env():
    mp = pytest.MonkeyPatch()
    mp.setenv('DDB_TABLE_NAME', 'test-table')
    yield
    mp.undo()

# Test cases
def test_successful_request(lambda_context, valid_event, caplog):
    """Test successful request processing"""
    caplog.set_level(logging.DEBUG)
    
    response = handler(valid_event, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.OK
    assert response["headers"]["Content-Type"] == "application/json"
    
    body = json.loads(response["body"])
    assert "message" in body
    assert body["message"] == "Hello from Lambda!"
    
    # Verify logging
    assert any("request_id: test-request-id-1234" in record.message 
              for record in caplog.records)

def test_empty_event(lambda_context):
    """Test handling of empty event"""
    response = handler(None, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.BAD_REQUEST
    body = json.loads(response["body"])
    assert "event is empty" in body["message"].lower()

def test_missing_body(lambda_context):
    """Test handling of event without body"""
    event = {"ID": 1}
    response = handler(event, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.BAD_REQUEST
    body = json.loads(response["body"])
    assert "request body is empty" in body["message"].lower()

def test_invalid_json_body(lambda_context):
    """Test handling of invalid JSON in body"""
    event = {
        "body": "invalid json"
    }
    response = handler(event, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.BAD_REQUEST
    body = json.loads(response["body"])
    assert "invalid json" in body["message"].lower()

def test_non_string_body(lambda_context):
    """Test handling of non-string body"""
    event = {
        "body": {"direct": "json"}
    }
    response = handler(event, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.BAD_REQUEST
    body = json.loads(response["body"])
    assert "must be valid a json string" in body["message"].lower()

@pytest.mark.parametrize("invalid_body", [
    None,
    "",
    "{}",
    '{"invalid": "data"}',
])
def test_invalid_body_content(lambda_context, invalid_body):
    """Test various invalid body contents"""
    event = {"body": invalid_body}
    response = handler(event, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.BAD_REQUEST

def test_error_logging(lambda_context, caplog):
    """Test error logging"""
    caplog.set_level(logging.ERROR)
    
    event = {"body": "invalid json"}
    response = handler(event, lambda_context)
    
    assert any(record.levelname == "ERROR" for record in caplog.records)
    assert "request_id: test-request-id-1234" in caplog.text

def test_ddb_table_initialization(lambda_context, valid_event, caplog):
    """Test DynamoDB table initialization"""
    caplog.set_level(logging.INFO)
    
    # First call should initialize table
    response = handler(valid_event, lambda_context)
    assert "Initializing DDB table" in caplog.text
    
    # Clear logs
    caplog.clear()
    
    # Second call should not initialize table again
    response = handler(valid_event, lambda_context)
    assert "Initializing DDB table" not in caplog.text

@pytest.mark.parametrize("event_data,expected_status", [
    ({"body": json.dumps({"name": "John", "email": "john@example.com"})}, HTTPStatus.OK),
    ({"body": "invalid"}, HTTPStatus.BAD_REQUEST),
    ({}, HTTPStatus.BAD_REQUEST),
    (None, HTTPStatus.BAD_REQUEST),
])
def test_various_inputs(lambda_context, event_data, expected_status):
    """Test various input combinations"""
    response = handler(event_data, lambda_context)
    assert response["statusCode"] == expected_status

def test_response_headers(lambda_context, valid_event):
    """Test response headers"""
    response = handler(valid_event, lambda_context)
    
    assert "headers" in response
    assert response["headers"]["Content-Type"] == "application/json"

def test_internal_server_error(lambda_context, monkeypatch):
    """Test internal server error handling"""
    # Simulate an unexpected error
    def mock_json_loads(*args, **kwargs):
        raise Exception("Unexpected error")
    
    monkeypatch.setattr('json.loads', mock_json_loads)
    
    response = handler({"body": "{}"}, lambda_context)
    
    assert response["statusCode"] == HTTPStatus.INTERNAL_SERVER_ERROR
    body = json.loads(response["body"])
    assert "request_id" in body["message"]

# Optional: Integration-style tests
@pytest.mark.integration
def test_end_to_end(lambda_context):
    """Test end-to-end flow"""
    # Setup test data
    test_event = {
        "body": json.dumps({
            "name": "Test User",
            "email": "test@example.com"
        })
    }
    
    # Execute
    response = handler(test_event, lambda_context)
    
    # Verify
    assert response["statusCode"] == HTTPStatus.OK
    body = json.loads(response["body"])
    assert "message" in body

# Test environment configuration
def test_environment_configuration():
    """Test environment variable configuration"""
    assert os.environ.get("DDB_TABLE_NAME") == "test-table"
