import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("table-1")

def lambda_handler(event, context):
    
    #print(event)
    for k, v in event.items():
        print(k, "-", v)
        item = {k: v}
        # table.put_item(Item=item)
        table.put_item(
            Item={'id': v},
            ConditionExpression="attribute_not_exists(id)"
        )
    
    # my_id = '001'
    # response = table.get_item(
    # Key={
    #         'id': my_id
    #     }
    # )
    # print("Response: ", response)
    # if response.get('Item') is not None:
    #     item = response['Item']
    #     print("Item: ", item)
    # else:
    #     print("Not found: ", my_id)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
