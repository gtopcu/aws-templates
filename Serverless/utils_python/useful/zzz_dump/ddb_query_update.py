
import os

from aws_lambda_powertools import Logger

import boto3
from boto3.dynamodb.conditions import Key

DDB_TABLE = "employees"
DDB_PARTITION_KEY = "PK"
DDB_PARTITION_KEY_VALUE = "1000"

ddb = boto3.resource("dynamo")
table = ddb.Table(DDB_TABLE)

logger = Logger()

def dd_query_update() -> None:

    try:
        updated_count = 0
        kwargs = {}
        while True:
            response = table.query(
                KeyConditionExpression=Key(DDB_PARTITION_KEY).eq(DDB_PARTITION_KEY_VALUE),
                **kwargs,
            )
            logger.info(f"Fetched {response["Count"]} results from DynamoDB.")

            for item in response["Items"]:    
                try:
                    old_address = item["address"]
                    new_address = "address"
                    
                    table.update_item(
                        Key={
                            DDB_PARTITION_KEY: DDB_PARTITION_KEY_VALUE,
                            "SK": "sort_key",
                        },
                        UpdateExpression="REMOVE address SET new_address = :val",
                        ExpressionAttributeValues={
                            ":val": new_address
                        },
                    )
                    logger.info(f"Updated DDB")
                    updated_count += 1
                except Exception as e:
                    logger.exception(f"Error updating DDB: {e}")

            if "LastEvaluatedKey" in response:
                kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
            else:
                break

        logger.info(f"Successfully updated {updated_count} items in DDB")

    except Exception as e:
        logger.exception(f"Error updating DDB: {e}")
        raise

if __name__ == "__main__":
    pass