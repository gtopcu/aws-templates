# https://docs.powertools.aws.dev/lambda/python/2.29.1/core/event_handler/appsync/

from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
    make_id,
    aws_date,
    aws_datetime,
    aws_time,
    aws_timestamp,
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

import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.utilities.data_classes import AppSyncResolverEvent
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths

from typing import TypedDict

tracer = Tracer()
logger = Logger()
app = AppSyncResolver()


tracer = Tracer(service="sample_resolver")
logger = Logger(service="sample_resolver")
app = AppSyncResolver()

# "identity": {
#     "claims": {
#         "sub": "e6e252d4-60b1-7013-3a41-92bffafb6541",
#         "cognito:groups": [
#             "admin"
#         ],
#         "email_verified": true,
#         "custom:position": "Admin",
#         "iss": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_b1bClh7oA",
#         "cognito:username": "e6e25sd4-60b1-7013-3a41-92bffafb6141",
#         "custom:company_id": "45beb454-710f-4e5b-aaaf-cf5b29c4c108",
#         "origin_jti": "326e9178-b1f5-4214-b6f5-741f1b2e12c7",
#         "cognito:roles": [
#             "arn:aws:iam::012345678901:role/api-authenticated-role"
#         ],
#         "aud": "qvhp5vg1lde5pmt7sue34p1dt",
#         "event_id": "3eeb2c3a-3523-4b58-bf11-857b28433940",
#         "token_use": "id",
#         "auth_time": 1749724451,
#         "exp": 1749738055,
#         "iat": 1749734455,
#         "jti": "c9a5cab6-5fb0-46d3-be3c-8aa3a6c49796",
#         "email": "gtopcu@gmail.com"
#     },
#     "defaultAuthStrategy": "ALLOW",
#     "groups": [
#         "admin"
#     ],
#     "issuer": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_y1gClh7oA",
#     "sourceIp": [
#         "104.28.96.62"
#     ],
#     "sub": "e6e252d4-60b1-7013-3a41-92bffafb6541",
#     "username": "e6e252d4-60b1-7013-3a41-92bffafb6541"
# },


class CustomEventModel(AppSyncResolverEvent):
    @property
    def country_viewer(self) -> str:
        return self.request_headers.get("cloudfront-viewer-country", "")
    @property
    def company_id(self) -> str | None:
        return self.identity.get("claims", {}).get("custom:company_id")
    @property
    def email(self) -> str | None:
        return self.identity.get("claims", {}).get("email")
    @property
    def given_name(self) -> str | None:
        return self.identity.get("claims", {}).get("given_name")
    @property
    def family_name(self) -> str | None:
        return self.identity.get("claims", {}).get("family_name")


class Location(TypedDict, total=False):
    id: str  # required due to GraphQL Schema
    name: str
    description: str
    address: str

@app.resolver(field_name="createLocation")
def create_location(id: str) -> dict:  
    app.current_event.domain_name
    app.current_event.request_headers
    app.current_event.raw_event
    app.current_event.identity
    app.current_event.arguments
    app.current_event.field_name
    app.current_event.get
    app.current_event.items
    app.current_event.keys
    app.current_event.values
    app.current_event.company_id

    return { "id": id }

@app.resolver(field_name="listLocations")
@app.resolver(field_name="locations")
@tracer.capture_method
def get_locations(name: str, description: str = "") -> list[Location]:  # match GraphQL Query arguments

    if app.current_event.country_viewer == "US":
        ...
    try:
        pass
    except ValueError as e:
        logger.error(f"Validation Error: {e}")
        raise
    except Exception as e:
        logger.exception(f"Error getting data requests: {e}")
        raise

    return [{"name": name, "description": description}]


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER, log_event=False)
@tracer.capture_lambda_handler
def lambda_handler(event, context:LambdaContext) -> dict:
    identity = event.get("identity")
    if identity and identity.get("claims"):
        claims = identity.get("claims")
        company_id = claims.get("custom:company_id")
        cognito_user = claims.get("cognito:username")

        logger.append_keys(
            company_id=company_id,
            cognito_user=cognito_user,
        )
    return app.resolve(event, context, data_model=CustomEventModel)


# -----------------------------------------------------------------------------------------------------------

# from uuid import uuid4

# class CompanyEventModel(AppSyncResolverEvent):
#     @property
#     def company_id(self) -> str:
#         return self.identity.get("claims")["custom:company_id"]

# @app.resolver(type_name="Mutation", field_name="createNotification")
# @tracer.capture_method
# def create_notification_resolver(
#     companyId: str,
#     notificationType: str,
#     facilityId: str | None = None,
#     sourceId: str | None = None,
#     fileName: str | None = None,
#     message: str | None = None,
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
#     companyId: str | None = None,
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
#     companyId: str | None = None,
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
#     companyId: str | None = None,
#     limit: int | None = None,
#     cursor: str | None = None,
#     sortOrder: str | None = None,
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


# @logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER, log_event=False)
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
