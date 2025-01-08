
"""
https://docs.pydantic.dev/latest/
https://www.youtube.com/watch?v=502XOB0u8OY


BaseModel — Pydantic's own super class with many common utilities available via instance methods
pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized

pip install -U pydantic 
pip install -U email_validator
pydantic[email]
pydantic = {extras = ["email"], version = "^2.6.1"}

DevTools -> debug(my_model)
https://docs.pydantic.dev/latest/integrations/devtools/
pip install devtools
from devtools import debug
debug(my_model)

OpenAPI/JSON/YAML/CSV/GraphQL/Dict to Pydantic:
https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/

Model Usage:
https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage

ORM Mode:
https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances

Pydantic Settings:
https://docs.pydantic.dev/latest/api/pydantic_settings/

Pydantic Types:
https://docs.pydantic.dev/dev/api/types/#pydantic.types

Pydantic Lambda:
https://docs.pydantic.dev/latest/integrations/aws_lambda/
https://pydantic.dev/articles/lambda-intro


"""

from datetime import datetime, timezone
import time
from typing import Any, Optional, TypedDict, Self
# from typing import Dict, List, Tuple
from typing import Literal, Annotated
from annotated_types import Gt, Ge, Le, Lt
# from typing_extensions import Annotated, Gt, Ge, Le, Lt
from uuid import uuid4, UUID
from enum import auto, IntFlag
import re

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    ValidationError,
    ConfigDict,
    ValidationInfo,
    computed_field,
    Json,
    EmailStr,
    StrictInt,
    PositiveInt,
    NegativeInt,
    PositiveFloat,
    NegativeFloat,
    NonNegativeInt,     # An integer that must be greater than or equal to zero
    NonNegativeFloat,   # A float that must be greater than or equal to zero
    NonPositiveInt,     # An integer that must be less than or equal to zero
    NonPositiveFloat,   # A float that must be less than or equal to zero
    StringConstraints,
    HttpUrl,
    PastDate,
    FutureDate,
    PastDatetime,
    FutureDatetime,
    AwareDatetime,      # A datetime that requires timezone info
    NaiveDatetime,      # A datetime that doesn't require timezone info
    Secret,
    SecretStr,
    Base64Str,
    UUID4,

)

# ----------------------------------------------------------------------------------------------------

# https://github.com/boto/boto3/issues/665#issuecomment-340260257
from decimal import Decimal, getcontext, setcontext, ExtendedContext
setcontext(ExtendedContext)
getcontext().prec = 2
# round(Decimal(1.2345), 2)

# https://github.com/pydantic/pydantic/issues/8006
# Do not use Optional[str] = None, use str | None = None instead
# model_dump with exclude_defaults=True or exclude_none=Truev

# VSCode Settings -> Type Checking Mode

# ----------------------------------------------------------------------------------------------------
# Validating JSON fields:
class Order(BaseModel):
    order_id: int
    reason: str
class OrderModel(BaseModel):
    body: Json[Order]
# {
#     "body": "{\"order_id\": 12345, \"reason\": \"Changed my mind\"}"
# }
# ----------------------------------------------------------------------------------------------------

class Person(BaseModel):
    id: str = Field(min_length=1, max_length=50, description="Employee ID")
    # uuid: UUID = Field(default_factory=uuid4, description="Unique ID", examples=["12345678-1234-1234-1234-123456789012"])
    name: str = Field(min_length=1, max_length=100, description="Full Name")
    age: int | None = Field(default=None, ge=0, le=100, description="Age in years")
    # birthday: PastDate | None
    address: str | None = Field(default=None, min_length=1, max_length=200, description="Address")
    email: EmailStr | None = Field(default=None, description="Email address")
    url: HttpUrl | None = Field(default=None, alias="url_alias")
    money: Decimal = Field(default=Decimal(0), ge=Decimal(0), description="Money in USD") 
    # money: float = Field(default=0, decimal_places=2, ge=0, description="Money in USD") 
    # hobbies: list[str] | None = None
    # items: list[Item] # 
    # created: datetime = Field(default_factory=datetime.now, description="Record creation timestamp", serialization_alias="creationDate")
    # created: str = Field(default=str(time.strftime("%Y-%m-%dT%H:%M:%S")), description="Record creation date")
    # created: str = Field(default=str(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")), description="Record creation date")
    # expiry: int = Field(default=0, description="Record expiry timestamp - dynamo TTL")

    # @computed_field
    # @property
    # def age(self) -> int: 
    #     return (date.today() - self.birthday).days // 365

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.address} {self.creation_date}"

    # You must raise either ValueError, TypeError, or AssertionError
    # @field_validator("name")
    # def name_not_empty(cls, v):
    #     if not v.strip():
    #         raise ValueError("name cannot be empty")
    #     return v.strip()

    # You must raise either ValueError, TypeError, or AssertionError
    # @model_validator(mode="after")  
    # def check_id_uuid(cls, values):
    #     id, uuid = values.get("id"), values.get("uuid")
    #     if id is not None and uuid is not None and id != uuid:
    #         raise ValueError("id and uuid should match")
    #     return values

    # @field_serializer("money", when_used="json")
    # def serialize_money(self, money: Decimal) -> str:
    #     return str(money)


try: 
    my_data = Person(id="1", name="John", age=30, email="john@example.com")# , url_alias="example.com") 
    print(my_data.model_dump_json(exclude_none=True)) # https://github.com/pydantic/pydantic/issues/8006
    # my_data.model_dump()
    my_data.model_dump(mode="json") # or python
    # MyData.model_validate_json()
    # MyData.model_validate_strings()
    # MyData.model_validate()
    # MyData.model_construct() - no validation
    # my_data.model_rebuild()
    # devtools.debug(my_model)

except ValidationError as e:
    print("Pydantic validation failed: " + str(e))
    #return {"result": "error", "message": e.errors(include_url=False, include_context=True, include_input=True)}
        

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