
import json

def lambda_handler(event, context):

    print("In lambda handler")
    print(event)

    # Parse Query String
    queryParam = event["queryStringParameters"]["param1"]
    print(queryParam)

    # Parse Request Body
    orderID = event["requestParameters"]["orderID"]
    
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Hello World"
    }

    return resp
