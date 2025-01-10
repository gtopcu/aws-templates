# https://github.com/getmoto/moto
# https://blog.newmathdata.com/advanced-unit-testing-in-aws-a666e787aa99
# https://aws.amazon.com/blogs/devops/unit-testing-aws-lambda-with-python-and-mock-aws-services/

# pip install moto
# pip install "moto[ec2,s3,all]""

import os
import pytest
import boto3
from moto import mock_aws
from moto import mock_s3
from moto import mock_dynamodb

# @moto.mock_dynamodb
# @moto.mock_s3


@mock_dynamodb
def test_dynamodb():
    # Set up the mock DynamoDB environment
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table_name = "my-test-table"
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
    )

    # Perform operations as if interacting with real AWS
    table = dynamodb.Table(table_name)
    table.put_item(Item={"id": "1", "name": "John Doe"})

    # Assert that the item was inserted correctly
    response = table.get_item(Key={"id": "1"})
    assert response["Item"]["name"] == "John Doe"


@mock_s3
def test_s3_upload():
    # Set up the mock S3 environment
    s3 = boto3.client("s3", region_name="us-east-1")
    bucket_name = "my-test-bucket"
    s3.create_bucket(Bucket=bucket_name)

    # Perform operations as if interacting with real AWS
    s3.put_object(Bucket=bucket_name, Key="test_file.txt", Body=b"Hello Moto!")

    # Assert that the object exists in the bucket
    response = s3.get_object(Bucket=bucket_name, Key="test_file.txt")
    data = response["Body"].read()
    assert data == b"Hello Moto!"


# @mock_aws
# def test_my_model_save():
#     conn = boto3.resource("s3", region_name="us-east-1")
#     # We need to create the bucket since this is all in Moto's 'virtual' AWS account
#     conn.create_bucket(Bucket="mybucket")
#     model_instance = MyModel("steve", "is awesome")
#     model_instance.save()
#     body = conn.Object("mybucket", "steve").get()["Body"].read().decode("utf-8")
#     assert body == "is awesome"

# --------------------------------------------------------------------------------------------------

@pytest.fixture(scope="function")  # scope can be function, class, module, session
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture
def aws_client(aws_credentials):
    with mock_aws():
        # yield boto3.client("dynamodb", region_name="us-east-1")
        yield boto3.resource("dynamodb", region_name="us-east-1")


@pytest.fixture
def create_table(aws_client):
    boto3.client("dynamodb").create_table(
        TableName="table-1",
        BillingMode="PAY_PER_REQUEST",
        KeySchema=[{"AttributeName": "PK","KeyType": "HASH"},{"AttributeName": "SK", "KeyType": "RANGE"}],
        AttributeDefinitions=[{"AttributeName": "PK", "AttributeType": "S"}, {"AttributeName": "SK", "AttributeType": "S"}]
    )

def test_dynamo_put(create_table):
    dynamo_put("string", "data")
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("string")
    response = table.get_item(Key={"string": "data", "mykey": "foo"})
    print(response)
    assert response["Item"]["string"] == "data"


def test_dynamo_put(create_table):
    dynamo_put("string", "data")
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("string")
    response = table.get_item(Key={"string": "data", "mykey": "foo"})
    print(response)
    assert response["Item"]["string"] == "data"


def dynamo_put(table_name, value):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)
    return table.put_item(
        Item={"string": value, "mykey": "foo"},
    )

# def lambda_handler(event, context):
#     connection = connect_to_database()
#     result = query(connection)
#     dynamo_put("string", result)

#     return result
