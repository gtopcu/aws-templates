# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/metrics/#creating-metrics
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricResolution, MetricUnit
from aws_lambda_powertools.utilities.typing import LambdaContext

import os
from uuid import uuid4
import pytest

metrics = Metrics()
STAGE = os.getenv("STAGE", "dev")
metrics.set_default_dimensions(environment=STAGE)


# Metrics are flushed upon request completion/failure
@metrics.log_metrics(capture_cold_start_metric=True, 
                     raise_on_empty_metrics=True)  
def lambda_handler(event: dict, context: LambdaContext):
    
    # High resolution -> 1 sec
    metrics.add_metric(name="SuccessfulBooking", unit=MetricUnit.Count, value=1, resolution=MetricResolution.High)
    # High resolution -> up to 60 secs
    metrics.add_metric(name="SuccessfulBooking", unit=MetricUnit.Count, value=1, resolution=5)

    #metrics.add_dimension(name="environment", value=STAGE)
    metrics.add_metric(name="TurbineReads", unit=MetricUnit.Count, value=1)
    metrics.add_metric(name="TurbineReads", unit=MetricUnit.Count, value=8)

    metrics.add_metadata(key="booking_id", value=f"{uuid4()}")


# @pytest.fixture(scope="function", autouse=True)
# def reset_metric_set():
#     # Clear out every metric data prior to every test
#     metrics = Metrics()
#     metrics.clear_metrics()
#     cold_start.is_cold_start = True  # ensure each test has cold start
#     metrics.clear_default_dimensions()  # remove persisted default dimensions, if any
#     yield


