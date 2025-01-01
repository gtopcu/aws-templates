# https://dynobase.dev/run-dynamodb-locally/
# https://dynobase.dev/dynamodb-python-with-boto3/#dynamodb-local
# https://www.dynamodbguide.com/expression-basics
# https://www.youtube.com/watch?v=cyge2Lx4Jvw

# docker run -p 8000:8000 amazon/dynamodb-local

# For NoSQL Workbench Local Dynamo - requires JRE:
# https://stackoverflow.com/questions/64788005/java-jdk-for-the-apple-silicon-chips
# brew install openjdk
# $(brew --prefix openjdk)/bin/java --version
# file $(brew --prefix openjdk)/bin/java
# echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> /Users/mac/.zshrc
# sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

# python -m venv .venv
# source .venv/bin/activate
# pip install -U -r requirements.txt

# pip install simplejson
# import simplejson as json
import json

import boto3
import boto3.dynamodb.conditions
import boto3.dynamodb.transform
import boto3.dynamodb.types
from boto3 import dynamodb
from boto3.dynamodb.conditions import Key, Attr

# from boto3.dynamodb.table import TableResource, BatchWriter, BatchReader
# from boto3.session import Session
from botocore.exceptions import ClientError
from .schemas import Person

# https://github.com/boto/boto3/issues/665#issuecomment-340260257
from decimal import Decimal

REGION = "us-east-1"
ACCESS_KEY_ID = "xxx"
ACCESS_KEY_SECRET = "yyy"

# ddb_client = boto3.client(
#     "dynamodb",
#     endpoint_url="http://localhost:8000",
#     region_name=REGION,
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=ACCESS_KEY_SECRET,
# )
ddb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_KEY_SECRET,
)

# for table in ddb.tables.all():
#     # print(table.name)

table: dynamodb.table = ddb.Table("employee")
print(table)
print("Table status:", table.table_status)

# table_resource: TableResource = table.TableResource()
# ddb.meta.client.describe_table(TableName="employee")

# ddb.meta.client.transact_write_items()
# ddb.meta.client.transact_get_items()
# dynamodb.transact_write_items()
# dynamodb.transact_get_items()

# ddb_client.get_waiter(TableName="employee").wait(TableName="employee", WaiterConfig={"Delay": 1, "MaxAttempts": 10}
# ddb_client.get_paginator(TableName="employee").paginate(TableName="employee", PaginationConfig={"MaxItems": 10, "PageSize": 10})
# ddb_client.can_paginate()
# ddb_client.meta.partition
# ddb_client.meta.region_name
# ddb_client.meta.service_model
# ddb_client.meta.events
# ddb_client.meta.config
# ddb_client.meta.endpoint_url

# table.query(Limit=37)

response = table.put_item(Item={"id": "1", "name": "Gokhan Topcu", "age": 40, "address": "my address"})
# print(response)

response = table.get_item(Key={"id": "1", "name": "Gokhan Topcu"})
if record := response.get("Item"):
    print("Record: ", record)
else:
    print("Not found")
#     return {
#         "statusCode": 404,
#         "body": { "result": "Not found" },
#    }
# record = response["Item"]
# print(record)
# print(type(record)) #dict
# print(record["id"])
# print(record["name"])
# print(record["address"])
# record = json.loads(record)
# record = json.loads(record, parse_float=Decimal)
# print(json.dumps(record))
person = Person(**record)
# print(person.model_dump())
# person.model_dump(mode="json") # or "python"
print(person.model_dump_json(exclude_none=True, exclude_defaults=True, exclude_unset=True))
# record:dict = json.loads(person.model_dump_json(exclude_none=True))
# print(record)

person = Person(
    id="2",
    name="Goknur Topcu",
    age=30,
    address="my address2",
    money=30.12,
    hobbies=["walking, swimming"],
)
response = table.put_item(Item=person.model_dump(exclude_none=True, exclude_defaults=True, exclude_unset=True))
# print(person.model_dump())
print(person.model_dump_json(exclude_none=True, exclude_defaults=True, exclude_unset=True))
#     return {
#         "statusCode": 201,
#         "body": { "result": "Created successfully" },
#    }
#      
# try:
#     table.put_item(Item=item, ConditionExpression="attribute_not_exists(id)")
#     successfulItems.append(item)
# except ClientError as err:
#     if(err.response['Error']['Code'] == "ConditionalCheckFailedException"):
#         print("Item already exists: ", item)
#         successfulItems.append(item)
#     else:
#         print("Error: " + str(err))

# response = table.update_item(
#     Key={
#         "id": "2"
#     },
#     UpdateExpression="SET age = :age", # SET-ADD-DELETE
#     ConditionExpression='attribute_not_exists(age)' # Do not update if exists
#     ExpressionAttributeValues={
#         ":age": 31
#     },
#     ReturnValues="UPDATED_NEW"
# )
# print(response)

# Delete
# response = table.delete_item(Key={"id": "1"})
# print(response)

# Scan - 1MB Limit
# response = table.scan()
# response = table.scan(
#     FilterExpression=Key("name").begins_with("G"),
#     ProjectionExpression="id, age"
# )
# for item in response["Items"]:
#     print(item)

# response = table.scan()
# # print(response)
# data = response['Items']
# while "LastEvaluatedKey" in response:
#     response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
#     data.extend(response['Items'])
# for record in data:
#     print(record)
#     # person = Person(**record)
#     # print(person.model_dump(exclude_none=True))


# Query - 1MB Limit
# response = table.query(
#     KeyConditionExpression=Key("id").eq("1"),
#     # FilterExpression=Attr("age").eq(30) & Attr("address").begins_with("my") #& Attr("hobbies").contains("walking"),
#     # FilterExpression=Attr("age").between(30, 40) & Attr("age").is_in([30, 31, 32]) & Attr("age").exists()
#     # FilterExpression=Attr("age").gt(30) & Attr("Age").lt(40) & Attr("age").ne(31) & Attr("age").gte(30) & Attr("age").lte(40)
#     # IndexName="GSI1",
#     # Limit=10,
#     # ProjectionExpression="id, name, age",
#     # ScanIndexForward=False # true = ascending, false = descending
# )
# data = response['Items']
# while "LastEvaluatedKey" in response:
#     response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
#     data.extend(response['Items'])
# print(data)


# Batch Write - 25 items / 16GB limit
# BatchWriter: Parallel, non-atomic writes -> handle partial failures!
# with table.batch_writer() as batch:
#     for i in range(1, 10):
#         batch.put_item(Item={"id": str(i)})
#         You can also delete_items in a batch.
#         batch.delete_item(Key={'id': str(i)})


# Batch Get - 100 items / 16GB limit
# response = ddb.batch_get_item(
#     RequestItems={"employee": {"Keys": [{"id": "1"}], "ConsistentRead": True}},
#     ReturnConsumedCapacity="TOTAL",
# )
# # print(response)
# if response["Responses"]:
#     for item in response["Responses"]["employee"]:
#         print(item)

# Delete All
# with table.batch_writer() as batch:
#     scan = None
#     while scan is None or "LastEvaluatedKey" in scan:
#         if scan is not None and "LastEvaluatedKey" in scan:
#             scan = table.scan(
#                 ProjectionExpression="id",
#                 ExclusiveStartKey=scan["LastEvaluatedKey"],
#             )
#         else:
#             scan = table.scan(ProjectionExpression="id")

#         for item in scan["Items"]:
#             batch.delete_item(Key={"id": item["id"]})


# Increment Attribute
# response = table.update_item(
#     Key={
#         'id': '777'
#     },
#     UpdateExpression='SET score.#s = score.#s + :val",
#     ExpressionAttributeNames={
#         "#s": "goals"
#     },
#     ExpressionAttributeValues={
#         ':val': decimal.Decimal(1)
#     },
#     ReturnValues="UPDATED_NEW"

# def update_item_counter():
#     table.update_item(
#         Key={'ID': 1000},
#         UpdateExpression='ADD hits :incr',
#         ExpressionAttributeValues={':incr': 1}
#     )
#

# Transaction write
def write_to_dynamodb_transaction():
    items = [
        {
            'Put': {
                'TableName': 'MyTable',
                'Item': {
                    'ID': {'S': '1'},
                    'Name': {'S': 'Item 1'},
                    'Price': {'N': '10'},
                }
            }
        }
    ]
    dynamodb = boto3.client('dynamodb', region_name='us-west-2')
    try:
        response = dynamodb.transact_write_items(TransactItems=items)
        # response = ddb.meta.client.transact_write_items(TransactItems=items)
        print("Transaction successful:", response)

    except ClientError as e:
        print(f"Error occurred: {e}")


# def write_to_dynamodb_transaction2(order_id: str, customer_id: str):
#     dynamodb = boto3.resource('dynamodb')
    
#     # Reference to tables
#     orders_table = dynamodb.Table('Orders')
#     customers_table = dynamodb.Table('Customers')
#     inventory_table = dynamodb.Table('Inventory')

#     try:
#         # Create transaction
#         dynamodb.meta.client.transact_write_items(
#             TransactItems=[
#                 {
#                     'Put': {
#                         'TableName': 'Orders',
#                         'Item': {
#                             'order_id': order_id,
#                             'customer_id': customer_id,
#                             'status': 'PENDING'
#                         },
#                         'ConditionExpression': 'attribute_not_exists(order_id)'
#                     }
#                 },
#                 {
#                     'Update': {
#                         'TableName': 'Customers',
#                         'Key': {
#                             'customer_id': customer_id
#                         },
#                         'UpdateExpression': 'SET order_count = order_count + :inc',
#                         'ExpressionAttributeValues': {
#                             ':inc': 1
#                         }
#                     }
#                 },
#                 {
#                     'Update': {
#                         'TableName': 'Inventory',
#                         'Key': {
#                             'product_id': 'PROD1'
#                         },
#                         'UpdateExpression': 'SET stock = stock - :dec',
#                         'ConditionExpression': 'stock >= :dec',
#                         'ExpressionAttributeValues': {
#                             ':dec': 1
#                         }
#                     }
#                 }
#             ]
#         )
#         return True
#     except ClientError as e:
#         print(f"Transaction failed: {e}")
#         return False
#
#