
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
    if not api_url:
        raise Exception("APPSYNC_ENDPOINT_URL env not set")
    api_key = os.environ[ENV_APPSYNC_API_KEY]
    if not api_key:
        raise Exception("APPSYNC_API_KEY env not set")
    
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

notification_mutation = """
mutation NotificationQuery($companyId: String!, $notificationType: NotificationType!, $facilityId: String, $sourceId: String, $fileName: String, $message: String) {
    createNotification(companyId: $companyId, notificationType: $notificationType, facilityId: $facilityId, sourceId: $sourceId, fileName: $fileName, message: $message) {
        companyId
        notificationId
        notificationType
        notificationStatus
        creationDatetime
        facilityId
        sourceId
        fileName
        message
    }
}
"""

class NotificationRequest(BaseModel):
    company_id: str
    notification_type: str
    facility_id: str | None = None
    source_id: str | None = None
    file_name: str | None = None
    message: str | None = None

def send_notification(request: NotificationRequest) -> dict:
    variables = {
        "companyId": request.company_id,
        "notificationType": request.notification_type,
        "facilityId": request.facility_id,
        "sourceId": request.source_id,
        "fileName": request.file_name,
        "message": request.message,
    }
    return execute_gql(query=notification_mutation, variables=variables)

