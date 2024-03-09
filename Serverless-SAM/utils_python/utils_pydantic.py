
"""
https://docs.pydantic.dev/latest/
https://www.youtube.com/watch?v=502XOB0u8OY


BaseModel — Pydantic's own super class with many common utilities available via instance methods
pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized

pydantic = {extras = ["email"], version = "^2.6.1"}
"""
from datetime import datetime
from typing import Any, Optional, TypedDict, Self
# from typing import Dict, List, Tuple
from typing import Literal, Annotated
from annotated_types import Gt, Ge, Le, Lt
from uuid import uuid4, UUID4
from enum import auto, IntFlag
import re

import pydantic
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    EmailStr,
    SecretStr,
    StrictInt,
    PositiveInt,
    StringConstraints
    #AwareDatetime
)
class Role(IntFlag):
    AUTHOR = auto()
    EDITOR = auto()
    VIEWER = auto()
    ADMIN = AUTHOR | EDITOR | VIEWER

NAME_REGEX = re.compile(r"^[a-zA-Z]+$")

class User(BaseModel):
    model_config={
        "strict": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "coerce_numbers_to_str": False,
        "allow_inf_nan": False,
        "str_to_lower": False
    }
    uuid: UUID4 = Field(default_factory=uuid4) #"12345678-1234-1234-1234-123456789012"
    other_uuids: list[UUID4] = Field(default_factory=list)
    id_: Optional[int] = Field(alias="id", default=None, strict=True, frozen=True, kw_only=False)
    name: Optional[str] = "default"
    age: PositiveInt
    email: EmailStr | None
    birthday: datetime = Field(default_factory=datetime.now)
    color: Literal['red', 'green', 'blue'] = 'red',
    weight: Annotated[float, Gt(0), Le(200)]
    props: dict[str, list[tuple[int, bool, float]]] 
    address: str = Field(examples=["Istanbul", "Ankara"], description="home address")
    password: SecretStr = Field(exclude=True)
    role: Role = Field(default=Role.EDITOR, validate_default=True)
    regex_attr: StringConstraints(to_lower=True, strict=True, min_length=1, max_length=10, pattern=NAME_REGEX)
    other_attributes: dict[str, Any] = {}
    # other: StringConstraints.pattern("[a-z]+$")

    # @pydantic.field_validator('name', mode="before", check_fields=True)
    # @classmethod
    # def check_name(cls, value: int | str | Role):
    #     print("Validating name")
    #     if value is None:
    #         raise ValueError('name cannot be None')
    #     return value

    # @pydantic.field_validator('age', mode="after")
    # @classmethod
    # def check_name(cls, value):
    #     can now use self.

    @pydantic.model_validator(mode="before")
    @classmethod
    def validate_user(cls, values: dict[str, Any]) -> dict[str, Any]:
        if "name" not in values:
            raise ValueError("name is required")
        if "name".casefold() != "john":
            raise ValueError("name must be John")
    
    @pydantic.field_serializer("role", when_used="json") #always
    @classmethod
    def serialize_role(self, value: Role) -> str:
        return value.name

    @pydantic.model_serializer(mode="wrap", when_used="always") #mode="plain"
    def serialize_user(self, serializer, info) -> dict[str, Any]:
        if not info.include and not info.exclude:
            return {"name": self.name.lower()}
        return serializer(self)

def main() -> None:
    
    try:
        user1 = User(id=1, age=30, name="GT", email="john@example.com", birthday='2020-01-02T03:04:05Z',
                     weight=80, props={"foobar" : [(1, True, 0.1)]})
        
        # print(user1.model_dump())
        # print(user1.model_dump(mode="json", include="color", exclude="address",
        #                       exclude_unset=True, exclude_defaults=True, exclude_none=True))
        # print(user1.model_dump_json())
        # user1.id
        # user1.name
        # user1.age

        # Generates JSON Schema version 2020-12 - the latest version compatible with OpenAPI 3.1
        #print(user1.model_json_schema())

        user2 = User.model_validate(user1)
        # user3 = User.model_validate_json("", strict=True)
        
        print("Done")

    except pydantic.ValidationError as e:
        print(f"Pydantic validation failed: {e}")

def validate(data: dict[str, Any]) -> None:
    try:
        user = User.model_validate(data)
        print(user)
    except pydantic.ValidationError as e:
        # print(f"Pydantic validation failed: {e}")
        print("Validation failed: ")
        for error in e.errors():
            print(error)

if __name__ == "__main__":
    main()