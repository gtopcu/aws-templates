import os
from typing import Any, Optional
import json

# pip install aws-lambda-powertools

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
import boto3
from boto3.dynamodb.conditions import Key

# Initialize Powertools
logger = Logger()
tracer = Tracer()
app = APIGatewayHttpResolver()

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "users"))

# ----- API Routes -----

@app.get("/users/<id>")
@tracer.capture_method
def get_user(id: str):
    """Get a user by ID and optionally filter by name"""
    logger.info(f"Getting user with ID: {id}")
    
    name = app.current_event.query_string_parameters.get("name") if app.current_event.query_string_parameters else None
    
    if name:
        # Get specific user with id and name (GetItem)
        response = table.get_item(
            Key={
                "id": id,
                "name": name
            }
        )
        user = response.get("Item")
        
        if not user:
            return {"statusCode": 404, "body": "User not found"}
        
        return {"statusCode": 200, "body": user}
    else:
        # Query all users with the same ID (Query)
        response = table.query(
            KeyConditionExpression=Key("id").eq(id)
        )
        
        return {"statusCode": 200, "body": response.get("Items", [])}

@app.get("/users")
@tracer.capture_method
def list_users():
    """List all users (Scan operation)"""
    logger.info("Listing all users")
    
    # Optional parameters
    limit_param = app.current_event.query_string_parameters.get("limit") if app.current_event.query_string_parameters else None
    
    scan_params = {}
    if limit_param and limit_param.isdigit():
        scan_params["Limit"] = int(limit_param)
    
    response = table.scan(**scan_params)
    users = response.get("Items", [])
    
    return {"statusCode": 200, "body": users}

@app.post("/users")
@tracer.capture_method
def create_user():
    """Create a new user (PutItem operation)"""
    try:
        # Parse request body
        body = json.loads(app.current_event.body)
        
        # Validate required fields
        if not body.get("id") or not body.get("name"):
            return {"statusCode": 400, "body": "Missing required fields: id and name"}
            
        # Save user to DynamoDB
        item = {
            "id": body["id"],
            "name": body["name"],
        }
        
        # Add any additional fields from the request
        for key, value in body.items():
            if key not in ["id", "name"]:
                item[key] = value
        
        logger.info(f"Creating user: {item}")
        table.put_item(Item=item)
        
        return {"statusCode": 201, "body": item}
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        return {"statusCode": 500, "body": f"Error creating user: {str(e)}"}

@app.put("/users/<id>")
@tracer.capture_method
def update_user(id: str):
    """Update a user (UpdateItem operation)"""
    try:
        # Parse request body
        body = json.loads(app.current_event.body)
        
        # Validate name is provided (needed for composite key)
        if not body.get("name"):
            return {"statusCode": 400, "body": "Missing required field: name"}
        
        # Basic validation that the item exists
        existing_user = table.get_item(
            Key={
                "id": id,
                "name": body["name"]
            }
        )
        
        if not existing_user.get("Item"):
            return {"statusCode": 404, "body": "User not found"}
            
        # Prepare update expression and attributes
        update_expression = "SET "
        expression_attribute_values = {}
        
        for key, value in body.items():
            if key not in ["id", "name"]:  # Cannot update primary key fields
                update_expression += f"{key} = :{key}, "
                expression_attribute_values[f":{key}"] = value
        
        # Only update if there are fields to be updated
        if update_expression != "SET ":
            # Remove trailing comma and space from the expression
            update_expression = update_expression[:-2]
            
            logger.info(f"Updating user with ID: {id}, Name: {body['name']}")
            
            table.update_item(
                Key={
                    "id": id,
                    "name": body["name"]
                },
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            
            # Get the updated item
            updated_user = table.get_item(
                Key={
                    "id": id,
                    "name": body["name"]
                }
            ).get("Item")
            
            return {"statusCode": 200, "body": updated_user}
        else:
            return {"statusCode": 400, "body": "No fields to update provided"}
            
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        return {"statusCode": 500, "body": f"Error updating user: {str(e)}"}

@app.delete("/users/<id>")
@tracer.capture_method
def delete_user(id: str):
    """Delete a user (DeleteItem operation)"""
    try:
        # Get name from query parameters
        name = app.current_event.query_string_parameters.get("name") if app.current_event.query_string_parameters else None
        
        if not name:
            return {"statusCode": 400, "body": "Missing required query parameter: name"}
        
        logger.info(f"Deleting user with ID: {id}, Name: {name}")
        
        # Delete the item
        table.delete_item(
            Key={
                "id": id,
                "name": name
            }
        )
        
        return {"statusCode": 204, "body": ""}
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        return {"statusCode": 500, "body": f"Error deleting user: {str(e)}"}

# ----- Lambda Handler -----

@logger.inject_lambda_context(correlation_id_path="requestContext.requestId")
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    """Main Lambda handler function"""
    try:
        return app.resolve(event, context)
    except Exception as e:
        logger.exception("Unhandled exception")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Internal Server Error: {str(e)}"})
        }