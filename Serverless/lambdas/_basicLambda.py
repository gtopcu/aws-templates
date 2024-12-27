
# import json

# from datetime import datetime, timezone
# import time

# print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
# print(time().strftime("%Y-%m-%d %H:%M:%S"))


# def handler(event:dict, context:dict):
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': {
#             'message': 'Hello from Lambda!',
#             'path': event['path'],
#             'method': event['httpMethod'],
#             'queryStringParameters': event['queryStringParameters'],
#             'headers': event['headers']
#         }
#     }