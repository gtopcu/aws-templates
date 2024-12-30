
# Available as of Powertools 3.4.0
# https://github.com/aws-powertools/powertools-lambda-python/releases/tag/v3.4.0

# APIGatewayWebSocketMessageEventModel - For WebSocket messages events
# APIGatewayWebSocketConnectEventModel - For WebSocket $connect events
# APIGatewayWebSocketDisconnectEventModel - For WebSocket $disconnect events

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.parser import event_parser
from aws_lambda_powertools.utilities.parser.models import (
    # APIGatewayWebSocketConnectEventModel,
    # APIGatewayWebSocketDisconnectEventModel,
    # APIGatewayWebSocketConnectEventRequestContext,
    # APIGatewayWebSocketDisconnectEventRequestContext,
    # APIGatewayWebSocketEventIdentity,
    # APIGatewayWebSocketEventRequestContextBase,
    APIGatewayWebSocketMessageEventModel,
    # APIGatewayWebSocketMessageEventRequestContext
)
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(log_uncaught_exceptions=True, serialize_stacktrace=True)

@event_parser()
def lambda_handler(event: APIGatewayWebSocketMessageEventModel, context:LambdaContext):
    logger.info(event.request_context.domain_name)
    logger.info(event.request_context.api_id)
    logger.info(event.request_context.connection_id)
    logger.info(event.request_context.connected_at)
    logger.info(event.request_context.extended_request_id)
    logger.info(event.request_context.event_type)
    logger.info(event.request_context.message_direction)
    logger.info(event.request_context.identity)
    logger.info(event)
    logger.info(event.body)
    


    
    
    





