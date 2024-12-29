
# import json

# from datetime import datetime, timezone
# import time

# print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
# print(time().strftime("%Y-%m-%d %H:%M:%S"))

# aws lambda invoke \
# --function-name my-function \
# --cli-binary-format raw-in-base64-out \
# --payload '{"name": "Alice", "birthday": "1990-01-01", "email": "alice@gmail.com"}' \
# output.json && cat output.json 

# def handler(event:dict, context:dict):
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Content-Type": "application/json"
#         },
#         "body": {
#             "message": "Hello from Lambda!",
#             "path": event["path"],
#             "method": event["httpMethod"],
#             "queryStringParameters": event["queryStringParameters"],
#             "headers": event["headers"],
#             "request_id": context.aws_request_id,
#         }
#     }