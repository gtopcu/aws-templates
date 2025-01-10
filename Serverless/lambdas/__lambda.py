import json
import os
from datetime import datetime, timezone
import time
import logging

from http import HTTPStatus

# logger = logging.getLogger(__name__)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
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


# ddb_employees = EmployeeTable.init_ddb(os.environ["DDB_TABLE_NAME"])


def handler(event: dict, context: dict):
    logger.info("context: ", context, "event: ", event)

    try:
        # request_id = context.aws_request_id
        # method = event["httpMethod"]
        # headers = event["headers"]
        # raw_path = event["rawPath"]
        # path = event["path"]
        # pathParameters = event["pathParameters"]
        # query_string_params = event["queryStringParameters"]
        # request_context = event["requestContext"]
        # body = event["body"]
        
        return {
            "statusCode": HTTPStatus.OK,
            "headers": {"Content-Type": "application/json"},
            "body": {
                "message": "Hello from Lambda!",
            },
        }
    except Exception as e:
        logger.error(str(e), exc_info=True)
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            # "statusCode": HTTPStatus.BAD_REQUEST,
            "body": {
                "message": "Error processing the request",
            },
        }


def test_func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

def test():
    params = {
        "a": 1,
        "b": 2,
        "c": 3,}
    test_func(**params)

if __name__ == "__main__":
    test()