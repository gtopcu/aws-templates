
# https://dynobase.dev/run-dynamodb-locally/

# docker run -p 8000:8000 amazon/dynamodb-local

# For NoSQL Workbench Local Dynamo - requires JRE:
# brew install openjdk
# $(brew --prefix openjdk)/bin/java --version
# file $(brew --prefix openjdk)/bin/java  
# echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> /Users/mac/.zshrc
# sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

# python -m venv .venv
# source .venv/bin/activate
# pip install -U -r requirements.txt
# /Users/mac/GoogleDrive/VSCode/aws-templates/Serverless/utils_aws/utils_dynamodb/dynamodb-local/.venv

import boto3
from boto3.session import Session
from botocore.exceptions import ClientError

from boto3.dynamodb.table import TableResource #, BatchWriter, BatchReader
import boto3.dynamodb.types
import boto3.dynamodb.transform
import boto3.dynamodb.conditions
from boto3.dynamodb.conditions import Key, Attr

REGION = "us-east-1"

ddb_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name=REGION)
ddb_resource = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name=REGION)

table = ddb_resource.Table('table-1')
# table_resource: TableResource = table.TableResource()

# print(list(ddb.tables.all()))

# # Limit
# table.query(Limit=37)


# response = table.put_item(
#     Item={
#         'id': 1,
#         'title': 'my-document-title',
#         'content': 'some-content',
#     }
# )

# try:
#     table.put_item(Item=item)
#     return {
#         'statusCode': 201,
#         'body': event
#     }
# except ClientError as err:
#     # print(str(err))
#     print("Error Code: " + f"{err.response['Error']['Code']}")
#     print("Error Message: " + f"{err.response['Error']['Message']}")


    # with table.batch_writer() as batch:
    #     for _ in range(1000000):
    #         batch.put_item(Item={'HashKey': '...',
    #                              'Otherstuff': '...'})
    #     # You can also delete_items in a batch.
    #     batch.delete_item(Key={'HashKey': 'SomeHashKey'})
