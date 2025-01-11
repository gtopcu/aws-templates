
import boto3
from boto3.dynamodb.conditions import Key, Attr

import time

REGION = "us-east-1"
ACCESS_KEY_ID = "xxx"
ACCESS_KEY_SECRET = "yyy"

# ddb_client = boto3.client("dynamodb")
ddb = boto3.resource("dynamodb",
    endpoint_url="http://localhost:8000",
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_KEY_SECRET,
)

# table = ddb.create_table(
#     TableName="load-test",
#     KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
#     AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
#     # ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
#     BillingMode="PAY_PER_REQUEST",
# )

table = ddb.Table("load-test")

# delete table
# table.delete()

# response = table.put_item(Item={"id": "1", "name": "Gokhan Topcu", "age": 40, "address": "my address"})

start = time.time()

# ------------------------------------------------------------------------------------------------------------------------------
ITEM_COUNT = 25

# 117s
# for i in range(ITEM_COUNT):
#     response = table.put_item(Item={"id": str(i), "name": "Gokhan Topcu", "age": 40, "address": "my address"})

# ------------------------------------------------------------------------------------------------------------------------------

# 47s
# with table.batch_writer() as batch:
#     for i in range(ITEM_COUNT):
#         batch.put_item(Item={"id": str(i), "name": "Gokhan Topcu", "age": 40, "address": "my address"})
#         # batch.delete_item(Key={'PK': str(i)})

# # "UnprocessedItems": {},
response = ddb.batch_write_item(
    RequestItems={
        "load-test": [
            {"PutRequest": {"Item": {"id": str(i), "name": "Gokhan Topcu", "age": 40, "address": "my address"} }}
            for i in range(1025, 1050, 1)
        ]
    }
)
#print(response)
print("Unprocessed:", response["UnprocessedItems"])


# ------------------------------------------------------------------------------------------------------------------------------
# SCAN/QUERY

# 'Count': 23360, 'ScannedCount': 23360, 'LastEvaluatedKey': {'PK': '39001'}
kwargs = { 
            #"KeyConditionExpression"    : Key("id").eq("1"),
            #"FilterExpression"         : Attr("name").begins_with("z"),
            #"FilterExpression"         : Attr("age").gt(40),
            #"FilterExpression"         : "age > :val",
            #"ExpressionAttributeValues" : {":val": "40"},
        }

response = table.scan(**kwargs,
    # KeyConditionExpression=Key("id").eq("1")
    # KeyConditionExpression=Key("id").eq("1") & Key("name").begins_with("G"),
    # FilterExpression=Key("name").begins_with("G"),
    # FilterExpression=Attr("age").gt(40),
    # FilterExpression="age > :val",
    # ExpressionAttributeValues={":val": "40"},
    # Limit=100,
    # ProjectionExpression="PK, age",
    # ConsistentRead=True
) 
# print(response)
data = response['Items']
while "LastEvaluatedKey" in response:
    response = table.scan(**kwargs, ExclusiveStartKey=response["LastEvaluatedKey"])
    data.extend(response['Items'])
# print(response)
print(len(data))

# ------------------------------------------------------------------------------------------------------------------------------

# table.query(Limit=100)

print("Time taken: " + f"{time.time() - start:.2f}")



