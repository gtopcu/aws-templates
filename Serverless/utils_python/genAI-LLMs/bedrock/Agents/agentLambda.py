
# https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/bedrock_agents/
# https://www.youtube.com/watch?v=NWoC5FTSt7s
# https://www.youtube.com/watch?v=2L_XE6g3atI

from distutils import version # Deprecated since version 3.10, removed in version 3.12.
import requests

def powertools_version() -> str:
    response = requests.get("https://pypi.org/pypi/aws-lambda-powertools/json")
    response.raise_for_status()

    data = response.json()
    releases = data["releases"]

    versions = []
    for release in releases:
        versions.append(version.parse(release))
    return max(versions).public

def schedule_meeting(email:str) -> str:
    return "Scheduled meeting with: " + email

def lambda_handler(event:dict, context:dict):
    action_group = event["actionGroup"]
    action = event["action"]
    api_path = event["apiPath"]
    http_method = event["httpMethod"]
    parameters: list[dict] = event["parameters"]

    if api_path == "/latest_version" and http_method == "GET":
        body = powertools_version()
    elif api_path == "/schedule_meeting" and http_method == "POST":
        email = next((param["value"] for param in parameters if param["name"] == "email"), None)
        body = schedule_meeting(email)
    else:
        body = { "{}::{}::{} is not a valid api call".format(http_method, action, api_path)  }

    response_body = {
        "application/json": {
            "body": str(body)
        }
    }

    action_response = {
        "actionGroup": action_group,
        "apiPath": api_path,
        "httpMethod": http_method,
        "httpStatusCode": "200",
        "responseBody": response_body
    }

    return { "messageVersion": "1.0", "response": action_response }
        
        

