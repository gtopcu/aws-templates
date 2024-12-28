# https://docs.powertools.aws.dev/lambda/python/latest/utilities/parser/#key-features

from pydantic import BaseModel, ValidationError
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser, parse

"""
{
    "id": "12345",
    "name": "Jane Doe"
}
"""
class MyEvent(BaseModel):
    id: int
    name: str


# @event_parser(model=MyEvent) # raises a ValidationError directly from Pydantic
def lambda_handler(event: MyEvent, context:LambdaContext):
    
    # return {"statusCode": 200, "body": f"Hello {event.name}, your ID is {event.id}"}
    try:
        parsed_event: MyEvent = parse(model=MyEvent, event=event)
        return {
            "statusCode": 200,
            "body": f"Hello {parsed_event.name}, your ID is {parsed_event.id}",
        }
    except ValidationError as e:
        return {"statusCode": 400, "body": f"Validation error: {str(e)}"}

        # try:
        #     my_event: MyEvent = parse(event=event, model=MyEvent)
        #     return event.name
        # except ValidationError:
        #     return {
        #         "status_code": 400,
        #         "message": "Invalid input data" 
        #     }