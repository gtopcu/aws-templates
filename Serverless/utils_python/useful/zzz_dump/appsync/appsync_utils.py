
import os
import requests
from requests import Response, Timeout

from aws_lambda_powertools import Logger, Tracer

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
