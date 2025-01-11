import json
import os
import logging
import boto3
from http import HTTPStatus
from typing import Any
from datetime import datetime
from botocore.exceptions import ClientError


"""
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/TABLE_NAME"
        }
    ]
}

GET /items?id=12345
POST /items
{
    "id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
}
"""

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def validate_post_body(body: dict[str, Any]) -> None:
    """Validate the POST request body contains required fields with correct types."""
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

def validate_get_params(params: dict[str, str]) -> str:
    """Validate and extract ID from query parameters."""
    if not params or 'id' not in params:
        raise ValueError("Missing required query parameter: id")
    
    item_id = params['id'].strip()
    if not item_id:
        raise ValueError("ID parameter cannot be empty")
    
    return item_id

def handle_post_request(body: dict) -> dict:
    """Handle POST request to create new item."""
    # Validate request body
    validate_post_body(body)
    
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

def handle_get_request(query_params: dict) -> dict:
    """Handle GET request to retrieve item by ID."""
    # Validate and extract ID from query parameters
    item_id = validate_get_params(query_params)
    
    try:
        # Get item from DynamoDB
        response = table.get_item(
            Key={
                'id': item_id
            }
        )
        
        # Check if item exists
        if 'Item' not in response:
            return {
                'statusCode': HTTPStatus.NOT_FOUND,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'error': f'Item with ID {item_id} not found'
                })
            }
        
        return {
            'statusCode': HTTPStatus.OK,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response['Item'])
        }
        
    except ClientError as e:
        logger.error("DynamoDB error: %s", str(e))
        raise

def lambda_handler(event: dict, context: dict) -> dict:
    """Handle POST and GET requests from API Gateway."""
    logger.info("Received event: %s", json.dumps(event))
    
    try:
        http_method = event.get('httpMethod')
        
        if http_method == 'POST':
            # Check if body exists and parse it
            if 'body' not in event:
                raise ValueError("Missing request body")
                
            body = event['body']
            if isinstance(body, str):
                try:
                    body = json.loads(body)
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON in request body")
            
            return handle_post_request(body)
            
        elif http_method == 'GET':
            query_params = event.get('queryStringParameters')
            return handle_get_request(query_params)
            
        else:
            return {
                'statusCode': HTTPStatus.METHOD_NOT_ALLOWED,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'error': f'Method {http_method} not allowed'
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
