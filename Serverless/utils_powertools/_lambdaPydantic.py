# https://pydantic.dev/articles/lambda-intro

from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
    computed_field,
    validate_call,
    FutureDate,
    PastDate,
)
from datetime import date


class UserSignUpEvent(BaseModel):
    name: str
    # birthday: date
    birthday: PastDate
    email: str

    @computed_field
    @property
    def age(self) -> int:
        return (date.today() - self.birthday).days // 365

    @field_validator("name")
    @classmethod
    def name_has_first_and_last(cls, v: str) -> str:
        stripped_name = v.strip()
        if " " not in stripped_name:
            raise ValueError("`name` must contain first and last name, got {v}")
        return stripped_name.title()


class Context(BaseModel):
    aws_request_id: str
    function_name: str


def lambda_handler(event: dict, context: dict) -> dict:
    try:
        user = UserSignUpEvent.model_validate(event)
        context_data = Context.model_validate(context)
    except ValidationError as e:
        return {"result": "error", "message": e.errors(include_url=False)}

    return {
        "result": "success",
        "user": user.model_dump(mode="json"),
        "request_id": context_data.aws_request_id,
    }


@validate_call
def lambda_handler_inner(event: UserSignUpEvent, context: Context) -> dict:
    return {
        "result": "success",
        "user": event.model_dump(mode="json"),
        "request_id": context.aws_request_id,
    }


def lambda_handler(event: dict, context: dict) -> dict:
    try:
        response = lambda_handler_inner(event, context)
        return response
    except ValidationError as e:
        return {"result": "error", "message": e.errors(include_url=False)}
