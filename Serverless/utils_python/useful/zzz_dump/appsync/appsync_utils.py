
import os
import requests
from requests import Response, Timeout
from pydantic import BaseModel

from aws_lambda_powertools import Logger, Tracer

"""
aws appsync list-api-keys --api-id yd3lmvxh45hehmxhz6zhqz7hym --profile default

import boto3
import json

def get_appsync_api_keys(api_id, region='us-east-1'):
    client = boto3.client('appsync', region_name=region)
    
    try:
        response = client.list_api_keys(apiId=api_id)
        return response['apiKeys']
    except Exception as e:
        print(f"Error: {e}")
        return None

api_keys = get_appsync_api_keys('your-api-id')
if api_keys:
    for key in api_keys:
        print(f"Key ID: {key['id']}")
        print(f"Description: {key.get('description', 'No description')}")

"""

ENV_APPSYNC_ENDPOINT_URL = "APPSYNC_ENDPOINT_URL"
ENV_APPSYNC_API_KEY = "APPSYNC_API_KEY"

logger = Logger(service="GraphQLService")

def execute_gql(query: str, variables: dict | None = None) -> dict:
    """
    Executes the requested graphql query, with the associated variables.

    :param query:     The query to be executed. This is usually a templated query.
    :param variables: The associated variables values for the query.
    :return: The json response from the query call.
    """
    api_url = os.environ[ENV_APPSYNC_ENDPOINT_URL]
    api_key = os.environ[ENV_APPSYNC_API_KEY]
    
    request_body_json = {"query": query, "variables": variables}
    
    logger.info(f"Sending GraphQL request to: {api_url} Query: {request_body_json}")
    response = requests.post(
        api_url,
        json=request_body_json,
        headers={
            "Content-Type": "application/graphql",
            "x-api-key": api_key,
        },
    )
    logger.info("GraphQL Response: ", response.json())
    if response.status_code != 200 or response.json().get("errors") is not None:
        e = Exception(
            f"Query failed: {response.request.body}. "
            f"Response: {response.json()}"
        )
        logger.exception(e)
        raise e

    logger.info(f"Query successful. Response: {response.request.body}. ")
    return response.json()


def send_message_event(
    _id: str,
    timestamp: str,
    conversation_id: str,
    sender: str,
    message: str,
):
    query = """
        mutation aiPublishMessage($event: NewConversationEvent!) {
            aiPublishMessage(event: $event) {
                id
                timestamp
                conversationId
                sender
                message
            }
        }
    """

    variables = {
        "event": {
            "id": _id,
            "timestamp": timestamp,
            "conversationId": conversation_id,
            "sender": sender,
            "message": message,
        }
    }

    execute_gql(query=query, variables=variables)


