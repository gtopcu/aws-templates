
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from pydantic.alias_generators import to_camel, to_pascal, to_snake

# To enable us to match the graphQL schema's casing (companyId), the base model is configured with a camelCase serializer.
# For data sent from the (graphQL) resolvers, convert all Pydantic models to dicts using:
# Model.model_dump(mode='json', by_alias=True, exclude_none=True)
#
# For storage in dynamodb however, we want to stick to the backend's field naming conventions and convert models to dicts using:
# Model.model_dump(mode='json', exclude_none=True)

class ParentModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, extra='allow') # default forbid, allow, ignore

    @classmethod
    def get_field_names(cls, alias=False) -> list[str]:
        return list(cls.model_json_schema(by_alias=alias).get("properties").keys())


class MyModel(ParentModel):
    name: str
    # company_id: str = Field(frozen=True)

if __name__ == "__main__":
    kwargs = { "name":"gokhan", "age": 40 }
    model = MyModel(**kwargs)
    print(model)
