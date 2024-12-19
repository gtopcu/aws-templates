
# https://dev.to/aws-builders/save-time-with-the-amazon-bedrock-converse-api-2ai6

import boto3, json

#create a boto3 session - stores config state and allows you to create service clients
session = boto3.Session()

#create a Bedrock Runtime Client instance - used to send API calls to AI models in Bedrock
bedrock = session.client(service_name='bedrock-runtime')

#here's our prompt telling the model what we want it to do, we can change this later
system_prompts = [{"text": "You are an app that creates reading lists for book groups."}]

message_list = []

initial_message = {
                "role": "user",
                "content": [{"text": "Create a list of five novels suitable for a book group who are interested in classic novels."}],
            }

message_list.append(initial_message)

response = bedrock.converse(
                modelId="anthropic.claude-v2",
                messages=message_list,
                system=system_prompts,
                inferenceConfig={
                            "maxTokens": 2048,
                            "temperature": 0,
                            "topP": 1
                            },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4))