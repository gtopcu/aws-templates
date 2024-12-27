
"""
https://docs.pydantic.dev/latest/
https://www.youtube.com/watch?v=502XOB0u8OY


BaseModel — Pydantic's own super class with many common utilities available via instance methods
pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized

pip install -U pydantic 
pip install -U email_validator
pydantic[email]
pydantic = {extras = ["email"], version = "^2.6.1"}

OpenAPI/JSON/YAML/CSV/GraphQL/Dict to Pydantic:
https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/

Model Usage:
https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage

ORM Mode:
https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances

"""
from datetime import datetime
from typing import Any, Optional, TypedDict, Self
# from typing import Dict, List, Tuple
from typing import Literal, Annotated
from annotated_types import Gt, Ge, Le, Lt
from uuid import uuid4, UUID
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
    StringConstraints,
    HttpUrl
    #AwareDatetime
)

# ----------------------------------------------------------------------------------------------------
class Item(BaseModel):
    name: str

class MyData(BaseModel):
    name: str = Field(min_length=1, max_length=10, description="Full Name")
    age: int = Field(ge=0, le=100)
    email: EmailStr | None = None
    url: HttpUrl | None = Field(default=None, alias="url_alias")
    uuid: UUID = Field(default_factory=uuid4)
    size: Optional[float] = None
    # items: list[Item]
    creation_date: datetime = Field(default_factory=datetime.now, description="Record creation timestamp")

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.email} {self.url} {self.uuid} {self.creation_date}"

    @pydantic.field_validator('name')
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

try: 
    my_data = MyData(name="John", age=30, email="john@example.com", url="https://example.com")
    print(my_data.model_dump_json())
    # my_data.model_dump()
    # MyData.model_validate_json()
    # MyData.model_validate_strings()
    # MyData.model_validate()
    # MyData.model_construct() - no validation
    # my_data.model_rebuild()
except pydantic.ValidationError as e:
    print("Pydantic validation failed: " + str(e))

# ----------------------------------------------------------------------------------------------------

# class Role(IntFlag):
#     AUTHOR = auto()
#     EDITOR = auto()
#     VIEWER = auto()
#     ADMIN = AUTHOR | EDITOR | VIEWER

# NAME_REGEX = re.compile(r"^[a-zA-Z]+$")

# class User(BaseModel):
#     model_config={
#         "strict": True,
#         "extra": "forbid",
#         "str_strip_whitespace": True,
#         "coerce_numbers_to_str": False,
#         "allow_inf_nan": False,
#         "str_to_lower": False
#     }
#     uuid: UUID = Field(default_factory=uuid4) #"12345678-1234-1234-1234-123456789012"
# #   user_id: str = Field(default_factory=lambda: f"{uuid4()}")
#     other_uuids: list[UUID] = Field(default_factory=list)
#     id_: int = Field(alias="id", default=None, gt=0, strict=True, frozen=True, kw_only=False)
#     name: str = "default"
#     last_name: str = Field(exclude=True, pattern=NAME_REGEX)
#     age: PositiveInt
#     email: EmailStr | None
#     title: str | None = Field(default="Mr.", min_length=1, max_length=10)
#     birthday: datetime = Field(default_factory=datetime.now)
#     color: Literal['red', 'green', 'blue'] = 'red',
#     weight: Annotated[float, Gt(0), Le(200)]
#     props: dict[str, list[tuple[int, bool, float]]] 
#     address: str = Field(examples=["Istanbul", "Ankara"], description="home address")
#     password: SecretStr = Field(exclude=True)
#     role: Role = Field(default=Role.EDITOR, validate_default=True)
#     regex_attr: StringConstraints(to_lower=True, strict=True, min_length=1, max_length=10, pattern=NAME_REGEX)
#     other_attributes: dict[str, Any] = {}
#     # other: StringConstraints.pattern("[a-z]+$")

#     # @pydantic.field_validator('name', mode="before", check_fields=True)
#     # @classmethod
#     # def check_name(cls, value: int | str | Role):
#     #     print("Validating name")
#     #     if value is None:
#     #         raise ValueError('name cannot be None')
#     #     return value

#     # @pydantic.field_validator('age', mode="after")
#     # @classmethod
#     # def check_name(cls, value):
#     #     can now use self.

#     @pydantic.model_validator(mode="before")
#     @classmethod
#     def validate_user(cls, values: dict[str, Any]) -> dict[str, Any]:
#         if "name" not in values:
#             raise ValueError("name is required")
#         if "name".casefold() != "john":
#             raise ValueError("name must be John")
    
#     # @pydantic.model_validator(mode="before")
#     # @classmethod
#     # def transform_body_to_dict(cls, value: str):
#     #     return json.loads(value)
    
#     @pydantic.field_serializer("role", when_used="json") #always
#     @classmethod
#     def serialize_role(self, value: Role) -> str:
#         return value.name

#     @pydantic.model_serializer(mode="wrap", when_used="always") #mode="plain"
#     def serialize_user(self, serializer, info) -> dict[str, Any]:
#         if not info.include and not info.exclude:
#             return {"name": self.name.lower()}
#         return serializer(self)

   

# def main() -> None:
    
#     try:
        # user1 = User(id=1, age=30, name="GT", email="john@example.com", birthday='2020-01-02T03:04:05Z',
        #              weight=80, props={"foobar" : [(1, True, 0.1)]})
        
        # print(user1.model_dump())
        # print(user1.model_dump(mode="json", include="color", exclude="address",
        #                       exclude_unset=True, exclude_defaults=True, exclude_none=True))
        # print(user1.model_dump_json())
        # user1.id
        # user1.name
        # user1.age

        # Generates JSON Schema version 2020-12 - the latest version compatible with OpenAPI 3.1
        #print(user1.model_json_schema())

        # user2 = User.model_validate(user1)
        # user3 = User.model_validate_json("", strict=True)
        
    #     print("Done")

    # except pydantic.ValidationError as e:
    #     print(f"Pydantic validation failed: {e}")

# def validate(data: dict[str, Any]) -> None:
#     try:
#         user = User.model_validate(data)
#         print(user)
#     except pydantic.ValidationError as e:
#         # print(f"Pydantic validation failed: {e}")
#         print("Validation failed: ")
#         for error in e.errors():
#             print(error)

# if __name__ == "__main__":
#     main()