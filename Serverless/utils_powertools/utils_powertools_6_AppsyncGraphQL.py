# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/event_handler/appsync/

from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
    aws_date,
    aws_datetime,
    aws_time,
    aws_timestamp,
    make_id,
    aws_uuid,
    aws_json,
    aws_email,
    aws_url,
    aws_ip,
    aws_arn,
    aws_phone,
    aws_bytes,
    aws_base64,
    aws_enum,
    aws_any,
    aws_json_string,
    aws_json_object,
    aws_json_array,
    _formatted_time,
     _formatted_datetime,
     _formatted_date,
)

# Scalars: https://docs.aws.amazon.com/appsync/latest/devguide/scalars.html

my_id: str = make_id()  # Scalar: ID
my_date: str = aws_date()  # Scalar: AWSDate
my_timestamp: str = aws_time()  # Scalar: AWSTime
my_datetime: str = aws_datetime()  # Scalar: AWSDateTime
my_epoch_timestamp: int = aws_timestamp()  # Scalar: AWSTimestamp

import sys
from typing import TypedDict

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
def get_locations(name: str, description: str = "") -> list[Location]:  # match GraphQL Query arguments
    return [{"name": name, "description": description}]


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)




# from typing import Optional
# from uuid import uuid4

# from aws_lambda_powertools import Logger, Tracer
# from aws_lambda_powertools.event_handler import AppSyncResolver
# from aws_lambda_powertools.logging import correlation_paths
# from aws_lambda_powertools.utilities.data_classes import AppSyncResolverEvent
# from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
#     aws_datetime,
# )
# from aws_lambda_powertools.utilities.typing import LambdaContext


# tracer = Tracer()
# logger = Logger()
# app = AppSyncResolver()

# class CompanyEventModel(AppSyncResolverEvent):
#     @property
#     def company_id(self) -> str:
#         return self.identity.get("claims")["custom:company_id"]


# @app.resolver(type_name="Mutation", field_name="createNotification")
# @tracer.capture_method
# def create_notification_resolver(
#     companyId: str,
#     notificationType: str,
#     facilityId: Optional[str] = None,
#     sourceId: Optional[str] = None,
#     fileName: Optional[str] = None,
#     message: Optional[str] = None,
# ) -> dict:
#     notification_type = NotificationType(notificationType)
#     notification = UserNotification(
#         company_id=companyId,
#         notification_id=str(uuid4()),
#         notification_type=notification_type,
#         creation_datetime=aws_datetime(),
#         facility_id=facilityId,
#         source_id=sourceId,
#         file_name=fileName,
#         message=message,
#     )
#     get_notification_repository().save_notification(notification)

#     return notification.model_dump(mode="json", by_alias=True)


# @app.resolver(type_name="Mutation", field_name="markNotificationAsRead")
# @tracer.capture_method
# def mark_notification_as_read_resolver(
#     notificationId: str,
#     companyId: Optional[str] = None,
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")
#         get_notification_repository().update_notification_status(
#             company_id=company_id,
#             notification_id=notificationId,
#             notification_status=NotificationStatus.READ,
#         )
#     except Exception as e:
#         logger.exception(e)
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "UPDATED"}


# @app.resolver(type_name="Mutation", field_name="deleteNotification")
# @tracer.capture_method
# def delete_notification_resolver(
#     notificationId: str,
#     companyId: Optional[str] = None,
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")
#         get_notification_repository().delete_notification(
#             company_id=company_id,
#             notification_id=notificationId,
#         )
#     except Exception as e:
#         logger.exception(e)
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "DELETED"}


# @app.resolver(type_name="Query", field_name="getNotifications")
# @tracer.capture_method
# def get_notifications_resolver(
#     companyId: Optional[str] = None,
#     limit: Optional[int] = None,
#     cursor: Optional[str] = None,
#     sortOrder: Optional[str] = None,
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")
#         notification_page = get_notification_repository().get_notifications(
#             company_id=company_id,
#             limit=limit,
#             cursor=cursor,
#             sort_order=SortOrder.DESC if sortOrder == "DESC" else None,
#         )
#     except Exception as e:
#         logger.exception(e)
#         raise
#     else:
#         return notification_page.model_dump(mode="json", by_alias=True)


# @logger.inject_lambda_context(
#     correlation_id_path=correlation_paths.APPSYNC_RESOLVER, log_event=True
# )
# @tracer.capture_lambda_handler
# def lambda_handler(event: dict, context: LambdaContext) -> dict:
#     return app.resolve(event, context, data_model=CompanyEventModel)


# def _return_failure(exception: Exception):
#     logger.exception(exception)
#     return {
#         "message": "FAILED",
#         "success": False,
#         "errorDetails": {
#             "errorType": type(exception).__name__,
#             "errorMessage": str(exception),
#         },
#     }
