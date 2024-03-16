import json
import boto3
import botocore
from botocore.exceptions import 
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("table-1")

"""
docker pull amazon/dynamodb-local
docker run -p 8000:8000 amazon/dynamodb-local
http://localhost:8000

# For a Boto3 client.
ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
response = ddb.list_tables()
print(response)

# For a Boto3 service resource
ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
print(list(ddb.tables.all()))

"""
# inputItems = json.loads("""
# [
#   {
#     "id": "010",
#     "age": 43,
#     "cars": [
#       "audi",
#       "bentley",
#       "bmw",
#       "skoda"
#     ]
#   },
#   {
#     "id": "011",
#     "age": 11,
#     "cars": [
#       "fiat",
#       "volvo"
#     ]
#   }
# ]
# """
# )
# for item in inputItems:
#     print(item["id"])

def lambda_handler(event, context):
    
    #print(event)
    
    # for key, value in sorted(botocore.exceptions.__dict__.items()):
    #     if isinstance(value, type):
    #         print(key)
    
    # for k, v in event.items():
    #     print(k, "-", v)
    #     item = {k: v}
    
    successfulItems = []
    for item in event:
        try: 
            table.put_item(Item=item, ConditionExpression="attribute_not_exists(id)")
            successfulItems.append(item)
        except botocore.exceptions.ClientError as error:
            if(error.response['Error']['Code'] == "ConditionalCheckFailedException"):
                print("Item already exists: ", item)
                successfulItems.append(item)
            else:
                print("Error: ", error)
    return {
         'statusCode': 201,
         'body': successfulItems
    }
        
    # try:
    #     item = event
    #     table.put_item(Item=item)
    #     # table.put_item(
    #     #                 Item={'id': v},
    #     #                 ConditionExpression="attribute_not_exists(id)"
    #     #             )
    #     print("success!")
        
    # except botocore.exceptions.ClientError as error:
    #     print("error!")
    #     print(error.response['Error']['Code'])
    #     print(error.response['Error']['Message'])
    #     print(error.response['ResponseMetadata'])
    
    # my_id = '001'
    # response = table.get_item(
    #   Key={
    #           'id': my_id
    #       },
    #   ConsistentRead=True|False,
    #   ProjectionExpression='string'
    # )
    # print("Response: ", response)
    # if response.get('Item') is not None:
    #     item = response['Item']
    #     print("Item: ", item)
    # else:
    #     print("Not found: ", my_id)
    
    # if item := response.get('Item'): #walrus operator
    #    print("Item: ", item)
    # else:
    #     print("Not found!")

    # response = table.query(
    #     KeyConditionExpression=Key('id').eq('001')
    # )
    # #print(response)
    # data = response['Items']
    # while 'LastEvaluatedKey' in response:
    #      response = table.query(ExclusiveStartKey=response['LastEvaluatedKey'])
    #      data.extend(response['Items'])
    # print(data)
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
