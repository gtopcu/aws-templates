
from pydantic import BaseModel
from typing import Optional
import json

# https://github.com/pydantic/pydantic/issues/8006
# Do not use Optional[str] = None, use str | None = None instead
# model_dump with exclude_defaults=True or exclude_none=True

class Person(BaseModel):
    ID: str
    Name: str
    Age: int | None = None
    Address: str | None = None 
    Hobbies: list[str] | None = None