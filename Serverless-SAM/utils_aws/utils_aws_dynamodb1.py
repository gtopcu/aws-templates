
# Code whisperer: Option + C
# https://www.youtube.com/watch?v=twxM7WTfhGs
# https://dynobase.dev/dynamodb-python-with-boto3/

import boto3
from boto3.dynamodb.conditions import Key, Attr
# from boto3.dynamodb.types import STRING
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

# import botocore
# from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

# https://dynobase.dev/dynamodb-python-with-boto3/#get-item

# Use port 8000 for DynamoDB Local and 4569 for DynamoDB from LocalStack
# dynamodb = boto3.resource('dynamodb',
#                          region_name=region,
#                          endpoint_url='http://localhost:8000')

# client = boto3.client('dynamodb',
#                       aws_access_key_id='yyyy',
#                       aws_secret_access_key='xxxx',
#                       region_name='us-east-1')

# from botocore.config import Config
# my_config = Config(
#    connect_timeout = 1.0,
#    read_timeout = 1.0
# )
# dynamodb = boto3.resource('dynamodb', config=my_config)

# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html
def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = TypeDeserializer()
    return {
        k: deserializer.deserialize(v) 
        for k, v in dynamo_object.items()
    }  
  
def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {
        k: serializer.serialize(v)
        for k, v in python_object.items()
    }

def get_item(table_name, key):
    """ Key={"id": id} """
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key) 
    return response

def put_item(table_name, item):
    table = dynamodb.Table(table_name)
    return table.put_item(Item=item)
    """
    Item={
        'id': 1,
        'title': 'my-document-title',
        'content': 'some-content',
    }
    """
def update_item(table_name, key, updateExpression, expressionAttributeValues):
    """
    Key={
            'id': '894673'
        },
        UpdateExpression='SET country = :newCountry",
        ConditionExpression='attribute_not_exists(deletedAt)' # Do not update if
        ExpressionAttributeValues={
            ':newCountry': "Canada"
        },
        ReturnValues="UPDATED_NEW"
    """
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=updateExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

def delete_item(table_name, key: Key):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key=key)
    return response

# 1MB limit
def query(table_name, keyConditionExpression, expressionAttributeValues):
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=keyConditionExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )

    data = response['Items']
    # LastEvaluatedKey indicates that there are more results
    while 'LastEvaluatedKey' in response:
        response = table.query(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.update(response['Items'])
    
    return response
    """
    response = table.query(
        KeyConditionExpression=Key('id').eq(1)
        IndexName: 'GSI1'
        ScanIndexForward=False # true = ascending, false = descending
    )
    for i in response['Items']:
        print(i['title'], ":", i['description'])
    """

# 1MB limit
def scan(table_name):
    table = dynamodb.Table(table_name)
    response = table.scan()
    return response
    
    """
    response = table.scan(FilterExpression=Attr('country').eq('US') & Attr('city').eq('NYC'))
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    return data
    """

# 16MB and 100 items limit
def batch_get_items():
    response = dynamodb.batch_get_item(
        RequestItems={
            'my-table': {
                'Keys': [
                    {
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                ],
                'ConsistentRead': True
            }
        },
        ReturnConsumedCapacity='TOTAL'
    )
    return response