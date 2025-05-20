
# https://www.youtube.com/watch?v=wLNBsr_JKuc

import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime', region_name='eu-west-3')

prompt = 'What is the GIL in Python?'

parameters = {
    "modelId": "mistral.mistral-large-2402-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        'prompt': f'<s>[INST] {prompt} [/INST]',
        'max_tokens': 200,
        'temperature': 0.2,
        'top_p': 0.9,
        'top_k': 50
    })
}

response = bedrock_runtime.invoke_model(**parameters)

print(response['body'].read())