
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from pydantic.alias_generators import to_camel, to_pascal, to_snake


# To enable us to match the graphQL schema's casing (otherwise it looks funny and will also give end users a lot of
# linting pains), the base model is configured with a camelCase serializer.
#
# As such, for data sent from the (graphQL) resolvers we want to convert all Pydantic models to dicts using:
# Model.model_dump(mode='json', by_alias=True, exclude_none=True)
#
# For storage in dynamodb however, we want to stick to the backend's field naming conventions.
# As such it should be converted to dicts using:
# Model.model_dump(mode='json', exclude_none=True)

class ParentModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @classmethod
    def get_field_names(cls, alias=False) -> list[str]:
        return list(cls.model_json_schema(alias).get("properties").keys())


class ViewModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @classmethod
    def get_field_names(cls, alias=False) -> list[str]:
        return list(cls.model_json_schema(alias).get("properties").keys())
