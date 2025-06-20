
import os
import requests
from requests import Response, Timeout

ENV_APPSYNC_API_KEY = "APPSYNC_API_KEY"
ENV_APPSYNC_ENDPOINT_URL = "APPSYNC_ENDPOINT_URL"

def execute_gql(query: str, variables: dict | None = None) -> dict:
    """
    Executes the requested graphql query, with the associated variables.

    :param query:     The query to be executed. This is usually a templated query.
    :param variables: The associated variables values for the query.
    :return: The json response from the query call.
    """
    response = requests.post(
        os.environ[ENV_APPSYNC_ENDPOINT_URL],
        json={"query": query, "variables": variables},
        headers={
            "Content-Type": "application/graphql",
            "x-api-key": os.environ[ENV_APPSYNC_API_KEY],
        },
    )
    print(response.json())
    if response.status_code != 200 or response.json().get("errors") is not None:
        raise Exception(
            f"The following query failed: {response.request.body}. "
            f"Response: {response.json()}"
        )
    return response.json()