import json
import os
import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['DDB_TABLE_NAME'])
_lambda = boto3.client('lambda')


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    # response = table.get_item(
    #     Key={'PK': event['path']}
    # )
    table.update_item(
        Key={'path': event['path']},
        UpdateExpression='ADD hits :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    resp = _lambda.invoke(
        FunctionName=os.environ['LAMBDA_NAME'],
        Payload=json.dumps(event),
    )
    body = resp['Payload'].read()

    print('downstream response: {}'.format(body))
    return json.loads(body)
