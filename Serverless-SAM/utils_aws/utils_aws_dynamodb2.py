# Code whisperer: Option + C
import boto3

dynamodb = boto3.resource('dynamodb')

# https://dynobase.dev/dynamodb-python-with-boto3/#get-item

def get_item(table_name, key):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response

def put_item(table_name, item):
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)

def update_item(table_name, key, updateExpression, expressionAttributeValues):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=updateExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

def delete_item(table_name, key):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key=key)
    return response

def query(table_name, keyConditionExpression, expressionAttributeValues):
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=keyConditionExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

def scan(table_name):
    table = dynamodb.Table(table_name)
    response = table.scan()
    return response