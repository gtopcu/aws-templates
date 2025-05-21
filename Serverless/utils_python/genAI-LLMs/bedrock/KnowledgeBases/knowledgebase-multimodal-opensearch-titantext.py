

# https://www.youtube.com/watch?v=cIjBfl5oEKE

# pip install -U boto3 botocore python-dotenv
import os
import boto3
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client(
    service_name='bedrock-agent-runtime',
    config=Config(region_name=os.environ.get('AWS_REGION', 'us-west-2'))
)

user_query = ""

response = bedrock.retrieve_and_generate(
    input={
        'text': user_query
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': os.environ['KNOWLEDGE_BASE_ID'],
            'modelArn': f"arn:aws:bedrock:{os.environ.get('AWS_REGION', 'us-west-2')}::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0"
        }
    }
)