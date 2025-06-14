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
from datetime import datetime, timezone
# https://github.com/boto/boto3/issues/665#issuecomment-340260257
from decimal import Decimal

import boto3
import boto3.dynamodb.conditions
import boto3.dynamodb.transform
import boto3.dynamodb.types
from boto3 import dynamodb
from boto3.dynamodb.conditions import Attr, Key
# from boto3.dynamodb.table import TableResource, BatchWriter, BatchReader
# from boto3.session import Session
from botocore.exceptions import ClientError

from .schemas import Person

REGION = "us-east-1"
ACCESS_KEY_ID = "xxx"
ACCESS_KEY_SECRET = "yyy"

# import botocore.session
# session = botocore.session.get_session()
# client = session.create_client('dynamodb', region_name='us-east-1') 
# session.get_credentials()

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
ddb_client = ddb.meta.client

# for table in ddb.tables.all():
#     # print(table.name)

table: dynamodb.table = ddb.Table("employee")

# ddb                                     # dynamodb.ServiceResource()
# table                                   # dynamodb.Table(name='load-test')
# table.name                              # load-test
# table.table_status                      # ACTIVE
# table.creation_date_time                # Sun, 12 Jan 2025 09:43:35 GMT
# ddb.meta                                # ResourceMeta('dynamodb', identifiers=[])
# ddb.meta.service_name                   # dynamodb
# client = ddb.meta.client                # Get a low-level client from a resource instance
# client.list_tables()                    # {'TableNames': ['employee', 'load-test'], ... }
# client.meta.endpoint_url                # http://localhost:8000
# client.meta.service_model               # ServiceModel(dynamodb)
# client.meta.region_name                 # us-east-1
# client.meta.partition                   # aws
# client.meta.events                      # Events
# client.meta.config                      # Config
# client.meta.config.user_agent()         # Boto3/1.24.12 Python/3.9.12 Linux/5.15.0-46-generic Botocore/1.29.12
# client.meta.config.connect_timeout      # 60
# client.meta.config.read_timeout         # 60
# client.meta.config.max_pool_connections # 10
# client.meta.config.retries              # {'max_attempts': 3}
# client.can_paginate("query")              # True

# table = ddb_client.create_table(
#     TableName="table-1",
#     KeySchema=[{"AttributeName": "PK","KeyType": "HASH"},{"AttributeName": "SK", "KeyType": "RANGE"}],
#     AttributeDefinitions=[{"AttributeName": "PK", "AttributeType": "S"}, {"AttributeName": "SK", "AttributeType": "S"}],
#     # ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
#     BillingMode="PAY_PER_REQUEST",
# )
# waiter = client.get_waiter('table_exists')
# waiter.wait(TableName=table.name, WaiterConfig={"Delay": 3, "MaxAttempts": 10})

# delete table
# table.delete()

# paginator = client.get_paginator("scan") # <botocore.client.DynamoDB.Paginator.Scan>

# Add timestamp to the item
# timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
# body = {
#     "PK": "1",
#     "name": "Gokhan Topcu",
# }
# item = {
#     **body,
#     'timestamp': timestamp
# }
# table.put_item(Item=item)

response = table.put_item(Item={"PK": "1", "name": "Gokhan Topcu", "age": 40, "address": "my address"})
# print(response)

response = table.get_item(Key={"PK": "1", "name": "Gokhan Topcu"})
# if 'Item' not in response:
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
# print(record["PK"])
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
    PK="2",
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
# # PK:2KB, SK:1KB, Max:400KB/item -> Apply size limit!     
# try:
#     table.put_item(Item=item, ConditionExpression="attribute_not_exists(PK)")
#     successfulItems.append(item)
# except ClientError as err:
#     if(err.response['Error']['Code'] == "ConditionalCheckFailedException"):
#         print("Item already exists: ", item)
#         successfulItems.append(item)
#     else:
#         print("Error: " + str(err))

# response = table.update_item(
#     Key={
#         "PK": "2"
#     },
#     UpdateExpression="SET age = :age", # SET-ADD-DELETE #"SET status = :status REMOVE address"
#     ConditionExpression='attribute_not_exists(age)' # Do not update if exists
#     ExpressionAttributeValues={
#         ":age": 31
#     },
#     ReturnValues="UPDATED_NEW"
# )
# print(response)

# Idempotency for PutItem/UpdateItem:
# Use condition expressions for idempotency -> set 'ReturnValuesOnConditionCheckFailure' to 'ALL_OLD'  
# Use the returned 'error' and 'error.Item' to run any additional logic and choose the appropriate error message
# https://www.serverlessguru.com/blog/dynamodb-common-mistakes-and-how-to-fix-them
# response = table.update_item(
#     Key={
#         "PK": "2"
#     },
#     UpdateExpression="SET age = :age", # SET-ADD-DELETE
#     ConditionExpression="attribute_exists(#pk) OR (attribute_not_exists(#pk) AND #age <> :age)",
#     ExpressionAttributeNames={
#         "#pk": 'PK',
#         "#age": 'age'
#     },
#     ExpressionAttributeValues={
#         ":age": 31
#     },
#     ReturnValues="UPDATED_NEW",
#     ReturnValuesOnConditionCheckFailure="ALL_OLD"
# )
# response.error
# response.error.Item
# print(response)

# Delete
# response = table.delete_item(Key={"PK": "1"})
# print(response)

# ------------------------------------------------------------------------------------------------------------------------------

# Scan - 1MB Limit -> dynamo can return empty response even though there are matching records!
# 'Count': 23360, 'ScannedCount': 23360, 'LastEvaluatedKey': {'PK': '39001'}

# response = table.scan()
# kwargs = { 
#            "FilterExpression" : "age > :val",
#            "ExpressionAttributeValues" : {":val": "40"},
# }
# kwargs = dict(
#     KeyConditionExpression=Key("age").eq(40),
#     FilterExpression=Attr("name").begins_with("G"),
#     ConsistentRead=True,
# )
# response = table.scan(**kwargs,
#     FilterExpression=Key("name").begins_with("G"),
#     ProjectionExpression="PK, age",
#     ProjectionExpression: "Colors[0], Scores[1]",         # list access by index
#     ProjectionExpression: "Address.City",                 # map access by . notation
#     ProjectionExpression: "Orders[0].Items[0].ProductId", # using both list & map access
#     ProjectionExpression: "#ord[0].#itm[0].#pid",         # using expression att. names
#     FilterExpression: "Colors[0] = :color",               # filtering lists
#     FilterExpression: "contains(Colors, :color)",         # filtering list with "contains"
#     ExpressionAttributeValues: {":color": "Red"}
#     FilterExpression: "contains(Scores, :score)",         # filtering a number set
#     ExpressionAttributeValues: { ":score": 90 }
#     FilterExpression: "size(Colors) = :size",             # checking list/set size
#     ExpressionAttributeValues: {":size": 3}
#     Limit=10
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


# Query - 1MB Limit -> dynamo can return empty response even though there are matching records!
# kwargs = dict(
#     KeyConditionExpression=Key("age").eq(40),
#     FilterExpression=Attr("name").begins_with("G"),
#     ConsistentRead=True,
# )
# response = table.query(
#    IndexName="GSI1",
#    KeyConditionExpression=Key("PK").eq("1") & Key("name").begins_with("G") # between(1, 3) gt(1) gte(1) lt(1) lte(1)
#     # FilterExpression=Attr("age").eq(30) & Attr("address").begins_with("my") #& Attr("hobbies").contains("walking"),
#     # FilterExpression=Attr("age").between(30, 40) & Attr("age").is_in([30, 31, 32]) & Attr("age").exists()
#     # FilterExpression=Attr("age").gt(30) & Attr("Age").lt(40) & Attr("age").ne(31) & Attr("age").gte(30) & Attr("age").lte(40)
#     # Limit=10,
#     # ProjectionExpression="PK, name, age",
#     # Select='ALL_ATTRIBUTES',
#     # ScanIndexForward=False # true = ascending, false = descending,
#     # ConsistentRead=True,
# )
# data = response['Items']
# while "LastEvaluatedKey" in response:
#     response = table.query(ExclusiveStartKey=response["LastEvaluatedKey"])
#     data.extend(response['Items'])
# print(data)

# ------------------------------------------------------------------------------------------------------------------------------

# Batch Write/Delete - 25 items / 16GB limit
# BatchWriter: Parallel, non-atomic writes
# Records that are not processed will be returned in 'UnprocessedItems' attribute in the response - apply retry!
# "UnprocessedItems": {},
# response = ddb.batch_write_item(
#     RequestItems={
#         table.name: [
#             {"PutRequest": {"Item": {"PK": str(i), "name": "Gokhan Topcu", "age": 40, "address": "my address"}}}
#             for i in range(ITEM_COUNT)
#         ]
#     }
# )
# print(response)
# print(response["UnprocessedItems"])

# with table.batch_writer() as batch:
#     for i in range(1, 10):
#         batch.put_item(Item={"PK": str(i)})
#         batch.delete_item(Key={'PK': str(i)})


# Batch Get - 100 items / 16GB limit (from same/different tables)
# Records that are not processed will be returned in 'UnprocessedItems' attribute in the response - apply retry!
# "UnprocessedItems": {},
# key_list = [ {"PK": "1"}, {"PK": "2"} ]
# response = ddb.batch_get_item(
#     RequestItems={table.name: {"Keys": key_list}},
#     # ConsistentRead=True,
#     ReturnConsumedCapacity="TOTAL",
# )
# print(response)
# print(response["UnprocessedItems"])
# if response["Responses"]:
#     for item in response["Responses"][table.name]:
#         print(item)

# Delete All
# with table.batch_writer() as batch:
#     scan = None
#     while scan is None or "LastEvaluatedKey" in scan:
#         if scan is not None and "LastEvaluatedKey" in scan:
#             scan = table.scan(
#                 ProjectionExpression="PK",
#                 ExclusiveStartKey=scan["LastEvaluatedKey"],
#             )
#         else:
#             scan = table.scan(ProjectionExpression="PK")

#         for item in scan["Items"]:
#             batch.delete_item(Key={"PK": item["PK"]})

# ------------------------------------------------------------------------------------------------------------------------------

# Increment Attribute
# response = table.update_item(
#     Key={
#         'PK': '777'
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
#         Key={'PK': 1000},
#         UpdateExpression='ADD hits :incr',
#         ExpressionAttributeValues={':incr': 1},
#         # ReturnValues="UPDATED_NEW",
#     )
#

# ------------------------------------------------------------------------------------------------------------------------------

# client.transact_write_items()
# client.transact_get_items()
# ddb.transact_write_items()
# ddb.transact_get_items()

# Transaction write
# def write_to_dynamodb_transaction():
#     items = [
#         {
#             'Put': {
#                 'TableName': 'MyTable',
#                 'Item': {
#                     'PK': {'S': '1'},
#                     'Name': {'S': 'Item 1'},
#                     'Price': {'N': '10'},
#                 }
#             }
#         }
#     ]
#     dynamodb = boto3.client('dynamodb', region_name='us-west-2')
#     try:
#         response = dynamodb.transact_write_items(TransactItems=items)
#         # response = ddb.meta.client.transact_write_items(TransactItems=items)
#         print("Transaction successful:", response)

#     except ClientError as e:
#         print(f"Error occurred: {e}")


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
# ------------------------------------------------------------------------------------------------------------------------------

# Run PartiQL:
# input = { "Statement": "select * from load-test" }
# response = dynamodb_client.execute_statement(**input)

# ------------------------------------------------------------------------------------------------------------------------------
# PAGINATION
# client = ddb.meta.client

# - Paginators automatically handle the LastEvaluatedKey logic
# - They're more efficient than manual pagination
# - Use appropriate page sizes to balance memory usage and performance
# - Consider using parallel scan for very large tables
# - Always handle potential errors and implement retries when necessary
# - Monitor your throughput consumption when using pagination

# 1 - Scan with no arguments
# response_iterator = paginator.paginate(TableName=table.name, PaginationConfig={"MaxItems": 8, "PageSize": 2})
# for page in response_iterator:
#     print("**************************************************************")
#     print(page["Items"])

# 2 - Scan/Query with arguments.
# paginator = client.get_paginator("scan")    # <botocore.client.DynamoDB.Paginator.Scan>
# paginator = client.get_paginator("query") # <botocore.client.DynamoDB.Paginator.Query>
# kwargs = {
#     #"KeyConditionExpression": "id = :id",
#     #"ExpressionAttributeValues": { ":id": "123"},
# }
# kwargs = dict(
#     KeyConditionExpression=Key("age").eq(40),
#     FilterExpression=Attr("name").begins_with("G"),
#     ConsistentRead=True,
# )
# response_iterator = paginator.paginate(
#     TableName=table.name,
#     **kwargs,
#     PaginationConfig={
#         "PageSize": 2,  # Items per page
#         "MaxItems": 10  # Total items to retrieve 
#     })
# for page in response_iterator:
#     print("**************************************************************")
#     print(page["Items"])

# ------------------------------------------------------------------------------------------------------------------------------
