import os
from typing import Iterable
from functools import lru_cache

import boto3
from aws_lambda_powertools import Logger
from botocore.exceptions import ClientError
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient

logger = Logger()

USER_POOL_ID = "USER_POOL_ID"
CUSTOM_COMPANY_ID_KEY = "custom:company_id"

class User: 
    company_id: str
    email: str
    position: str


class CognitoUserRepository():
    __session: boto3.Session
    __cognito_client: CognitoIdentityProviderClient

    def __init__(self, session: boto3.Session = None):
        if session:
            self.__session = session
        else:
            self.__session = boto3.Session()

        self.__cognito_client = self.__session.client("cognito-idp")

    def create_user(self, user: User):
        logger.info(
            f'Attempting to create user "{user.email}" for company "{user.company_id}, with position "{user.position}"'
        )
        try:
            self.__cognito_client.admin_create_user(
                UserPoolId=os.getenv(USER_POOL_ID),
                Username=user.email,
                UserAttributes=[
                    {"Name": "email", "Value": user.email},
                    {"Name": "email_verified", "Value": "true"},
                    {"Name": CUSTOM_COMPANY_ID_KEY, "Value": user.company_id},
                    {"Name": "custom:position", "Value": user.position},
                ],
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "UsernameExistsException":
                msg = f'An account for user "{user.email}" already exists!'
                logger.exception(e)
                raise Exception(msg)
            else:
                logger.exception(e)
            raise
        else:
            logger.info(
                f'Created user "{user.email}" for company "{user.company_id}, with position "{user.position}"'
            )

    def update_user(self, user: User):
        logger.info(
            f'Updating user "{user.email}" for company "{user.company_id}, with position "{user.position}"'
        )
        try:
            self.__cognito_client.admin_update_user_attributes(
                UserPoolId=os.getenv(USER_POOL_ID),
                Username=user.email,
                UserAttributes=[
                    {"Name": "email", "Value": user.email},
                    {"Name": "email_verified", "Value": "true"},
                    {"Name": CUSTOM_COMPANY_ID_KEY, "Value": user.company_id},
                    {"Name": "custom:position", "Value": user.position},
                ],
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "UserNotFoundException":
                msg = f'An account for user "{user.email}" does not exist!'
                logger.exception(e)
                raise Exception(msg)
            else:
                logger.exception(e)
            raise
        else:
            logger.info(
                f'Updated user "{user.email}" for company "{user.company_id}, with position "{user.position}"'
            )

    def delete_user(self, user_email):
        logger.info(f'Attempting to delete user "{user_email}"')
        try:
            self.__cognito_client.admin_delete_user(
                UserPoolId=os.getenv(USER_POOL_ID), Username=user_email
            )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(f'Deleted user "{user_email}"')

    def delete_users(self, users: Iterable[User]):
        logger.info("Attempting to delete users.")
        try:
            for user in users:
                self.__cognito_client.admin_delete_user(
                    UserPoolId=os.getenv(USER_POOL_ID), Username=user.email
                )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info("Deleted users.")

    def add_user_to_group(self, user: User, group_name: str):
        logger.info(f'Attempting to add user "{user.email}" to group "{group_name}"')
        try:
            self.__cognito_client.admin_add_user_to_group(
                UserPoolId=os.getenv(USER_POOL_ID),
                Username=user.email,
                GroupName=group_name,
            )
        except Exception as e:
            logger.exception(e)
            raise
        else:
            logger.info(f'Added user "{user.email}" to group "{group_name}"')

    def get_admin_user_emails(self) -> list[str]:
        logger.info("Fetching admin users")
        try:
            result = self.__cognito_client.list_users_in_group(
                UserPoolId=os.getenv(USER_POOL_ID),
                GroupName="super-admin",
            )
        except Exception as e:
            logger.exception(e)
            raise
        else:
            logger.info("Fetched admin users")
            return [
                a["Value"]
                for u in result["Users"]
                for a in u["Attributes"]
                if a["Name"] == "email"
            ]

    def get_moderator_user_emails(self) -> list[str]:
        logger.info("Fetching moderator users")
        try:
            result = self.__cognito_client.list_users_in_group(
                UserPoolId=os.getenv(USER_POOL_ID),
                GroupName="moderator",
            )
        except Exception as e:
            logger.exception(e)
            raise
        else:
            logger.info("Fetched moderator users")
            return [
                a["Value"]
                for u in result["Users"]
                for a in u["Attributes"]
                if a["Name"] == "email"
            ]


