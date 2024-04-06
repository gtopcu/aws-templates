# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/event_handler/api_gateway/

# When using the data validation feature, you need to add pydantic as a dependency
# Resolvers: APIGatewayRestResolver, APIGatewayHttpResolver, ALBResolver, LambdaFunctionUrlResolver, VPCLatticeResolver

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
#from aws_lambda_powertools.event_handler import APIGatewayHttpResolver # for HTTP v2
#from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEvent
#from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2 # for HTTP v2


import requests
from requests import Response

tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()
#app = APIGatewayHttpResolver() # Defaults to v2 payload
#app = LambdaFunctionUrlResolver()


@app.get("/todos")
def get_todos():
    todos: Response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos.raise_for_status()
    # for brevity, we'll limit to the first 10 only
    return {"todos": todos.json()[:10]}

@app.get("/todos/<todo_id>")
@tracer.capture_method
def get_todo_by_id(todo_id: str):
    todos: Response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    todos.raise_for_status()
    return {"todos": todos.json()}

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

# You can continue to use other utilities just as before
@tracer.capture_lambda_handler#(capture_response=False, capture_error=False)
@logger.inject_lambda_context(#log_event=True, #beware of sensitive data!
                              clear_state=True, #logger is global scope
                              correlation_id_path=correlation_paths.API_GATEWAY_REST)

@event_source(data_class=APIGatewayProxyEvent) 
def lambda_handler(event: APIGatewayProxyEvent, context) -> dict:

    # event.path
    # event.body
    # event.json_body
    # event.path_parameters
    # event.get_query_string_value
    # event.get_header_value
    logger.debug(event)

    logger.info(
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






