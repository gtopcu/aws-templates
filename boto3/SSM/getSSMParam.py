import json
import boto3

client = boto3.client('ssm')

def lambda_handler(event, context):
    
    #print(event)
    #print(context)
    #print("Done!")
    
    #Get max object size config from SSM
    paramMaxSize = int(client.get_parameter(
        Name='/dev/guardrails/max_size',
        WithDecryption=True|False
    )["Parameter"]["Value"])
    print(paramMaxSize)
    
    #Get object size from S3 event 
    s3_obj_size = int(event["Records"][0]["s3"]["object"]["size"])
    print(s3_obj_size)
    
    if s3_obj_size > paramMaxSize:
        raise Exception("Object exceeds max allowed size")
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

    

