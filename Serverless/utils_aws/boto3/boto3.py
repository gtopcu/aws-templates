
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html

import boto3
import botocore
from botocore.exceptions import ClientError
import boto3.session
import logging

# Boto3 adheres to the following lookup order when searching through sources for configuration values:
# - A Config object that’s created and passed as the config parameter when creating a client
# - Environment variables
# - The ~/.aws/config file

# Retries are only available in DEBUG log mode !!!
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html

# [myConfigProfile]
# region = us-east-1
# max_attempts = 10
# retry_mode = standard

# Setting custom config - modes: legacy/standard/adaptive, default is legacy with 5 max retries
from botocore.config import Config
my_config = Config(
    region_name = 'us-west-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'adaptive'
    }
)
client = boto3.client('kinesis', config=my_config)

# Session - not thread safe, create new one per thread
my_session = boto3.session.Session()
credentials = boto3.session.Session().get_credentials()
awsauth = botocore.auth.AWS4Auth(credentials.access_key, credentials.secret_key, 'us-west-2', 'kinesis')
# aws_access_key_id
# aws_secret_access_key
# region_name
# profile_name

# Now we can create low-level clients or resource clients from our custom session
sqs = my_session.client('sqs')
s3 = my_session.resource('s3')

# Catch exceptions through ClientError and parse error codes for all service-side exceptions and errors
try:
    client.describe_stream(StreamName='myDataStream')

except ClientError as err:
    # print(str(err))
    print("Error Code: " + f"{err.response['Error']['Code']}")
    print("Error Message: " + f"{err.response['Error']['Message']}")

# list all boto3 exceptions
for key, value in sorted(botocore.exceptions.__dict__.items()):
    if isinstance(value, type):
        print(key)

"""
{
    'Error': {
        'Code': 'SomeServiceException',
        'Message': 'Details/context around the exception or error'
    },
    'ResponseMetadata': {
        'RequestId': '1234567890ABCDEF',
        'HostId': 'host ID data will appear here as a hash',
        'HTTPStatusCode': 400,
        'HTTPHeaders': {'header metadata key/values will appear here'},
        'RetryAttempts': 0
    }
}

"""
# Client
# Client instances are thread-safe, but creating them is not. Create before using them with a ThreadPoolExecutor
client = boto3.client('aws_service_name')
try:
    client.some_api_call(SomeParam='some_param')

except botocore.exceptions.ClientError as error:
    # Put your error handling logic here
    raise error

except botocore.exceptions.ParamValidationError as error:
    raise ValueError('The parameters you provided are incorrect: {}'.format(error))


#  AWS service specific exception with Client
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

client = boto3.client('kinesis')

try:
    logger.info('Calling DescribeStream API on myDataStream')
    client.describe_stream(StreamName='myDataStream')

except ClientError as error:
    if error.response['Error']['Code'] == 'LimitExceededException':
        logger.warn('API call limit exceeded; backing off and retrying...')
    else:
        raise error
# except client.exceptions.LimitExceedException as error: # catching specific error
#     logger.warn('API call limit exceeded; backing off and retrying...')

# same example for SQS
client = boto3.client('sqs')
queue_url = 'SQS_QUEUE_URL'

try:
    client.send_message(QueueUrl=queue_url, MessageBody=('some_message'))

except ClientError as err:
    if err.response['Error']['Code'] == 'InternalError': # Generic error
        print('Error Message: {}'.format(err.response['Error']['Message']))
        print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
        print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
    else:
        raise err


# Resource
# Not thread safe create new one per thread
client = boto3.resource('s3')

try:
    client.create_bucket(BucketName='myTestBucket')

except client.meta.client.exceptions.BucketAlreadyExists as err:
    print("Bucket {} already exists!".format(err.response['Error']['BucketName']))
    raise err


# Install latest boto3 for lambda
# import sys
# from pip._internal import main
# main(['install', '-I', '-q', 'boto3', '--target', '/tmp/', '--no-cache-dir', '--disable-pip-version-check'])
# sys.path.insert(0,'/tmp/')
# import boto3

