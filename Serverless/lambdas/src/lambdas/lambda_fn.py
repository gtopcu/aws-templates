import json
import os
from datetime import datetime, timezone
import time
import logging

from http import HTTPStatus
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.basicConfig( level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')

# print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
# print(time().strftime("%Y-%m-%d %H:%M:%S"))

# aws lambda invoke \
# --function-name my-function \
# --cli-binary-format raw-in-base64-out \
# --payload '{"name": "Alice", "birthday": "1990-01-01", "email": "alice@gmail.com"}' \
# output.json && cat output.json

ddb_table = None


def handler(event: dict, context: dict):
    request_id = context.aws_request_id

    # logger.info("context: ", context, "event: ", event)
    # logger.info("context: %s, event: %s", context, event)
    logger.debug(f"request_id: {request_id}, context: {context}, event: {event}")

    try:
        global ddb_table
        if ddb_table is None:
            print("Initializing DDB table..")
            # ddb = boto3.resource("dynamodb")
            # ddb_table = ddb.Table(os.environ["DDB_TABLE_NAME"])
            ddb_table = os.environ["DDB_TABLE_NAME"]
    
        if not event:
            raise ValueError("event is empty")

        # method = event["httpMethod"]
        # headers = event["headers"]
        # raw_path = event["rawPath"]
        # path = event["path"]
        # pathParameters = event["pathParameters"]
        # query_string_params = event["queryStringParameters"]
        # request_context = event["requestContext"]
        # body = event["body"]
        
        # Input Validation
        body = event.get("body")
        
        if not body:
            raise ValueError("Request body is empty")
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON in request body")
        else:
            raise ValueError("Request body must be valid a JSON string")

        return {
            "statusCode": HTTPStatus.OK,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Hello from Lambda!"}),
        }
    except ValueError as e:
        logger.debug(f"request_id: {request_id}\nerror: {str(e)}", exc_info=True)
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": json.dumps({"message": f"error: {str(e)}"}),
        }
    except Exception as e:
        logger.error(f"request_id: {request_id}\nerror: {str(e)}", exc_info=True)
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": json.dumps({"message": f"Error processing the request. request_id: {request_id}"}
            ),
        }
