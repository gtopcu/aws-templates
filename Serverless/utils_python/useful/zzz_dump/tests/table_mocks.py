import os
from typing import Optional

import boto3

from secr.repository.company_repository import ICompanyRepository
from secr.repository.dynamodb import dd_company_repository
from secr.repository.processed_customer_data_repository import IProcessedCustomerDataItemRepository


def mock_processed_cust_data_repo() -> ICompanyRepository:
    return dd_company_repository.get_company_repository()

def create_dd_table(
    table,
    table_env_variable,
    partition_key,
    sort_key,
    additional_attributes: Optional[list[dict]] = None,
    global_secondary_indexes: Optional[list[dict]] = None,
):
    if additional_attributes is None:
        additional_attributes = []
    os.environ[table_env_variable] = table
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

    with mock_aws():  # ensure the table isn't really created if tests are misconfigured
        client = boto3.client("dynamodb")
        client.create_table(
            AttributeDefinitions=[
                {
                    "AttributeName": partition_key,
                    "AttributeType": "S",
                },
                {
                    "AttributeName": sort_key,
                    "AttributeType": "S",
                },
                *additional_attributes,
            ],
            TableName=table,
            KeySchema=[
                {
                    "AttributeName": partition_key,
                    "KeyType": "HASH",
                },
                {
                    "AttributeName": sort_key,
                    "KeyType": "RANGE",
                },
            ],
            BillingMode="PAY_PER_REQUEST",
            **non_null_dict_items({"GlobalSecondaryIndexes": global_secondary_indexes}),
        )
