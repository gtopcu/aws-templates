# Code whisperer: Option + C
import boto3

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

def getItem(tableName, primaryKeyName, primary_key, sortKeyName, sort_key):
    table = dynamodb.Table(tableName)
    response = table.get_item(Key={
        primaryKeyName: primary_key,
        sortKeyName: sort_key
    })
    return response

def batchGetItems():
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

def putItem(tableName, item):
    table = dynamodb.Table(tableName)
    table.put_item(Item=item)
    """
    response = table.put_item(
        Item={
            'id': 1,
            'title': 'my-document-title',
            'content': 'some-content',
        }
    )
    """

def updateItem(tableName, key, updateExpression, expressionAttributeValues):
    table = dynamodb.Table(tableName)
    response = table.update_item(
        Key=key,
        UpdateExpression=updateExpression,
        ExpressionAttributeValues=expressionAttributeValues
    )
    return response
    """
    response = table.update_item(
        Key={
            'id': '894673'
        },
        UpdateExpression='SET country = :newCountry",
        ConditionExpression='attribute_not_exists(deletedAt)' # Do not update if
        ExpressionAttributeValues={
            ':newCountry': "Canada"
        },
        ReturnValues="UPDATED_NEW"
    )
    """

def deleteItem(tableName, primaryKeyName, primary_key, sortKeyName, sort_key):
    table = dynamodb.Table(tableName)
    response = table.delete_item(Key={
        primaryKeyName: primary_key,
        sortKeyName: sort_key
    })
    return response

def query(tableName, keyConditionExpression, expressionAttributeValues):
    table = dynamodb.Table(tableName)
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

def scan(tableName):
    table = dynamodb.Table(tableName)
    response = table.scan()
    return response
    
    """
    1MB limit on scan

    response = table.scan(FilterExpression=Attr('country').eq('US') & Attr('city').eq('NYC'))
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    """