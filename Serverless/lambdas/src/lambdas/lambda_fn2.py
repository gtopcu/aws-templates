import json
import os
import logging
import boto3
from http import HTTPStatus
from typing import Any
from datetime import datetime

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def validate_request_body(body: dict[str, Any]) -> None:
    """Validate the request body contains required fields with correct types."""
    required_fields = {
        'id': str,
        'name': str,
        'email': str
    }
    
    for field, field_type in required_fields.items():
        if field not in body:
            raise ValueError(f"Missing required field: {field}")
        if not isinstance(body[field], field_type):
            raise ValueError(f"Invalid type for {field}. Expected {field_type.__name__}")
        if not body[field].strip():  # Check for empty strings
            raise ValueError(f"Field {field} cannot be empty")

def lambda_handler(event: dict, context: dict) -> dict:
    """Handle POST requests from API Gateway and write to DynamoDB."""
    logger.info("Received event: %s", json.dumps(event))
    
    try:
        # Check if body exists and parse it
        if 'body' not in event:
            raise ValueError("Missing request body")
            
        body = event['body']
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON in request body")
        
        # Validate request body
        validate_request_body(body)
        
        # Add timestamp to the item
        timestamp = datetime.now(datetime.timezone.utc).isoformat()
        item = {
            **body,
            'timestamp': timestamp
        }
        
        # Write to DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': HTTPStatus.CREATED,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Item created successfully',
                'id': body['id']
            })
        }
        
    except ValueError as e:
        logger.warning("Validation error: %s", str(e))
        return {
            'statusCode': HTTPStatus.BAD_REQUEST,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }
        
    except Exception as e:
        logger.error("Internal error: %s", str(e), exc_info=True)
        return {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Internal server error'
            })
        }
