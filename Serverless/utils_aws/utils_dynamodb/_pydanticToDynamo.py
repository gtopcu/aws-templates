
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

with person_table.batch_writer() as batch:
    for item in list:
        json_string = item.model_dump_json()
        record = json.loads(json_string)
        batch.put_item(record)

# As plain string:
with person_table.batch_writer() as batch:
    for i in list:
        record = i.dict()
        batch.put_item(json.dumps(record))