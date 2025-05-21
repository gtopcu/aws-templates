
# https://towardsaws.com/detailed-roadmap-generative-ai-implementation-in-serverless-computing-using-aws-bedrock-f243755f0a3b

# pip install -U boto3 botocore python-dotenv
import os
import json
import boto3
from botocore.config import Config
from dotenv import load_dotenv

# load_dotenv()

# bedrock = boto3.client(
#     service_name='bedrock-agent-runtime',
#     config=Config(region_name=os.environ.get('AWS_REGION', 'us-west-2'))
# )

bedrock=boto3.client(service_name="bedrock-runtime")

prompt_data="""
AI tell me more about advertising in ecommerce using social media
"""

payload={
    "prompt":prompt_data,
    "maxTokens":512,
    "temperature":0.8,
    "topP":0.8
}
body = json.dumps(payload)
model_id = "ai21.j2-mid-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

output = json.loads(response.get("body").read())
response_text = output.get("completions")[0].get("data").get("text")
print(response_text)