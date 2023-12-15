# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/event_handler/appsync/

from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
    aws_date,
    aws_datetime,
    aws_time,
    aws_timestamp,
    make_id,
)

# Scalars: https://docs.aws.amazon.com/appsync/latest/devguide/scalars.html

my_id: str = make_id()  # Scalar: ID
my_date: str = aws_date()  # Scalar: AWSDate
my_timestamp: str = aws_time()  # Scalar: AWSTime
my_datetime: str = aws_datetime()  # Scalar: AWSDateTime
my_epoch_timestamp: int = aws_timestamp()  # Scalar: AWSTimestamp

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from typing import List

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer()
logger = Logger()
app = AppSyncResolver()


class Location(TypedDict, total=False):
    id: str  # noqa AA03 VNE003, required due to GraphQL Schema
    name: str
    description: str
    address: str


@app.resolver(field_name="listLocations")
@app.resolver(field_name="locations")
@tracer.capture_method
def get_locations(name: str, description: str = "") -> List[Location]:  # match GraphQL Query arguments
    return [{"name": name, "description": description}]


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)




