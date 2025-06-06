from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.batch import (
    BatchProcessor,
    EventType,
    process_partial_response,
)
from aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event import (
    DynamoDBRecord,
    DynamoDBRecordEventName,
)
from aws_lambda_powertools.utilities.typing import LambdaContext

processor = BatchProcessor(event_type=EventType.DynamoDBStreams)
tracer = Tracer()
logger = Logger()


def record_handler(record: DynamoDBRecord):
    match record.event_name:
        case DynamoDBRecordEventName.INSERT:
            # handle_insert_event(record.dynamodb.new_image)
            # source_id = new_image.get('source_id')
        case DynamoDBRecordEventName.MODIFY:
            # handle_modify_event(record.dynamodb.old_image, record.dynamodb.new_image)
        case DynamoDBRecordEventName.REMOVE:
            # handle_remove_event(record.dynamodb.old_image)
        case _:
            logger.error("Unknown event type. Not insert, modify or remove.")


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext):
    return process_partial_response(
        event=event, record_handler=record_handler, processor=processor, context=context
    )
