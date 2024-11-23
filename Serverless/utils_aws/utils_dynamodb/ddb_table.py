

import boto3
from botocore.exceptions import ClientError

import boto3.dynamodb.table
import boto3.dynamodb.conditions
import boto3.dynamodb.types
import boto3.dynamodb.transform

dynamo: boto3.session.Session.resource = boto3.resource('dynamodb')
table: boto3.dynamodb.table.Table = dynamo.Table('table-1')
table_resouce: boto3.dynamodb.table.TableResource = table.TableResource()


def lambda_handler(event, context):
    try:
        table.put_item(Item=event)
        return {
            'statusCode': 201,
            'body': event
        }
    except ClientError as e:
        print(e)
        return {
            'statusCode': 500,
            'body': e
        }   


# class ddb_table:

#     def __init__(self, table_name:str):
#         table: boto3.dynamodb.table = boto3.resource('dynamodb').Table(table_name)
#         table_resouce = table.TableResource()
#         table_resouce.
        

#     # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#     def put_item(self, item: dict) -> None:
        
#         self.table.put_item(Item=item)
        
