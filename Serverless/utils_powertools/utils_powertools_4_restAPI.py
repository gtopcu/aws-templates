
# https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/api_gateway/
# https://docs.powertools.aws.dev/lambda/python/latest/utilities/data_classes/#api-gateway-proxy-v2
# https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
# https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

# When using the data validation feature, you need to add pydantic as a dependency
# Resolvers: APIGatewayRestResolver, APIGatewayHttpResolver, ALBResolver, LambdaFunctionUrlResolver, VPCLatticeResolver

from aws_lambda_powertools import Logger, Tracer
#from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response, content_types
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver, Response, content_types # for HTTP v2
#from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

# from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEvent
from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2 # for HTTP v2
#from aws_lambda_powertools.utilities.data_classes import event_source, LambdaFunctionUrlEvent
from aws_lambda_powertools.event_handler.openapi.exceptions import RequestValidationError

from aws_lambda_powertools.event_handler.exceptions import (
    BadRequestError,
    InternalServerError,
    NotFoundError,
    ServiceError,
    UnauthorizedError,
)

import requests
from requests import Response

# from aws_lambda_powertools.utilities.parser import event_parser, parse
# from pydantic import BaseModel, Field, ValidationError
from typing import Any, Optional

tracer = Tracer()
logger = Logger(level="INFO")
# app = APIGatewayRestResolver() 
# app = APIGatewayRestResolver(enable_validation=True, strip_prefixes=["/customDNS"]) 
# app.enable_swagger(path="/swagger", persist_authorization=True)
# cors_config = CORSConfig(allow_origin="https://www.example.com", max_age=300)
# app = APIGatewayRestResolver(cors=cors_config)

app = APIGatewayHttpResolver() # Defaults to v2 payload
# app.enable_swagger(path="/swagger") #, persist_authorization=True)
# app = LambdaFunctionUrlResolver()


# class Todo(BaseModel):  
#     userId: int
#     id_: int | None = Field(default=None, alias="id", default=None)
#     title: str
#     completed: bool


@app.get("/ping")
def ping():
    return {"message": "pong"} # Auto-serializes dictionary responses to JSON and trims

@app.get("/todos")
def get_todos():
    todos: Response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos.raise_for_status()
    return {"todos": todos.json()[:10]}

@app.get("/todos/<todo_id>")
@tracer.capture_method
def get_todo_by_id(todo_id: str) -> Todo:
    my_todo = Todo(userId=1, id_=todo_id, title="delectus aut autem", completed=False)
    # return my_todo.model_dump()
    return my_todo.model_dump_json(by_alias=True)

@app.get(".+")
@tracer.capture_method
def catch_any_route_get_method():
    return {"path_received": app.current_event.path}

@app.post("/todos")
@tracer.capture_method
def create_todo():
    todo_data: dict = app.current_event.json_body  # deserialize json str to dict
    todo: Response = requests.post("https://jsonplaceholder.typicode.com/todos", data=todo_data)
    todo.raise_for_status()
    return {"todo": todo.json()}

# PUT and POST HTTP requests to the path /hello will route to this function
@app.route("/todos", method=["PUT", "POST"])
def create_todo():
    todo_data: dict = app.current_event.json_body  # deserialize json str to dict
    todo: Response = requests.post("https://jsonplaceholder.typicode.com/todos", data=todo_data)
    todo.raise_for_status()
    return {"todo": todo.json()}

# @app.post("/todos")
# def create_todo(todo: Todo) -> int:
#     response = requests.post("https://jsonplaceholder.typicode.com/todos", json=todo.model_dump_json(by_alias=True))
#     response.raise_for_status()

#     return response.json()["id"]

# @app.exception_handler(RequestValidationError)  
# def handle_validation_error(ex: RequestValidationError):
#     logger.error("Request failed validation", path=app.current_event.path, errors=ex.errors())

#     return Response(
#         status_code=422,
#         content_type=content_types.APPLICATION_JSON,
#         body="Invalid data",
#     )

# @app.not_found
# @tracer.capture_method
# def handle_not_found_errors(exc: NotFoundError) -> Response:
#     logger.info(f"Route not found: {app.current_event.path}")
#     return Response(status_code=418, content_type=content_types.TEXT_PLAIN, body="I'm a teapot!")

# @app.exception_handler(ValueError)
# def handle_invalid_limit_qs(ex: ValueError):  # receives exception raised
#     metadata = {"path": app.current_event.path, "query_strings": app.current_event.query_string_parameters}
#     logger.error(f"Malformed request: {ex}", extra=metadata)

#     return Response(
#         status_code=400,
#         content_type=content_types.TEXT_PLAIN,
#         body="Invalid request parameters.",
#     )

# @app.get(rule="/bad-request-error")
# def bad_request_error():
#     raise BadRequestError("Missing required parameter")  # HTTP  400

# You can continue to use other utilities just as before
@tracer.capture_lambda_handler#(capture_response=False, capture_error=False)
@logger.inject_lambda_context(log_event=True, #beware of sensitive data!
                              clear_state=True, #logger is global scope
                              # correlation_id_path=correlation_paths.API_GATEWAY_REST
                              correlation_id_path=correlation_paths.API_GATEWAY_HTTP
                              )

# @event_source(data_class=APIGatewayProxyEvent) 
@event_source(data_class=APIGatewayProxyEventV2) # for HTTP v2
def lambda_handler(event: APIGatewayProxyEventV2, context:LambdaContext) -> dict:

    # event.path
    # event.body
    # event.json_body
    # event.headers.get("X-Api-Key")
    # event.get_header_value
    # event.path_parameters
    # event.query_string_parameters.get("id")
    # event.query_string_parameters["id"]
    # event.get_query_string_value

    logger.debug(event)

    logger.debug(
            {
                "request_id": context.aws_request_id,
                "function_name": context.function_name,
                "function_version": context.function_version,
                "log_group_name": context.log_group_name,
                "memory_limit_in_mb": context.memory_limit_in_mb,
                "remaining_time": context.get_remaining_time_in_millis()
            },
        )

    return app.resolve(event, context)

    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Content-Type": "application/json"
    #     },
    #     "body": {
    #         "message": "Hello from Lambda!",
    #         "path": event["path"],
    #         "method": event["httpMethod"],
    #         "queryStringParameters": event["queryStringParameters"],
    #         "headers": event["headers"],
    #         "request_id": context.aws_request_id,
    #     }
    # }




