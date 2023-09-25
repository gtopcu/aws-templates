import boto3
import json

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.event_handler import (
    APIGatewayRestResolver,
    Response,
    content_types,
)
from aws_lambda_powertools.event_handler.exceptions import (
    BadRequestError,
    InternalServerError,
    NotFoundError,
    ServiceError,
    UnauthorizedError,
)
from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEvent

"""
from botocore.exceptions import ClientError
try:
    client = boto3.client('translate')
except ClientError as e:
    logging.warning(f"Error: {e}")
"""

#tracer = Tracer()
logger = Logger(log_uncaught_exceptions=False)
#metrics = Metrics(capture_cold_start_metric=True)
#metrics.set_default_dimensions(environment=STAGE, another="one")
app = APIGatewayRestResolver()

#@tracer.capture_method
@app.get("/todos/<todo_id>")
#@app.get(".+")
#@app.post("/todos")
#@app.route("/todos", method=["PUT", "POST"])
def handler_get(todo_id: str):
    data: dict = app.current_event.json_body 
    #app.lambda_context
    #api_key: str = app.current_event.get_header_value(name="X-Api-Key", case_sensitive=True, default_value="")
    #todo_id: str = app.current_event.get_query_string_value(name="id", default_value="")
    #raise BadRequestError("Missing required parameter")  # HTTP  400
    return None

@app.not_found
#@tracer.capture_method
def handle_not_found_errors(exc: NotFoundError) -> Response:
    logger.info(f"Not found route: {app.current_event.path}")
    return Response(status_code=404, content_type=content_types.TEXT_PLAIN, body="Not found")

#@tracer.capture_lambda_handler
#@metrics.log_metrics  # ensures metrics are flushed upon request completion/failure
@logger.inject_lambda_context(log_event=True, 
                              clear_state=True, #clear logger cache
                              correlation_id_path=correlation_paths.API_GATEWAY_REST)
@event_source(data_class=APIGatewayProxyEvent)
def handler(event: APIGatewayProxyEvent, context: LambdaContext) -> dict:
    
    return app.resolve(event, context)
    
    #print(event)
    #input = json.loads(json_string)
    #indented = json.dumps(json_input, indent=2)
    #print(event['Input'][0]['Text'])

    # req_id = context.aws_request_id
    # remaining_time = context.get_remaining_time_in_millis()
    # memory_limit = context.memory_limit_in_mb

    # if "path" in event.path and event.http_method == "GET":
    #     request_context = event.request_context
    #     identity = request_context.identity
    #     user = identity.user
    #     print(event.json_body)
    
    #logger.append_keys(order_id=order_id)
    #logger.info("Collecting payment", order_id=order_id)
    #logger.info("Success")
    #metrics.add_dimension(name="environment", value=STAGE)
    #metrics.add_metric(name="SuccessfulRuns", unit=MetricUnit.Count, value=1, resolution=MetricResolution.High)

    # Get a single parameter from SSM
    # endpoint_url: str = parameters.get_parameter("/lambda-powertools/endpoint_url")
    # api_key: Any = parameters.get_secret("/lambda-powertools/api-key")
    # headers: dict = {"X-API-Key": api_key}

    # if 'order_id' in event.path and event.http_method == 'GET':
    #     print(event.body)

    # return {"statusCode": 200, "body": "success"}

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


