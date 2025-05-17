
import json
import os

import boto3
from botocore.exceptions import ClientError

import boto3.dynamodb.table
import boto3.dynamodb.conditions
import boto3.dynamodb.types
import boto3.dynamodb.transform

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('table-1')
# table_resource: boto3.dynamodb.table.TableResource = table.TableResource()


def lambda_handler(event, context):    
    try:
        item = json.loads(event["body"])
        table.put_item(Item=item)
        return {
            'statusCode': 201,
            'body': event
        }
    except ClientError as err:
        # print(str(err))
        print("Error Code: " + f"{err.response['Error']['Code']}")
        print("Error Message: " + f"{err.response['Error']['Message']}")

