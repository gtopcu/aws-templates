
import boto3

lambda_client = boto3.client('lambda')

def invoke_lambda(function_name, event):
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=event
    )
    return response


# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html

# import boto3
# import botocore

# # Set "running_locally" flag if you are running the integration test locally
# running_locally = True

# if running_locally:

#     # Create Lambda SDK client to connect to appropriate Lambda endpoint
#     lambda_client = boto3.client('lambda',
#         region_name="us-west-2",
#         endpoint_url="http://127.0.0.1:3001",
#         use_ssl=False,
#         verify=False,
#         config=botocore.client.Config(
#             signature_version=botocore.UNSIGNED,
#             read_timeout=5,
#             retries={'max_attempts': 0},
#         )
#     )
# else:
#     lambda_client = boto3.client('lambda')


# # Invoke your Lambda function as you normally usually do. The function will run
# # locally if it is configured to do so
# response = lambda_client.invoke(FunctionName="HelloWorldFunction")

# # Verify the response
# assert response == "Hello World"