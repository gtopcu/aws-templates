
# https://pypi.org/project/pydantic-dynamo/

from pydantic import BaseModel
from typing import Optional

import boto3
import json

class Person(BaseModel):
    Name: str
    Address: Optional[Address]

class Address(BaseModel):
   HouseNumber: int
   current: bool
   street: str


dynamo_resource = boto3.Session().resource('dynamodb', region_name='us-west-2')
person_table = dynamo_resource.Table('person')

items: list[Person] = None

with person_table.batch_writer() as batch:
    for item in items:
        json_string = item.model_dump_json(exclude_defaults=True, exclude_none=True)
        record = json.loads(json_string)
        batch.put_item(record)

# As plain string:
with person_table.batch_writer() as batch:
    for item in items:
        record = item.model_dump(exclude_defaults=True, exclude_none=True)
        batch.put_item(json.dumps(record))