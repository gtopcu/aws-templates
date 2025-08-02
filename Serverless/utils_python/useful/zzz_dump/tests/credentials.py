import json
import os

import boto3
from pydantic import BaseModel

RDS_HOST_ENV = "RDS_HOST_URL"
RDS_PORT_ENV = "RDS_PORT"
RDS_DBNAME_ENV = "RDS_DBNAME"
PASSWORD_SECRET_ENV = "RDS_PASSWORD_ARN"

__secretsmanager_client = None


class Credentials(BaseModel):
    user: str
    password: str
    host: str
    port: int
    dbname: str
    options: str

    def get_conninfo(self) -> dict:
        return self.model_dump(mode="json")


class CredentialsManager:
    def __init__(self):
        self.__client = get_secretsmanager()

    def get_credentials(self) -> Credentials:
        pwd_secret_arn = os.environ[PASSWORD_SECRET_ENV]
        pwd_secret_response = self.__client.get_secret_value(SecretId=pwd_secret_arn)

        host = os.environ[RDS_HOST_ENV]
        port = int(os.environ[RDS_PORT_ENV])
        dbname = os.environ[RDS_DBNAME_ENV]
        secret = json.loads(pwd_secret_response["SecretString"])

        return Credentials(
            user=secret["username"],
            password=secret["password"],
            port=port,
            host=host,
            dbname=dbname,
            options="-c search_path=secr_data,public",
        )


def get_secretsmanager():
    global __secretsmanager_client
    if client := __secretsmanager_client:
        return client
    else:
        __secretsmanager_client = boto3.client(service_name="secretsmanager")
        return __secretsmanager_client
