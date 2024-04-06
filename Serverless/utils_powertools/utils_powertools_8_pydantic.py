# https://docs.powertools.aws.dev/lambda/python/2.29.1/utilities/parser/#event_parser-decorator
# https://github.com/koxudaxi/datamodel-code-generator

from aws_lambda_powertools.utilities.parser import event_parser, BaseModel, ValidationError, parse, validator, root_validator
from aws_lambda_powertools.utilities.typing import LambdaContext
from typing import List, Optional

import json

class OrderItem(BaseModel):
    id: int
    quantity: int
    description: str

    @validator('description')
    def check_desc(cls, v):
        if v != "hello world":
            raise ValueError("Description must be hello world!")
        return v
    
    @validator('*')
    def has_whitespace(cls, v):
        if v is None:
            raise ValueError("All fields must have values")
        return v    

class Order(BaseModel):
    id: int
    description: str
    items: List[OrderItem] # nesting models are supported
    optional_field: Optional[str] = None # this field may or may not be available when parsing

class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password1'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return values

@event_parser(model=Order)
def handler(event: Order, context: LambdaContext):
    print(event.id)
    print(event.description)
    print(event.items)

    order_items = [item for item in event.items]
    
    def my_function():
        try:
            parsed_payload: Order = parse(event=payload, model=Order)
            # payload dict is now parsed into our model
            return parsed_payload.items
        except ValidationError:
            return {
                "status_code": 400,
                "message": "Invalid order"
            }

payload = {
    "id": 10876546789,
    "description": "My order",
    "items": [
        {
            "id": 1015938732,
            "quantity": 1,
            "description": "item xpto"
        }
    ]
}

handler(event=payload, context=LambdaContext())
handler(event=json.dumps(payload), context=LambdaContext()) # also works if event is a JSON string
