import boto3

# TABLE_NAME = "Dev-CdkCorePlatformStack51FD4ACB-User00B015A1-13QBM3OCLDAHM"
# TABLE_NAME = "Prod-CdkCorePlatformStack51FD4ACB-User00B015A1-KEGP4Z5QC79J"
TABLE_NAME = "Test-CdkCorePlatformStack51FD4ACB-User00B015A1-YKQ8AWCW81MI"

OLD_COLUMN_NAME = "role"
NEW_COLUMN_NAME = "title"

dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table(TABLE_NAME)

response = table.scan()
records = response["Items"]
while "LastEvaluatedKey" in response:
    response = table.scan(
        ExclusiveStartKey=response["LastEvaluatedKey"],
    )
    records.extend(response["Items"])

print("Old ->\n\n", records)

new_records = []

for record in records:
    new_record = {}
    for field, value in record.items():
        if field == OLD_COLUMN_NAME:
            new_record[NEW_COLUMN_NAME] = value
        else:
            new_record[field] = value
    table.put_item(Item=new_record)


response = table.scan()
records = response["Items"]
while "LastEvaluatedKey" in response:
    response = table.scan(
        ExclusiveStartKey=response["LastEvaluatedKey"],
    )
    records.extend(response["Items"])
print("\n\nNew ->\n\n", records)