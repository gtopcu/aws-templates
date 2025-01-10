# from http import HTTPStatus
# from lambdas.lambda_fn import handler
# from unittest.mock import MagicMock
# from unittest.mock import Mock
# import json
# import pytest

# class TestLambdaFn:

#     def test_handler_empty_body(self):
#         """
#         Test handler with an empty body in the event.
#         """
#         event = {
#             "body": None
#         }
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Request body is empty"}

#     def test_handler_empty_event(self):
#         """
#         Test handler function with an empty event.
#         """
#         # Arrange
#         event = {}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         # Act
#         result = handler(event, context)

#         # Assert
#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Request body is empty"}

#     def test_handler_empty_event_2(self):
#         """
#         Test handler with an empty event.
#         """
#         event = {}
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: event is empty"}

#     def test_handler_invalid_json_body(self):
#         """
#         Test handler function with an invalid JSON string body.
#         """
#         # Arrange
#         event = {
#             "body": "invalid json"
#         }
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         # Act
#         result = handler(event, context)

#         # Assert
#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Invalid JSON in request body"}

#     def test_handler_invalid_json_body_2(self):
#         """
#         Test handler with an invalid JSON body in the event.
#         """
#         event = {
#             "body": "invalid json"
#         }
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Invalid JSON in request body"}

#     def test_handler_non_string_body(self):
#         """
#         Test handler function with a non-string body.
#         """
#         # Arrange
#         event = {
#             "body": {"key": "value"}
#         }
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         # Act
#         result = handler(event, context)

#         # Assert
#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Request body must be valid a JSON string"}

#     def test_handler_non_string_body_2(self):
#         """
#         Test handler with a non-string body in the event.
#         """
#         event = {
#             "body": {"key": "value"}
#         }
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"]) == {"message": "error: Request body must be valid a JSON string"}

#     def test_handler_success(self):
#         """Test handler for successful execution"""
#         event = {"body": json.dumps({"key": "value"})}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.OK
#         assert result["headers"] == {"Content-Type": "application/json"}
#         assert json.loads(result["body"])["message"] == "Hello from Lambda!"

#     def test_handler_valid_json_body(self):
#         """
#         Test handler function with a valid JSON string body.
#         """
#         # Arrange
#         event = {
#             "body": json.dumps({"key": "value"})
#         }
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         # Act
#         result = handler(event, context)

#         # Assert
#         assert result["statusCode"] == HTTPStatus.OK
#         assert result["headers"] == {"Content-Type": "application/json"}
#         assert json.loads(result["body"]) == {"message": "Hello from Lambda!"}

#     def test_handler_valid_json_body_2(self):
#         """
#         Test handler function with a valid JSON string body.
#         """
#         # Arrange
#         event = {
#             "body": json.dumps({"key": "value"})
#         }
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         # Act
#         result = handler(event, context)

#         # Assert
#         assert result["statusCode"] == HTTPStatus.OK
#         assert result["headers"] == {"Content-Type": "application/json"}
#         assert json.loads(result["body"]) == {"message": "Hello from Lambda!"}

#     def test_handler_valid_json_body_3(self):
#         """
#         Test handler with a valid JSON body in the event.
#         """
#         event = {
#             "body": json.dumps({"key": "value"})
#         }
#         context = MagicMock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.OK
#         assert result["headers"] == {"Content-Type": "application/json"}
#         assert json.loads(result["body"]) == {"message": "Hello from Lambda!"}

#     def test_handler_when_body_is_empty(self):
#         """Test handler when body is empty"""
#         event = {"body": None}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"])["message"] == "error: Request body is empty"

#     def test_handler_when_body_is_invalid_json(self):
#         """Test handler when body is invalid JSON"""
#         event = {"body": "invalid json"}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"])["message"] == "error: Invalid JSON in request body"

#     def test_handler_when_body_is_not_string(self):
#         """
#         Test handler when body is not a string
#         """
#         event = {"body": {"key": "value"}}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"])["message"] == "error: Request body must be valid a JSON string"

#     def test_handler_when_event_is_empty(self):
#         """Test handler when event is empty"""
#         event = {}
#         context = Mock()
#         context.aws_request_id = "test-request-id"

#         result = handler(event, context)

#         assert result["statusCode"] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result["body"])["message"] == "error: event is empty"

#     def test_handler_with_empty_event(self):
#         """
#         Test handler with an empty event dictionary
#         """
#         event = {}
#         context = type('Context', (), {'aws_request_id': 'test_request_id'})()
        
#         result = handler(event, context)
        
#         assert result['statusCode'] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result['body'])['message'] == "error: event is empty"

#     def test_handler_with_invalid_json_body(self):
#         """
#         Test handler with an invalid JSON string in the body
#         """
#         event = {'body': '{invalid json}'}
#         context = type('Context', (), {'aws_request_id': 'test_request_id'})()
        
#         result = handler(event, context)
        
#         assert result['statusCode'] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result['body'])['message'] == "error: Invalid JSON in request body"

#     def test_handler_with_missing_body(self):
#         """
#         Test handler with an event missing the 'body' key
#         """
#         event = {'some_key': 'some_value'}
#         context = type('Context', (), {'aws_request_id': 'test_request_id'})()
        
#         result = handler(event, context)
        
#         assert result['statusCode'] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result['body'])['message'] == "error: Request body is empty"

#     def test_handler_with_non_string_body(self):
#         """
#         Test handler with a non-string body
#         """
#         event = {'body': {'key': 'value'}}
#         context = type('Context', (), {'aws_request_id': 'test_request_id'})()
        
#         result = handler(event, context)
        
#         assert result['statusCode'] == HTTPStatus.BAD_REQUEST
#         assert json.loads(result['body'])['message'] == "error: Request body must be valid a JSON string"

#     def test_handler_with_unexpected_exception(self):
#         """
#         Test handler with an unexpected exception
#         """
#         event = {'body': '{"key": "value"}'}
#         context = type('Context', (), {'aws_request_id': 'test_request_id'})()
        
#         # Simulate an unexpected exception
#         with pytest.raises(Exception):
#             raise Exception("Unexpected error")
        
#         result = handler(event, context)
        
#         assert result['statusCode'] == HTTPStatus.INTERNAL_SERVER_ERROR
#         assert json.loads(result['body'])['message'] == f"Error processing the request. request_id: {context.aws_request_id}"