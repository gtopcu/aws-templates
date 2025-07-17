import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from itertools import islice

# Adds missing items from table1 on source_aws to table2 on target_aws accounts

# AWS credentials for source and target accounts
SOURCE_AWS = {
    'region_name': 'eu-west-2',
    'aws_access_key_id': 'ASIARK6QF65DXCPT25NN',
    'aws_secret_access_key': 'MwF0251daOQllCIRIQRcuxdIdDhpwTomG+sbDzxG',
    'aws_session_token': 'IQoJb3JpZ2luX2VjEFwaCWV1LXdlc3QtMiJHMEUCIQDtntlHcSxTUhS0KIw9o9Om8+lUTitnuv+GsGKQ+J44YgIgR19jswPPRhLJWwScqK2WLQEtPolmX4cbZRP4v8+SKYYq6gIIdRAAGgwwOTIyNDE1MjQ1NTEiDEpL0HiT+yu6pEiy2CrHAgJNEx5ABqKeL3i1axhB1Jo0i6I8hzkiKSSkXxgugNlM1UkrwC5WKG94KQwrSXLZhK6XN68g1F9mH9hQ5VMVRvtfM1+fgpZCTzRbJMj3WEYdjMzsNMYsjgkJpIuHC7tKRFrvaiN4rUFOJ2PPgpIDYBfqfSqjHkqWyImvXgsjtt2EW3dNusxmL8A9HewUl6rmzwWnfTUZ/fHl9YkAVrPYb5J42cewtzUOGmZb/ZelzCk++Oo11t30ksbOXFFVTrWY3vvZl9THIR4x6DxcAHv+Ki+wT4DhXf9ruJlhLwpyC+MyRAo78QmuYqenmSFon8fZZZzCZzfXXETpTbySMbqeVGv4VN1WRI/V9pqjaZTlkgDzEeXJqqWe6IqMjZ5OGD5BrPFCYzkt20uoeY8P+UbeJpgEAUKdYX2BbTt8r9miwyuSZQVlK0AxeDCmz+PDBjqnASEYk0oTiRmwWOTg1NqNyF7JxIWOvrjA19v7EiECz3xTcm3Lye5lHrJyUixXU9OzP9nqErkVCUuCzD+myPkuXaQNuIX7tWu+1xJzbShokcsywe9CqiCfMVQH1usKIHkHhHLNZZS59ZEJwtAq2ECkwla8TrtPzEY0VuzioRtqztbKbN1AMlhF5LOc3SzVGbVo/BK1u/6drEWUXqQdhFwQ5zquAFSSNEsG',
}

TARGET_AWS = {
    'region_name': 'eu-west-2',
    'aws_access_key_id': 'ASIARK6QF65DXCPT25NN',
    'aws_secret_access_key': 'MwF0251daOQllCIRIQRcuxdIdDhpwTomG+sbDzxG',
    'aws_session_token': 'IQoJb3JpZ2luX2VjEFwaCWV1LXdlc3QtMiJHMEUCIQDtntlHcSxTUhS0KIw9o9Om8+lUTitnuv+GsGKQ+J44YgIgR19jswPPRhLJWwScqK2WLQEtPolmX4cbZRP4v8+SKYYq6gIIdRAAGgwwOTIyNDE1MjQ1NTEiDEpL0HiT+yu6pEiy2CrHAgJNEx5ABqKeL3i1axhB1Jo0i6I8hzkiKSSkXxgugNlM1UkrwC5WKG94KQwrSXLZhK6XN68g1F9mH9hQ5VMVRvtfM1+fgpZCTzRbJMj3WEYdjMzsNMYsjgkJpIuHC7tKRFrvaiN4rUFOJ2PPgpIDYBfqfSqjHkqWyImvXgsjtt2EW3dNusxmL8A9HewUl6rmzwWnfTUZ/fHl9YkAVrPYb5J42cewtzUOGmZb/ZelzCk++Oo11t30ksbOXFFVTrWY3vvZl9THIR4x6DxcAHv+Ki+wT4DhXf9ruJlhLwpyC+MyRAo78QmuYqenmSFon8fZZZzCZzfXXETpTbySMbqeVGv4VN1WRI/V9pqjaZTlkgDzEeXJqqWe6IqMjZ5OGD5BrPFCYzkt20uoeY8P+UbeJpgEAUKdYX2BbTt8r9miwyuSZQVlK0AxeDCmz+PDBjqnASEYk0oTiRmwWOTg1NqNyF7JxIWOvrjA19v7EiECz3xTcm3Lye5lHrJyUixXU9OzP9nqErkVCUuCzD+myPkuXaQNuIX7tWu+1xJzbShokcsywe9CqiCfMVQH1usKIHkHhHLNZZS59ZEJwtAq2ECkwla8TrtPzEY0VuzioRtqztbKbN1AMlhF5LOc3SzVGbVo/BK1u/6drEWUXqQdhFwQ5zquAFSSNEsG',
}


# DynamoDB table names
# SOURCE_TABLE_NAME = 'COMPANY_DATA'
SOURCE_TABLE_NAME = 'GLOBAL_CONSTANTS_DATA'
TARGET_TABLE_NAME = 'test_table1'

# Keys used as primary and sort keys
PK_NAME = 'PK'
SK_NAME = 'SK'

# Batch size limits
BATCH_GET_SIZE = 100
BATCH_WRITE_SIZE = 25


def chunked(iterable, size):
    """Yield successive chunks from iterable."""
    it = iter(iterable)
    return iter(lambda: list(islice(it, size)), [])


def get_all_keys(ddb, table_name):
    """Scan entire table and return set of (PK, SK) tuples."""
    table = ddb.Table(table_name)
    keys = set()
    response = table.scan(ProjectionExpression=f"{PK_NAME}, {SK_NAME}")
    items = response.get('Items', [])
    keys.update((item[PK_NAME], item[SK_NAME]) for item in items)

    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=f"{PK_NAME}, {SK_NAME}",
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items = response.get('Items', [])
        keys.update((item[PK_NAME], item[SK_NAME]) for item in items)

    return keys


def get_items_by_keys(ddb, table_name, keys):
    """Fetch full items from source table by list of keys."""
    table = ddb.Table(table_name)
    items = []

    for key_chunk in chunked(keys, BATCH_GET_SIZE):
        request_keys = [{PK_NAME: pk, SK_NAME: sk} for pk, sk in key_chunk]
        response = ddb.batch_get_item(
            RequestItems={
                table_name: {
                    'Keys': request_keys
                }
            }
        )
        items.extend(response['Responses'].get(table_name, []))

    return items


def batch_write_items(dynamodb_resource, table_name, items):
    """Write items to target table in batch."""
    table = dynamodb_resource.Table(table_name)

    with table.batch_writer(overwrite_by_pkeys=[PK_NAME, SK_NAME]) as writer:
        for item in items:
            writer.put_item(Item=item)


def download(path: str):
    source_session = boto3.Session(**SOURCE_AWS)
    source_dynamodb = source_session.resource('dynamodb')
    print("🔍 Scanning source table...")
    source_keys = get_all_keys(source_dynamodb, SOURCE_TABLE_NAME)
    print(f"📦 Fetching {len(source_keys)} items from source table...")
    source_items = get_items_by_keys(source_dynamodb, SOURCE_TABLE_NAME, source_keys)
    print("🔍 Downloading source table...")

    with open(path, "w") as fp:
        json.dump(source_items, fp, default=str)

    print("🔍 Done!")

def sync():
    # Create separate sessions for source and target
    source_session = boto3.Session(**SOURCE_AWS)
    target_session = boto3.Session(**TARGET_AWS)

    source_dynamodb = source_session.resource('dynamodb')
    target_dynamodb = target_session.resource('dynamodb')

    print("🔍 Scanning source table...")
    source_keys = get_all_keys(source_dynamodb, SOURCE_TABLE_NAME)

    print("🔍 Scanning target table...")
    target_keys = get_all_keys(target_dynamodb, TARGET_TABLE_NAME)

    missing_keys = list(source_keys - target_keys)
    print(f"➡️ Found {len(missing_keys)} missing items to copy...")

    if not missing_keys:
        print("✅ Target table is already up to date.")
        return

    # # Fetch missing items from source
    # print("📦 Fetching missing items from source table...")
    # missing_items = get_items_by_keys(source_dynamodb, SOURCE_TABLE_NAME, missing_keys)

    # # Write to target
    # print("📝 Writing missing items to target table...")
    # batch_write_items(target_dynamodb, TARGET_TABLE_NAME, missing_items)

    print("✅ Sync complete!")


def main():
    # download("D:\\output.json)
    sync()         

if __name__ == '__main__':
    main()
