# import json
# import pytest
# from http import HTTPStatus
# from lambdas.lambda_fn import handler

# # Mock AWS context object
# class MockContext:
#     def __init__(self):
#         self.aws_request_id = "test-request-id"

# @pytest.fixture
# def context():
#     return MockContext()

# @pytest.fixture
# def valid_event():
#     return {
#         "body": json.dumps({"test": "data"})
#     }

# def test_successful_request(valid_event, context):
#     response = handler(valid_event, context)
    
#     assert response["statusCode"] == HTTPStatus.OK
#     assert "Content-Type" in response["headers"]
#     assert response["headers"]["Content-Type"] == "application/json"
    
#     body = json.loads(response["body"])
#     assert "message" in body
#     assert body["message"] == "Hello from Lambda!"

# def test_empty_event(context):
#     response = handler({}, context)
    
#     assert response["statusCode"] == HTTPStatus.BAD_REQUEST
#     body = json.loads(response["body"])
#     assert "message" in body
#     assert "error: event is empty" in body["message"]

# def test_missing_body(context):
#     event = {"headers": {}}
#     response = handler(event, context)
    
#     assert response["statusCode"] == HTTPStatus.BAD_REQUEST
#     body = json.loads(response["body"])
#     assert "message" in body
#     assert "error: Request body is empty" in body["message"]

# def test_invalid_json_body(context):
#     event = {
#         "body": "invalid json"
#     }
#     response = handler(event, context)
    
#     assert response["statusCode"] == HTTPStatus.BAD_REQUEST
#     body = json.loads(response["body"])
#     assert "message" in body
#     assert "error: Invalid JSON in request body" in body["message"]

# def test_non_string_body(context):
#     event = {
#         "body": {"test": "data"}  # Body should be a JSON string, not a dict
#     }
#     response = handler(event, context)
    
#     assert response["statusCode"] == HTTPStatus.BAD_REQUEST
#     body = json.loads(response["body"])
#     assert "message" in body
#     assert "error: Request body must be valid a JSON string" in body["message"]

# @pytest.fixture
# def mock_dynamodb_table(monkeypatch):
#     class MockTable:
#         def __init__(self):
#             pass
    
#     monkeypatch.setenv("DDB_TABLE_NAME", "test-table")
#     return MockTable()

# def test_environment_variables(mock_dynamodb_table):
#     import os
#     assert "DDB_TABLE_NAME" in os.environ
#     assert os.environ["DDB_TABLE_NAME"] == "test-table"
