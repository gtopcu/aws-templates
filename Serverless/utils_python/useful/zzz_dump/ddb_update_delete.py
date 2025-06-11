
import boto3
from boto3.dynamodb.conditions import Attr
 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('COMPANY_DATA')
 

response = table.scan(
    FilterExpression=Attr('is_active').exists()
)
 
for item in response['Items']:
    is_active = item.get('is_active', False)
    is_active = not is_active
 
    key = {
        'PK': item['PK'],
        'SK': item['SK'],
    }
 
    table.update_item(
        Key=key,
        UpdateExpression='SET is_active = :status DELETE(REMOVE?) address',
        ExpressionAttributeValues={':status': is_active}
    )
 