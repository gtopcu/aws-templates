import os
import re
import sys

from aws_libs.core.utils import get_current_datetime

from platform_backend import secrets_config
from platform_backend.aws_resources_configs.dynamodb import \
    dynamodb_tables
from platform_backend.utils.api.appsync.graphql_queries import (
    create_institution_query,
    create_user_info_query,
)
from platform_backend.utils.api.appsync.utils import AppsyncClient
from platform_backend.utils.auth.utils import AwsCognitoUserPoolClient

import boto3


dynamodb = boto3.resource("dynamodb")


def _user_data_is_valid(user_data):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    allowed_user_types = {"SME", "Corporate"}
    return (
        re.fullmatch(email_regex, user_data["email"])
        and user_data["user_type"] in allowed_user_types
    )


def _create_institution_plan(env, institution_id, plan_type="PAID"):
    institution_table = dynamodb.Table(dynamodb_tables[env]["institution_plan"])
    date_time = get_current_datetime()
    institution_plan_record = {
        "institutionID": institution_id,
        "planType": plan_type,
        "createdAt": date_time,
        "updatedAt": date_time,
    }
    print(
        "Creating institution plan record:"
        f" {institution_plan_record}"
    )
    institution_table.put_item(Item=institution_plan_record)


if __name__ == '__main__':
    backend_environment = "prod"
    user_pool_id = secrets_config.cognito_user_pool_ids[backend_environment]
    appsync_graphql_endpoint = secrets_config.appsync_api_endpoints[
        backend_environment
    ]

    user_data = {
        "email": "burak@guul.games",
        "first_name": "Halil Burak",
        "last_name": "Yilmaz",
        "institution_name": "Guul Games",
        "institution_code": "guul_games",
        "user_type": "Corporate",
        # "user_type": "Higher Education",
    }

    if not _user_data_is_valid(user_data):
        print(
            "User data is not valid for creating a new user, please correct"
            "it and try again"
        )
        sys.exit()

    # create a user in the cognito user pool
    cognito_client = AwsCognitoUserPoolClient(user_pool_id)
    username = cognito_client.create_new_user(user_data["email"])

    os.environ['AWS_DEFAULT_PROFILE'] = "appsync-admin"
    appsync_client = AppsyncClient(appsync_graphql_endpoint)

    # create an institution with appsync query
    institution_data = {
        "name": user_data["institution_name"],
        "code": user_data["institution_code"],
    }
    institution_query_response = appsync_client.query_appsync(
        create_institution_query, {"input": institution_data}
    )
    print(
        "Institution Created Successfully. Returned response:"
        f" {institution_query_response}"
    )
    institution_id = institution_query_response["id"]

    # create a user info with appsync query
    user_info_data = {
        "userId": username,
        "institutionId": institution_id,
        "role": "Admin",
        "userType": user_data["user_type"],
        "firstName": user_data["first_name"],
        "lastName": user_data["last_name"],
        "displayName": user_data["first_name"] + " " + user_data["last_name"],
        "privacyAgreement": False,
        "privacyAgreementDate": "08/08/2020",
        "newsSubscription": False,
    }
    user_info_query_response = appsync_client.query_appsync(
        create_user_info_query,
        {"input": user_info_data},
    )
    print(
        "User Info Created Successfully. Returned response:"
        f" {user_info_query_response}"
    )

    del os.environ['AWS_DEFAULT_PROFILE']

    _create_institution_plan(backend_environment, institution_id)