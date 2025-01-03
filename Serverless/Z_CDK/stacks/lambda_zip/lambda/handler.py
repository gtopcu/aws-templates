import json
import requests


def lambda_handler(event, context):
    try:
        response = requests.get("https://api.example.com/data")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Success", "data": response.json()}),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"Error": str(e)})}
