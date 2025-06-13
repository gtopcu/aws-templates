
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.utilities.data_classes import AppSyncResolverEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer(service="sample_resolver")
logger = Logger(service="sample_resolver")
app = AppSyncResolver()


class MyCustomModel(AppSyncResolverEvent):
    @property
    def country_viewer(self) -> str:
        return self.request_headers.get("cloudfront-viewer-country", "")


@app.resolver(field_name="createSomething")
def create_something(id: str):  
    return id

@app.resolver(field_name="listLocations")
@app.resolver(field_name="locations")
def get_locations(name: str, description: str = ""):
    if app.current_event.country_viewer == "US":
        ...
    return name + description


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
@tracer.capture_lambda_handler
def lambda_handler(event, context:LambdaContext):
    return app.resolve(event, context, data_model=MyCustomModel)
