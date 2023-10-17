# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-start-lambda.html
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html

# Must be in root dir
# sam local invoke <options>
# sam local invoke HelloWorldFunction
# sam local invoke HelloWorldFunction --event events/event.json
# sam local start-api <options>
# sam local start-lambda <options>
# aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt

import boto3
import botocore
import json
from pathlib import Path

# sam local start-lambda
running_locally = True
lambda_client = None
function_name = ""
event = ""


def load_event(path: Path):
    with path.open() as f:
        return json.load(f)

def main() -> None:

    event = load_event(path=Path("events/sqs_event.json"))

    if running_locally:
        lambda_client = boto3.client('lambda',
            region_name="us-west-2",
            endpoint_url="http://127.0.0.1:3001",
            use_ssl=False,
            verify=False,
            config=botocore.client.Config(
                signature_version=botocore.UNSIGNED,
                read_timeout=10,
                retries={'max_attempts': 0},
            )
        )
    else:
        lambda_client = boto3.client('lambda')

    response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=event
        )

    # Verify the response
    assert response == "Hello World"