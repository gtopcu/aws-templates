import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from itertools import islice

# Adds missing items from table1 on source_aws to table2 on target_aws accounts

{
    # "region": "eu-west-2",
    # "access_key": "",
    # "secret_key": "",
    # "session_token": "",
}
SOURCE_AWS = {
    'region_name': 'eu-west-2',
    'aws_access_key_id': 'ASIARK6QF65DWD4QZ67O',
    'aws_secret_access_key': 'PcRNjI9QFVL6zvlkzrGX6Ucixact/iCQdUXQ2onT',
    'aws_session_token': 'IQoJb3JpZ2luX2VjENH//////////wEaCWV1LXdlc3QtMiJGMEQCICR9+KfoAQ2NLBdCNW3sy1jQIZ+eyHuo+8F1AhoE8gQDAiB+1SXgXofNc8d4fRueSVr5R6vtybR7kmivrEfxuHSOXCrzAgjq//////////8BEAAaDDA5MjI0MTUyNDU1MSIMkAQBjjsWP9Dv54N8KscCDDq838jwp5h3JU0FmsqY2gVeU+4USPbO8uSCisv4edr17QnOGwabQ9g+clLTQ/9cCqlaBe0kOHZmR3Zd0ZPV/xtyYZdlGG/u2b5nEg69qdNpNNYelKoVnevxZFCF66D1Q457juZLf/csR0rU+fEpQiji2I/rtVocIqEHHMs0qQsceH4b8vHtDlpRnKw3CMFjr75gz1KRFUuHangSBiYZT6Etw4ukH/Q54VX3Gvdrn5mMLRz3oopuq4ccuY/Ai18X21S/z1xxapuRxuEi5wJjnoV2SuY4D7DcaWT+R5z2Ak3eYGbxTZesyJjv+WDDG70/TAPccC72I6TW5pHAFL0QdOKeo4vkvVZWL/Kz1e8OiLXmKfwwe1d/eRAXo5qDzg5wnSlBJzMFo37Lm1Ewn4bKKDV/fOF9hJXPry6vg/TMvZZuZmTC+uM3MO6a/cMGOqgBwCrF5+0vQku9RPw8G9dCRVsV5RZ6SUGjVXpwPXQC5jInQ6VutDmfroSjFWNRJLzC22dY35HQUzFQdTYtarokeTYcMSRBcf7N7m+IrdJrBnWpwACtr+USjpr/IgLWlDW+855aporzmrhAbtLRALCbDiox2D2ZYpz3JSrIwDf1S8lqXODntCivb9gZVpq13b6yowLFHd9Ky+TtcBxpiFz5MOkEdgM8KyYN',
}
TARGET_AWS = {
    'region_name': 'eu-west-2',
    'aws_access_key_id': 'ASIAVRUVQHZFDLEJZ6E6',
    'aws_secret_access_key': 'pWZ+7kwKy3i0qz64JaOYik/PIfX2VVhXyLrIfpiW',
    'aws_session_token': 'IQoJb3JpZ2luX2VjENH//////////wEaCWV1LXdlc3QtMiJHMEUCIG/mdTGWcQS6FQrhRDUyoqb+y0sWzzEcHgcfpsRNC4nfAiEArb7V46r1+0dGmtjUHLGCPWiVj+uyn7bJ5xblLzTm2mMq8wII6v//////////ARAAGgwzODE0OTE4ODc2OTAiDD5deGenAsqJTh/sJirHAvuEz1ZhZme1IueI+s8plD4K2nQmJte+I6U3CgZcXKWHVYhr7bTwXo54FM9uNOt3N77uCxz2XcbOmb6GbPbaoHGHagF1w9uJesDFuKiw+zTGYq2HHKMqlIZqB7AbipDX5hNT50rSj6bsQdfziU8B5Rzgi+e6ttApty0TqZ515hOdkhlMSmJzJJdff9mlsFym6LukbuczichWpYTrqZNwmxgnTsD7ZAGrIlXjN2XkXXRqtj1XW/yY9fgOJYbfpwQojIZ14SVvMw0W2p0TG/qwJ/n+YM5lJea407dwt+RKmClI2zJoP4wCLyaxXJFgMvDw+rdJhWpSMpdsv9/S2IFZ3pNwkusJpPkua7+jUKD/BsoMD/jsSxY+bFZPikEYE9RklFfgpnbVfGyVAS7Gy4ou3pEmLNm4iyJv2q9prqx4MG7lKEaIlH3jkjCam/3DBjqnAcH6F9PGJWdt/oXgIWh95ecEruC//0nWNC9TKbGxVwzExGLMEG71nInzjqPmI0WWHcIKb5fZUN+B7ZO+vTbP7X6R9ioxYTxM/3QWKEptLO2PJDvPW/UCeDOsvekjOw3IzXehYQg5AxCQ+sCFW4WSCzrSZWFNGkCc6jl2vli4nsqACCjqB30EKdBpDkibnabSYC1woShG4X+v1j8JpEOka493y/TZK9L5',
}

SOURCE_TABLE_NAME = 'GLOBAL_CONSTANTS_DATA'
TARGET_TABLE_NAME = 'GLOBAL_CONSTANTS_DATA'

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

    source_dynamodb = source_session.resource("dynamodb")
    target_dynamodb = target_session.resource("dynamodb")

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
