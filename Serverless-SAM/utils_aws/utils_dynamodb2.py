# Code whisperer: Option + C
import boto3

dynamodb = boto3.resource('dynamodb')

# https://dynobase.dev/dynamodb-python-with-boto3/#get-item

def getItem(tableName, key):
    table = dynamodb.Table(tableName)
    response = table.get_item(Key=key)
    return response

def putItem(tableName, item):
    table = dynamodb.Table(tableName)
    table.put_item(Item=item)

def updateItem(tableName, key, updateExpression, expressionAttributeValues):
    table = dynamodb.Table(tableName)
    response = table.update_item(
        Key=key,
        UpdateExpression=updateExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

def deleteItem(tableName, key):
    table = dynamodb.Table(tableName)
    response = table.delete_item(Key=key)
    return response

def query(tableName, keyConditionExpression, expressionAttributeValues):
    table = dynamodb.Table(tableName)
    response = table.query(
        KeyConditionExpression=keyConditionExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

def scan(tableName):
    table = dynamodb.Table(tableName)
    response = table.scan()
    return response