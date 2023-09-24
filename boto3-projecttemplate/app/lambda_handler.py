import boto3

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

"""
from botocore.exceptions import ClientError
try:
    client = boto3.client('translate')
except ClientError as e:
    logging.warning(f"Error: {e}")
"""

#tracer = Tracer()
logger = Logger()

#@logger.inject_lambda_context
#@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext) -> dict:
    print(event)
    #input = json.loads(json_string)
    #indented = json.dumps(json_input, indent=2)
    print(event['Input'][0]['Text'])
    #logger.info("Success")
    return {"statusCode": 200, "body": "success"}

    """
	transactionId = event['queryStringParameters']['transactionId']
	print('transactionId=' + transactionId)
	transactionResponse['message'] = 'Hello from Lambda land'

	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	return responseObject
    """

if __name__=="__main__":
    handler()


