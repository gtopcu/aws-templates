
import boto3

lambda_client = boto3.client('lambda')

def invoke_lambda(function_name, event):
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=event
    )
    return response


