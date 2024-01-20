# https://docs.powertools.aws.dev/lambda/python/2.29.1/utilities/parser/#event_parser-decorator
from aws_lambda_powertools.utilities.parser import event_parser, BaseModel
from aws_lambda_powertools.utilities.typing import LambdaContext
from typing import List, Optional

import json

class OrderItem(BaseModel):
    id: int
    quantity: int
    description: str

class Order(BaseModel):
    id: int
    description: str
    items: List[OrderItem] # nesting models are supported
    optional_field: Optional[str] = None # this field may or may not be available when parsing


@event_parser(model=Order)
def handler(event: Order, context: LambdaContext):
    print(event.id)
    print(event.description)
    print(event.items)

    order_items = [item for item in event.items]
    ...

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
