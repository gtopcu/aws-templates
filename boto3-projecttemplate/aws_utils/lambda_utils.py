
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-start-lambda.html

# Must be in root dir
# sam local invoke <options>
# sam local invoke HelloWorldFunction
# sam local invoke HelloWorldFunction --event events/event.json
# sam local start-api <options>
# sam local start-lambda <options>
# aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt

import boto3
from botocore.config import Config
from botocore import UNSIGNED

print("Invoking lambda..")
lambda_client = boto3.client('lambda',
                             endpoint_url="http://127.0.0.1:3001",
                             use_ssl=False,
                             verify=False,
                             config=Config(signature_version=UNSIGNED,
                                           read_timeout=3,
                                           retries={'max_attempts': 0}
                                           )
                            )
lambda_client.invoke(FunctionName="ApiFunction")


