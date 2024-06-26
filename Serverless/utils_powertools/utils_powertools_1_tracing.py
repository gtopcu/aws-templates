
#https://docs.powertools.aws.dev/lambda/python/2.29.1/core/tracer/#annotations-metadata
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer()
#tracer = Tracer(service="example")

@tracer.capture_method(capture_response=False, capture_error=False)
def collect_payment(charge_id: str) -> str:
    tracer.put_annotation(key="PaymentId", value=charge_id)
    return f"dummy payment collected for charge: {charge_id}"


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> str:
    charge_id = event.get("charge_id", "")
    return collect_payment(charge_id=charge_id)