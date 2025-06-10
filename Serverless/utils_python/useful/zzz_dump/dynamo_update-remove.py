import boto3
from boto3.dynamodb.conditions import Attr
 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('COMPANY_DATA')
 
# You may want to use pagination for large tables
response = table.scan(
    FilterExpression=Attr('is_leased_facility').exists()
)
 
for item in response['Items']:
    is_leased = item.get('is_leased_facility', False)
    ownership_status = 'LEASED_NO_CONTROL' if is_leased else 'LEASED_OWNED_COMPANY_USE'
 
    # Primary key: Composite key (PK, SK)
    key = {
        'PK': item['PK'],
        'SK': item['SK'],
    }
 
    # Update the item
    table.update_item(
        Key=key,
        UpdateExpression='SET ownership_status = :status REMOVE is_leased_facility',
        ExpressionAttributeValues={':status': ownership_status}
    )
 
print('Migration complete.')