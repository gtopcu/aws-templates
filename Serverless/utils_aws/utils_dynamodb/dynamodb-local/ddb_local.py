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
# /Users/mac/GoogleDrive/VSCode/aws-templates/Serverless/utils_aws/utils_dynamodb/dynamodb-local/.venv

import json

import boto3
import boto3.dynamodb.conditions
import boto3.dynamodb.transform
import boto3.dynamodb.types
from boto3 import dynamodb
from boto3.dynamodb.conditions import Attr, Key

# from boto3.dynamodb.table import TableResource, BatchWriter, BatchReader
# from boto3.session import Session
from botocore.exceptions import ClientError
from pydantic_models import Person

REGION = "us-east-1"
ACCESS_KEY_ID = "xxx"
ACCESS_KEY_SECRET = "yyy"

# ddb_client = boto3.client(
#     "dynamodb",
#     endpoint_url="http://localhost:8000",
#     region_name=REGION,
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=ACCESS_KEY_SECRET,
# )
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

# table.query(Limit=37)

response = table.put_item(
    Item={"ID": "1", "Name": "Gokhan Topcu", "Age": 40, "Address": "my address"}
)
# print(response)

# response = table.get_item(Key={"ID": "1"})
# if item := response.get('Item'):
#     print("Item: ", item)
# else:
#     print("Not found: ", my_id)
# record = response["Item"]
# print(record)
# print(type(record)) #dict
# print(record["ID"])
# print(record["Name"])
# print(record["Address"])
# print(json.dumps(record))
# person = Person(**record)
# print(person.model_dump_json())

person = Person(
    ID="2",
    Name="Goknur Topcu",
    Age=30,
    Address="my address2",
    Hobbies=["walking, swimming"],
)
response = table.put_item(Item=person.model_dump())

# try:
#     table.put_item(Item=item, ConditionExpression="attribute_not_exists(ID)")
#     successfulItems.append(item)
# except ClientError as err:
#     if(err.response['Error']['Code'] == "ConditionalCheckFailedException"):
#         print("Item already exists: ", item)
#         successfulItems.append(item)
#     else:
#         print("Error: " + str(err))

# response = table.update_item(
#     Key={
#         "ID": "2"
#     },
#     UpdateExpression="SET Age = :age",
#     ConditionExpression='attribute_not_exists(Age)' # Do not update if exists
#     ExpressionAttributeValues={
#         ":age": 31
#     },
#     ReturnValues="UPDATED_NEW"
# )
# print(response)

# Delete
# response = table.delete_item(Key={"ID": "1"})
# print(response)

# Scan - 1MB Limit
# response = table.scan()
# response = table.scan(ProjectionExpression="ID, Name, Age")
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
#     KeyConditionExpression=Key("ID").eq("2"),
#     # FilterExpression=Attr("Age").eq(30) & Attr("Address").begins_with("my") #& Attr("Hobbies").contains("walking"),
#     # FilterExpression=Attr("Age").between(30, 40) & Attr("Age").is_in([30, 31, 32]) & Attr("Age").exists()
#     # FilterExpression=Attr("Age").gt(30) & Attr("Age").lt(40) & Attr("Age").ne(31) & Attr("Age").gte(30) & Attr("Age").lte(40)
#     # IndexName="GSI1",
#     # Limit=10,
#     # ProjectionExpression="ID, Name, Age",
#     # ScanIndexForward=False # true = ascending, false = descending
# )
# data = response['Items']
# while "LastEvaluatedKey" in response:
#     response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
#     data.extend(response['Items'])
# print(data)


# Batch Write - 25 items / 16GB limit
# with table.batch_writer() as batch:
#     for i in range(1, 10):
#         batch.put_item(Item={"ID": str(i)})
# You can also delete_items in a batch.
# batch.delete_item(Key={'HashKey': 'SomeHashKey'})


# Batch Get - 100 items / 16GB limit
# response = ddb.batch_get_item(
#     RequestItems={"employee": {"Keys": [{"ID": "1"}], "ConsistentRead": True}},
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
#                 ProjectionExpression="ID",
#                 ExclusiveStartKey=scan["LastEvaluatedKey"],
#             )
#         else:
#             scan = table.scan(ProjectionExpression="ID")

#         for item in scan["Items"]:
#             batch.delete_item(Key={"ID": item["ID"]})


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

# Legacy - do not use
# def update_item_counter():
#     ddb = boto3.resource('dynamodb')
#     table = ddb.Table(os.environ['DDB_TABLE_NAME'])
#     table.update_item(
#         Key={'path': 'get'},
#         UpdateExpression='ADD hits :incr',
#         ExpressionAttributeValues={':incr': 1}
#     )