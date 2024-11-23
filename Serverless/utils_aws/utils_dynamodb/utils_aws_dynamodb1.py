
# Code whisperer: Option + C
# https://www.youtube.com/watch?v=twxM7WTfhGs
# https://dynobase.dev/dynamodb-python-with-boto3/
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/service-resource/tables.html 

import boto3
from boto3.dynamodb.conditions import Key, Attr
# from boto3.dynamodb.types import STRING
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

# import botocore
# from botocore.exceptions import ClientError

ddb = boto3.resource('dynamodb')
# table.item_count
# table.table_size_bytes
# table.creation_date_time 

# https://dynobase.dev/dynamodb-python-with-boto3/#get-item

# Use port 8000 for DynamoDB Local and 4569 for DynamoDB from LocalStack
# ddb = boto3.resource('dynamodb',
#                          region_name=region,
#                          endpoint_url='http://localhost:8000')

# ddb = boto3.client('dynamodb',
#                       aws_access_key_id='yyyy',
#                       aws_secret_access_key='xxxx',
#                       region_name='us-east-1')

# # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html
# from botocore.config import Config
# my_config = Config(
#     connect_timeout = 5,
#     read_timeout = 10,
#     tcp_keepalive = True
#     retries = {
#      'mode': 'standard',
#      'total_max_attempts': 3
#    }
#    max_pool_connections = 20, # default 10 for Session
# )
# ddb = boto3.resource('dynamodb', config=my_config)

# https://www.dynamodbguide.com/expression-basics
# attribute_exists(): Check for existence of an attribute
# attribute_not_exists(): Check for non-existence of an attribute
# attribute_type(): Check if an attribute is of a certain type
# begins_with(): Check if an attribute begins with a particular substring
# contains(): Check if a String attribute contains a particular substring or a Set attribute contains a particular element
# size(): Returns a number indicating the size of an attribute

@staticmethod
def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = TypeDeserializer()
    return {
        k: deserializer.deserialize(v) 
        for k, v in dynamo_object.items()
    }  

@staticmethod
def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {
        k: serializer.serialize(v)
        for k, v in python_object.items()
    }

def get_item(table_name, key):
    """ Key={"id": id} """
    table = ddb.Table(table_name)
    response = table.get_item(Key=key) 
    if "Item" not in response:
        return None
    return response["Item"]

def put_item(table_name, item):
    """
        Item={
            'id': 1,
            'title': 'my-document-title',
            'content': 'some-content',
        }
    """
    table = ddb.Table(table_name)
    return table.put_item(Item=item)

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
    table = ddb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=updateExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response

# def update_item_counter():
#     ddb = boto3.resource('dynamodb')
#     table = ddb.Table(os.environ['DDB_TABLE_NAME'])
#     table.update_item(
#         Key={'path': 'get'},
#         UpdateExpression='ADD hits :incr',
#         ExpressionAttributeValues={':incr': 1}
#     )

def delete_item(table_name, key: Key):
    table = ddb.Table(table_name)
    response = table.delete_item(Key=key)
    return response

# 1MB limit
def query(table_name, keyConditionExpression, expressionAttributeValues):
    table = ddb.Table(table_name)
    response = table.query(
        KeyConditionExpression=keyConditionExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )

    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.query(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.update(response['Items'])
    
    return response

# 1MB limit
def scan(table_name):
    table = ddb.Table(table_name)
    response = table.scan()
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data

# 16MB and 100 items limit
# can read or write items from one or more tables
# Partial Errors: UnprocessedKeys
def batch_get_items():
    response = ddb.batch_get_item(
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

# 16MB and 25 items limit
# Partial Errors: UnprocessedItems
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html#batch-writing
def batch_write_items(table_name):
    table = ddb.Table(table_name)

    #overwrite_by_pkeys=['partition_key', 'sort_key']
    with table.batch_writer() as batch:
        for i in range(50):
            batch.put_item(
                Item={
                    'account_type': 'anonymous',
                    'username': 'user' + str(i),
                    'first_name': 'unknown',
                    'last_name': 'unknown'
                }
            )


    """
    response = client.query(
        TableName='YourTableName',
        KeyConditionExpression='pk = :pk_val AND begins_with(sk, :sk_val)',
        FilterExpression='#name = :name_val',
        ExpressionAttributeValues={
            ':pk_val': {'S': 'id#1'},
            ':sk_val': {'S': 'cart#'},
            ':name_val': {'S': 'SomeName'},
        },
        ExpressionAttributeNames={
            '#name': 'name',
        }
    )
    Same using Resource:
    response = table.query(
        KeyConditionExpression=Key('pk').eq('id#1') & Key('sk').begins_with('cart#'),
        FilterExpression=Attr('name').eq('SomeName'),
        'Limit': 100
    )

    response = table.query(
        KeyConditionExpression=Key('id').eq(1)
        IndexName: 'GSI1'
        ScanIndexForward=False # true = ascending, false = descending
    )
    for i in response['Items']:
        print(i['title'], ":", i['description'])

    response = table.scan(FilterExpression=Attr('country').eq('US') & Attr('city').eq('NYC'))
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data

    response = table.scan(
        FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
    )
    items = response['Items']
    print(items)

    # Nested attribute
    response = table.scan(
        FilterExpression=Attr('address.state').eq('CA')
    )


    """