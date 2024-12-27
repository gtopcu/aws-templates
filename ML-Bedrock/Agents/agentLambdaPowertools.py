
# https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/bedrock_agents/
# https://www.youtube.com/watch?v=NWoC5FTSt7s
# https://www.youtube.com/watch?v=2L_XE6g3atI

# from distutils import version # Deprecated since version 3.10, removed in version 3.12.
import requests

# from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.bedrock_agent import BedrockAgentResolver
from aws_lambda_powertools.utilities.typing import LambdaContext    
from aws_lambda_powertools.event_handler.openapi.params import Query, Body

from typing import Annotated
# from typing_extensions import TypedDict
# from pydantic import EmailStr

# for testing
from dataclasses import dataclass
import pytest


logger = Logger(service="bedrock-agent-lambda-meetings")
# tracer = Tracer(service="bedrock-agent-resolver")
app = BedrockAgentResolver()

# @app.get("/latest_version", description="Returns the latest version of AWS Powertools")
# def powertools_version() -> str:
#     response = requests.get("https://pypi.org/pypi/aws-lambda-powertools/json")
#     response.raise_for_status()

#     data = response.json()
#     releases = data["releases"]

#     versions = []
#     for release in releases:
#         versions.append(version.parse(release))
#     return max(versions).public

# @app.get("/todos/<todo_id>",
#     summary="Retrieves a TODO item, returning it's title",
#     description="Loads a TODO item identified by the `todo_id`",
#     response_description="The TODO title",
#     responses={
#         200: {"description": "TODO item found"},
#         404: {
#             "description": "TODO not found",
#         },
#     },
#     tags=["todos"],
# )

@app.get("/meeting_list", description="Returns the list of meetings")
def meeting_list() -> Annotated[str, Body(description="List of scheduled meetings")]:
    return "You have 1 meeting with gtopcu@gmail.com"

@app.post("/schedule_meeting", description="Schedules a meeting with the given email")
def schedule_meeting(email:Annotated[str, Query(max_length=200, description="Email address of the attendee to schedule the meeting with")]
    ) -> Annotated[str, Body(description="Email address of the scheduled attandee")]:
    
    # Append correlation data to all generated logs. This can be used to aggregate logs by session_id 
    # and observe the entire conversation between a user and the Agen
    logger.append_keys(
        session_id=app.current_event.session_id,
        action_group=app.current_event.action_group,
        input_text=app.current_event.input_text,
        # app.current_event.api_path
        # app.current_event.http_method
        # app.current_event.agent
        # app.current_event.parameters
        # app.current_event.decoded_body
    )
    return "Scheduled meeting with: " + email
   
# @tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event:dict, context:LambdaContext):

    logger.info("Agent Lambda Handler called")
    return app.resolve(event, context)


if __name__ == "__main__":
    schema = app.get_openapi_json_schema(   title="Meeting API", 
                                            version="1.0.0",
                                            description="Provides API methods to view and schedule meetings")
    with open("openapi.json", "w") as f:
        f.write(schema)
    # print(schema)


# Testing ------------------------------------------------------------------------

@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()

def test_lambda_handler(lambda_context):
    minimal_event = {
        "apiPath": "/current_time",
        "httpMethod": "GET",
        "inputText": "What is the current time?",
    }
    resp = lambda_handler(minimal_event, lambda_context)
    assert resp["response"]["httpStatuScode"] == 200
    assert resp["response"]["responseBody"]["application/json"]["body"] != ""