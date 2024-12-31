
from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    field_serializer,
    computed_field,
    ValidationInfo,
    ValidationError,
    EmailStr,
    SecretStr,
    StrictInt,
    PositiveInt,
    StringConstraints,
    HttpUrl,
    PastDate,
    FutureDate,
    PastDatetime,
    FutureDatetime,
    #AwareDatetime
)
from typing import Literal, Annotated
from annotated_types import Gt, Ge, Le, Lt
from uuid import uuid4, UUID
from datetime import datetime, timezone
import time

# https://github.com/boto/boto3/issues/665#issuecomment-340260257
from decimal import Decimal, getcontext, setcontext, ExtendedContext
setcontext(ExtendedContext)
getcontext().prec = 2

# https://github.com/pydantic/pydantic/issues/8006
# Do not use Optional[str] = None, use str | None = None instead
# model_dump with exclude_defaults=True or exclude_none=True

# https://pydantic.dev/articles/lambda-intro

class Person(BaseModel):
    id: str = Field(min_length=1, max_length=50, description="Employee ID")
    # uuid: UUID = Field(default_factory=uuid4, description="Unique ID", examples=["12345678-1234-1234-1234-123456789012"])
    name: str = Field(min_length=1, max_length=100, description="Full Name")
    age: int | None = Field(default=None, ge=0, le=100, description="Age in years")
    # birthday: PastDate | None
    address: str | None = Field(default=None, min_length=1, max_length=200, description="Address")
    # email: EmailStr | None = Field(default=None, description="Email address")
    # url: HttpUrl | None = Field(default=None, alias="url_alias")
    money: Decimal = Field(default=Decimal(0), ge=Decimal(0), description="Money in USD") 
    # money: float = Field(default=0, decimal_places=2, ge=0, description="Money in USD") 
    hobbies: list[str] | None = None
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

# try: 
#     my_data = Person(name="John", age=30, email="john@example.com", url="https://example.com")
#     print(my_data.model_dump_json(exclude_none=True)) # https://github.com/pydantic/pydantic/issues/8006
#     # my_data.model_dump()
#     # MyData.model_validate_json()
#     # MyData.model_validate_strings()
#     # MyData.model_validate()
#     # MyData.model_construct() - no validation
#     # my_data.model_rebuild()
# except ValidationError as e:
#     print("Pydantic validation failed: " + str(e))
#     return {"result": "error", "message": e.errors(include_url=False, include_context=True, include_input=True)}
