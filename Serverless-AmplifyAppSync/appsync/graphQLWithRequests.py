import os
import logging
from typing import Optional

import boto3
import requests
from requests_aws4auth import AWS4Auth

from exceptions import BadGraphqlRequest, ImproperlyConfigured

logger = logging.getLogger(__name__)


class AppsyncClient:
    def __init__(
            self,
            graphql_endpoint: Optional[str] = None,
            session: Optional[requests.Session] = None,
    ):
        self._graphql_endpoint = graphql_endpoint
        if not session:
            self._session = self._generate_aws4auth_request_session()

    @staticmethod
    def _generate_aws4auth_request_session():
        """
        Create a request session with correct aws credentials.
        Reads the credentials from the Iam role session
        :return: A request session with aws authentication headers
        """
        logger.info("Generating request session with aws4 auth tokens")
        session = requests.Session()

        credentials = boto3.session.Session().get_credentials()

        session.auth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            os.environ['REGION'],
            'appsync',
            session_token=credentials.token
        )

        logger.info(
            "Success in generating request session with aws4 auth tokens"
        )

        return session

    @staticmethod
    def get_data_from_graphql_response(response_json: dict):
        """
        Return dictionary belonging to the graphql query name in
        Appsync Graphql responses.
        Given:
            {
                "data": {
                    "getSDAverageAwakenessGraphDataByReportVideoID": {
                        cool_data
                    }
                }
            }
        Returns: cool_data
        :param response_json: Json dict representing graphql response
        :return: data dictionary from the graphql response
        """
        return response_json['data'][next(iter(response_json['data']))]

    def query_appsync(
            self,
            query: str,
            query_input: dict,
            graphql_endpoint: Optional[str] = None,
            parse_response: bool = True,
    ) -> dict:
        """
        Base generic method that is used for calling appsync resolvers.
        :param query: graphql query to be used
        :param query_input: graphql parameters
        :param graphql_endpoint: graphql endpoint
        :param parse_response: A boolean value to indicate parsing response
        before returning
        :return: json data containing the Appsync response
        """
        if not graphql_endpoint:
            if not self._graphql_endpoint:
                raise ImproperlyConfigured("Graphql endpoint not provided!")
            graphql_endpoint = self._graphql_endpoint

        response = self._session.request(
            url=graphql_endpoint,
            method='POST',
            json={
                'query': query,
                'variables': query_input
            }
        )

        response.raise_for_status()

        response_json = response.json()
        if response_json.get('errors'):
            raise BadGraphqlRequest(
                f'Faulty Graphql Request',
                response_json['errors'],
                query,
                query_input
            )

        if parse_response:
            return self.get_data_from_graphql_response(response_json)

        return response_json