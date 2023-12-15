import os
import time
import json
from pathlib import Path
import pydantic
from pydantic import BaseModel
import pytest
from typing import List, Dict, Optional
#from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent

# https://www.youtube.com/watch?v=Vj-iU-8_xLs
class APIGWEvent(BaseModel):
    body: Optional[str]
    headers: dict
    multiValueHeaders: dict
    httpMethod: str
    isBase64Encoded: bool
    path: str
    pathParameters: dict
    queryStringParameters: dict
    multiValueQueryStringParameters: dict
    stageVariables: dict
    requestContext: dict
    resource: str

    # @pydantic.model_validator(mode='before')
    # @classmethod
    # def check_model(cls, values):
    #     pass

    @pydantic.field_validator('stageVariables')
    @classmethod
    def check_stage_variables(cls, value):
        if value is None:
            raise ValueError('stageVariables cannot be None')
        return value


def main() -> None:
    #print(os.getcwd())
    #print(os.listdir('.'))
    #event = None

    start = time.perf_counter()
    with open("aws-templates/Serverless-SAM/events/apigw-proxy.json") as file:
        event = json.load(file)
        #print(event["multiValueHeaders"]["Accept"][0])
        try:
            parsedEvent = APIGWEvent(**event)
            #print(parsedEvent.headers)
        except Exception as e:
            print(e)
    
    with(pytest.raises(pydantic.ValidationError)):
        parsedEvent = APIGWEvent(**event)
        #print(parsedEvent.headers)
        return parsedEvent.model_dump()

    
    print(f"Time: {time.perf_counter() - start}")
    

if __name__ == "__main__":
    main()