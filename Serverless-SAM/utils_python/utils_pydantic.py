# https://docs.pydantic.dev/latest/

"""

BaseModel — Pydantic's own super class with many common utilities available via instance methods
pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized

"""

from datetime import datetime
from typing import Any, Optional, TypedDict
# from typing import Dict, List, Tuple
from typing import Literal, Annotated
from annotated_types import Gt, Ge, Le, Lt
from uuid import UUID

import pydantic
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    EmailStr,
    StrictInt,
    PositiveInt
    #StringConstraints,
    #AwareDatetime
)

class User(BaseModel):
    #uuid: UUID = "12345678-1234-1234-1234-123456789012"
    id: int = Field(strict=True)
    name: Optional[str] = "default"
    age: PositiveInt
    email: EmailStr
    registration: datetime | None
    color: Literal['red', 'green', 'blue'] = 'red',
    weight: Annotated[float, Gt(0), Le(200)]
    props: dict[str, list[tuple[int, bool, float]]] 
    # other: StringConstraints.pattern("[a-z]+$")
    # address: Optional[str]

    # @pydantic.field_validator('name')
    # @classmethod
    # def check_name(cls, value):
    #     print("Validating name")
    #     if value is None:
    #         raise ValueError('name cannot be None')
    #     return value

def main() -> None:
    
    try:
        user1 = User(id=1, age=30, name="GT", email="john@example.com", registration='2020-01-02T03:04:05Z',
                     weight=80, props={"foobar" : [(1, True, 0.1)]})
        
        print(user1.model_dump())
        #print(user1.model_dump(mode="json", include="color", exclude_unset=True, exclude_defaults=True, exclude_none=True))
        #print(user1.model_dump_json())
        # user1.id
        # user1.name
        # user1.age

        # Generates JSON Schema version 2020-12 - the latest version compatible with OpenAPI 3.1
        #print(user1.model_json_schema())

        # user1.model_validate(...)
        # user1.model_validate_json("", strict=True))
        
    except ValidationError as e:
        print(f"Pydantic validation failed: {e}")

if __name__ == "__main__":
    main()