import boto3
import botocore.exceptions.ClientError
import json


def template_conversion(template_file_path):

    """
    This function converts a Terraform template to work on AWS.
    The different functional models have individual request and response formats.
    For the formatting for the Anthropic Claude, refer to:
    https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html

    """

    try:

        with open(template_file_path) as file:

            template = file.read()

        bedrock_runtime = boto3.client(region_name="us-east-1",
                                       service_name='bedrock-runtime')

        prompt = f"Convert to work on AWS output as a template\n{template}"

        # Claude requires you to enclose the prompt as follows:
        enclosed_prompt = "\n\nHuman: " + prompt + "\n\nAssistant:"

        body = json.dumps({
            "prompt":  enclosed_prompt,
            "max_tokens_to_sample": 4096,
            "temperature": 0.5,
        }
        ).encode()

        response = bedrock_runtime.invoke_model(body=body, modelId="anthropic.claude-v2")
        response_body = json.loads(response.get('body').read())
        print(response_body.get('completion'))
        return response_body.get('completion')

    except ClientError:
        logger.error("Couldn't invoke Anthropic Claude")
        raise


result = template_conversion('azure.tf')

with open('aws.tf', 'a') as file:
    file.write(result)
    file.close()

with open('aws.tf', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(lines[2:])

with open("aws.tf") as f:
    lines = f.readlines()

index = -1
for i, line in enumerate(reversed(lines)):
    if "}" in line:
        index = len(lines) - i
        break

if index != -1:
    del lines[index+1:]

with open("aws.tf", "w") as f:
    f.writelines(lines)
