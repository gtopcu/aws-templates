import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "Hello, AWS Solutions Constructs! You have hit {}\n".format(event['path'])
    }