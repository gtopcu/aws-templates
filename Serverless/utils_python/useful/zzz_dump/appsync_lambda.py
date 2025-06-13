# from datetime import date, datetime
# import boto3
# from botocore.exceptions import ClientError

# from aws_lambda_powertools import Logger, Tracer
# from aws_lambda_powertools.event_handler import AppSyncResolver
# from aws_lambda_powertools.logging import correlation_paths
# from aws_lambda_powertools.utilities.data_classes import AppSyncResolverEvent
# from aws_lambda_powertools.utilities.typing import LambdaContext

# from generate_email_body import generate_email_body
# from secr.domain.model.enums import DataRequestStatus
# from secr.domain.model.supplier import DataRequest,  SupplierData
# from secr.repository.aurora.supplier_data_repository.supplier_data_repository import (
#     get_supplier_data_item_repository,
# )
# from secr.repository.aurora.supplier_data_repository.supplier_data_request_repository import (
#     get_supplier_data_request_repository,
# )
# from secr.repository.dynamodb.dd_company_repository import get_company_repository
# from secr.repository.dynamodb.dd_questionnaire_repository import (
#     get_questionnaire_repository,
# )

# # Initialize AWS services and utilities outside the handler
# session = boto3.Session()
# ses_client = session.client('ses', region_name='eu-west-2')

# tracer = Tracer()
# logger = Logger()
# app = AppSyncResolver()

# # Constants for email configuration
# DEFAULT_SENDER_EMAIL = "support@climatise.com"
# EMAIL_CHARSET = 'UTF-8'


# "identity": {
#     "claims": {
#         "sub": "e6e252d4-60b1-7013-3a41-92bffafb6541",
#         "cognito:groups": [
#             "admin"
#         ],
#         "email_verified": true,
#         "custom:position": "Admin",
#         "iss": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_y1bClh7oA",
#         "cognito:username": "e6e252d4-60b1-7013-3a41-92bffafb6141",
#         "custom:company_id": "45eeb454-710f-4e5b-aaaf-cf5b29c4c108",
#         "origin_jti": "326e9478-b1f5-4214-b6f5-741f1b2e12c7",
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
#     "issuer": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_y1bClh7oA",
#     "sourceIp": [
#         "104.28.96.62"
#     ],
#     "sub": "e6e252d4-60b1-7013-3a41-92bffafb6541",
#     "username": "e6e252d4-60b1-7013-3a41-92bffafb6541"
# },

# class CompanyEventModel(AppSyncResolverEvent):
#     """
#     Represents the event model for company-related AppSync requests.
#     Provides easy access to company-specific claims from the identity context.
#     """

#     @property
#     def company_id(self) -> str | None:
#         return self.identity.get("claims", {}).get("custom:company_id")

#     @property
#     def email(self) -> str | None:
#         return self.identity.get("claims", {}).get("email")

#     @property
#     def given_name(self) -> str | None:
#         return self.identity.get("claims", {}).get("given_name")

#     @property
#     def family_name(self) -> str | None:
#         return self.identity.get("claims", {}).get("family_name")



# @app.resolver(type_name="Mutation", field_name="createDataRequest")
# @tracer.capture_method
# def create_data_request_resolver(data_request: dict) -> dict:
#     """
#     Creates a new data request.

#     Args:
#         data_request: A dictionary containing the data request details.

#     Returns:
#         A dictionary representing the created data request.
#     """
#     try:
#         # Validate mandatory fields
#         mandatory_fields = ['supplierId']
#         for field in mandatory_fields:
#             if field not in data_request:
#                 raise ValueError(f"The '{field}' field is mandatory.")

#         supplier = get_supplier_details(data_request['supplierId'])
#         if not supplier:
#             raise ValueError(f"Supplier with ID {data_request['supplierId']} not found.")
#         if not supplier.supplier_email:
#             raise ValueError(f"Supplier with ID {data_request['supplierId']} does not have an email.")

#         questionnaire_id = data_request.get('questionnaireId')
#         financial_year_id = data_request.get('financialYearId')

#         # Create a new DataRequest instance
#         new_request = DataRequest(
#             supplier_id=data_request['supplierId'],
#             status=DataRequestStatus.AWAITING_REPLY,
#             date=date.today(),
#             questionnaire_id=questionnaire_id,
#             financial_year_id=financial_year_id,
#         )

#         already_exists = False
#         if questionnaire_id:
#             already_exists = get_supplier_data_request_repository().check_data_request_exists(
#                 data_request['supplierId'], questionnaire_id
#             )

#         if not already_exists:
#             # Save using repository
#             created_request = get_supplier_data_request_repository().create_data_request(new_request)
#         else:
#             raise ValueError(
#                 f"Data Request Already Present for the Supplier ID: {data_request['supplierId']} and Questionnaire ID: {questionnaire_id}"
#             )

#         try:
#             user_name = f"{app.current_event.given_name or 'user'} {app.current_event.family_name or ''}".strip()
#         except Exception:
#             user_name = "user"

#         try:
#             company_info = get_company_repository().get_company(supplier.company_id)
#             company_name = company_info.company_name if company_info else "Company"
#         except Exception:
#             company_name = "Company"

#         email_body, subject = generate_email_body(
#             supplier,
#             mail_type=DataRequestStatus.AWAITING_REPLY,
#             company_name=company_name,
#             user_name=user_name,
#             data_request_id=str(created_request.id),
#         )

#         recipient_email = [supplier.supplier_email]
#         body_text = "Data Upload Assignment"

#         # Send the email
#         mail_send_result = send_email(
#             DEFAULT_SENDER_EMAIL, recipient_email, subject, body_text, email_body
#         )

#         response = created_request.model_dump(mode="json", by_alias=True, exclude_none=True)
#         response['id'] = str(response['id'])
#         response['date'] = response['date'].isoformat()
#         response['messageid'] = mail_send_result

#     except ValueError as ve:
#         logger.error(f"Validation Error: {ve}")
#         raise
#     except Exception as e:
#         logger.exception(f"Error creating data request: {e}")
#         raise

#     return response

# @app.resolver(type_name="Mutation", field_name="updateDataRequestStatus")
# @tracer.capture_method
# def update_data_request_status_resolver(
#     dataRequestId: str | None = None,
#     supplierId: str | None = None,
#     status: str | None = None,
# ) -> dict:
#     """
#     Updates the status of a data request.

#     Args:
#         dataRequestId: The ID of the data request.
#         supplierId: The ID of the supplier.
#         status: The new status of the data request (as a string matching DataRequestStatus).

#     Returns:
#         A dictionary representing the updated data request.
#     """
#     if not status:
#         raise ValueError("Status cannot be None or empty.")
#     if not supplierId:
#         raise ValueError("supplierId cannot be None or empty.")

#     supplier = get_supplier_details(supplierId)
#     if not supplier:
#         raise ValueError(f"Supplier with ID {supplierId} not found.")
#     if not supplier.supplier_email:
#         raise ValueError(f"Supplier with ID {supplierId} does not have an email.")

#     try:
#         try:
#             new_status = DataRequestStatus[status.upper()]  # Convert status string to enum member
#         except KeyError:
#             raise ValueError(f"Invalid status: {status}. Must be one of {[e.name for e in DataRequestStatus]}")

#         updated_request = get_supplier_data_request_repository().update_data_request_status(
#             dataRequestId, supplierId, new_status
#         )
#         if not updated_request:
#             raise ValueError(
#                 f"Data request with ID {dataRequestId} and supplier ID {supplierId} not found."
#             )

#         try:
#             user_name = f"{app.current_event.given_name or 'user'} {app.current_event.family_name or ''}".strip()
#         except Exception:
#             user_name = "user"

#         try:
#             company_info = get_company_repository().get_company(supplier.company_id)
#             company_name = company_info.company_name if company_info else "Company"
#         except Exception:
#             company_name = "Company"

#         email_body, subject = generate_email_body(
#             supplier,
#             mail_type=new_status,
#             company_name=company_name,
#             user_name=user_name,
#             data_request_id=dataRequestId,
#         )

#         recipient_email = [supplier.supplier_email]
#         body_text = f"Data Request status updated to {status.upper()}"

#         send_email(DEFAULT_SENDER_EMAIL, recipient_email, subject, body_text, email_body)

#         response = updated_request.model_dump(mode="json", by_alias=True, exclude_none=True)
#         response['id'] = str(response['id'])
#         response['date'] = response['date'].isoformat()

#         return response
#     except ValueError as ve:
#         logger.error(f"Validation Error: {ve}")
#         raise
#     except Exception as e:
#         logger.exception(f"Error updating data request status: {e}")
#         raise


# @app.resolver(type_name="Query", field_name="getDataRequest")
# @tracer.capture_method
# def get_data_request_resolver(dataRequestId: str) -> dict:
#     """
#     Retrieves a data request by its ID.

#     Args:
#         dataRequestId: The ID of the data request.

#     Returns:
#         A dictionary representing the data request.
#     """
#     try:
#         data_request = get_supplier_data_request_repository().get_data_request_by_id(dataRequestId)
#         if not data_request:
#             raise ValueError(f"Data request with ID {dataRequestId} not found.")

#         response = data_request.model_dump(mode="json", by_alias=True, exclude_none=True)
#         response['id'] = str(response['id'])

#         # Convert date from string to date object if needed
#         if isinstance(response['date'], str):
#             try:
#                 response['date'] = datetime.strptime(response['date'], '%Y-%m-%d').date() #format date string to date object
#             except ValueError:
#                 logger.error(f"Invalid date format: {response['date']}")
#                 #handle the error, for example by setting date to None, or raising the exception.
#                 raise ValueError(f"Invalid date format: {response['date']}")

#         # Ensure date is a date object before calling isoformat()
#         if isinstance(response['date'], date):
#             response['date'] = response['date'].isoformat() #format the date object.

#         # Fetch Questionnaire if questionnaire_id is present
#         if data_request.questionnaire_id:
#             questionnaire = get_questionnaire_repository().get_questionnaire_by_id(
#                 questionnaire_id=data_request.questionnaire_id
#             )
#             if questionnaire:
#                 response["questionnaire"] = questionnaire.model_dump(
#                     mode="json", by_alias=True, exclude_none=True
#                 )

#         return response
#     except ValueError as ve:
#         logger.error(f"Validation Error: {ve}")
#         raise
#     except Exception as e:
#         logger.exception(f"Error getting data request: {e}")
#         raise

# @app.resolver(type_name="Mutation", field_name="updateDataRequest")
# @tracer.capture_method
# def update_data_request_resolver(dataRequestId: str | None = None, updateRequest: dict | None = None) -> dict:
#     """
#     Updates an existing data request.

#     Args:
#         dataRequestId: The ID of the data request to update.
#         updateRequest: A dictionary containing the fields to update.

#     Returns:
#         A dictionary representing the updated data request.
#     """
#     if not dataRequestId:
#         raise ValueError("dataRequestId cannot be None or empty.")
#     if not updateRequest:
#         raise ValueError("updateRequest cannot be None or empty.")

#     try:
#         existing_request = get_supplier_data_request_repository().get_data_request_by_id(dataRequestId)
#         if not existing_request:
#             raise ValueError(f"Data request with ID {dataRequestId} not found.")

#         updated_data_request = get_supplier_data_request_repository().update_data_request(
#             dataRequestId, updateRequest
#         )

#         supplier = get_supplier_details(updated_data_request.supplier_id)
#         if not supplier:
#             raise ValueError(f"Supplier with ID {updated_data_request.supplier_id} not found.")
#         if not supplier.supplier_email:
#             raise ValueError(f"Supplier with ID {updated_data_request.supplier_id} does not have an email.")

#         try:
#             user_name = f"{app.current_event.given_name or 'user'} {app.current_event.family_name or ''}".strip()
#         except Exception:
#             user_name = "user"

#         try:
#             company_info = get_company_repository().get_company(supplier.company_id)
#             company_name = company_info.company_name if company_info else "Company"
#         except Exception:
#             company_name = "Company"

#         if updated_data_request.status == DataRequestStatus.SUBMITTED:
#             email_body, subject = generate_email_body(
#                 supplier,
#                 mail_type=DataRequestStatus.SUBMITTED,
#                 company_name=company_name,
#                 user_name=user_name,
#                 data_request_id=dataRequestId,  # Changed to data_request_id
#             )
#             body_text = "Data Submitted"
#         elif updated_data_request.status == DataRequestStatus.CLARIFICATION_REQUESTED:
#             email_body, subject = generate_email_body(
#                 supplier,
#                 mail_type=DataRequestStatus.CLARIFICATION_REQUESTED,
#                 company_name=company_name,
#                 user_name=user_name,
#                 data_request_id=dataRequestId,  # Changed to data_request_id
#             )
#             body_text = "Data clarification requested"
#         elif updated_data_request.status == DataRequestStatus.APPROVED:
#             email_body, subject = generate_email_body(
#                 supplier,
#                 mail_type=DataRequestStatus.APPROVED,
#                 company_name=company_name,
#                 user_name=user_name,
#                 data_request_id=dataRequestId,  # Changed to data_request_id
#             )
#             body_text = "Data approved"
#         else:
#             # No email to send for other status updates
#             email_body, subject, body_text = None, None, None

#         if email_body and subject and body_text:
#             recipient_email = [supplier.supplier_email]
#             send_email(DEFAULT_SENDER_EMAIL, recipient_email, subject, body_text, email_body)

#         response = updated_data_request.model_dump(mode="json", by_alias=True, exclude_none=True)
#         response['id'] = str(response['id'])
#         response['date'] = response['date'].isoformat()

#         return response
#     except ValueError as ve:
#         logger.error(f"Validation Error: {ve}")
#         raise
#     except Exception as e:
#         logger.exception(f"Error updating data request: {e}")
#         raise


# @app.resolver(type_name="Query", field_name="getDataRequests")
# @tracer.capture_method
# def get_data_requests_resolver(filters: dict) -> list[dict]:
#     """
#     Retrieves a list of data requests based on provided filters.

#     Args:
#         filters: A dictionary containing filter criteria.

#     Returns:
#         A list of dictionaries, each representing a data request.
#     """
#     try:
#         status_filter = filters.get('status')
#         if status_filter:
#             try:
#                 filters['status'] = DataRequestStatus[status_filter.upper()]
#             except KeyError:
#                 raise ValueError(
#                     f"Invalid status filter: {status_filter}. Must be one of {[e.name for e in DataRequestStatus]}"
#                 )

#         data_requests = get_supplier_data_request_repository().get_data_requests(filters)
#         result = []
#         for request in data_requests:
#             response = request.model_dump(mode="json", by_alias=True, exclude_none=True)
#             response['id'] = str(response['id'])
#             response['date'] = request.date.isoformat()
#             if request.questionnaire_id:
#                 questionnaire = get_questionnaire_repository().get_questionnaire_by_id(
#                     questionnaire_id=request.questionnaire_id
#                 )
#                 response['questionnaire'] = (
#                     questionnaire.model_dump(mode="json", by_alias=True, exclude_none=True)
#                     if questionnaire
#                     else None
#                 )
#             result.append(response)
#         return result

#     except ValueError as ve:
#         logger.error(f"Validation Error: {ve}")
#         raise
#     except Exception as e:
#         logger.exception(f"Error getting data requests: {e}")
#         raise


# @logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
# @tracer.capture_lambda_handler
# def lambda_handler(event: dict, context: LambdaContext) -> dict:
#     """
#     Lambda handler function.

#     Args:
#         event: The event dictionary.
#         context: The Lambda context object.

#     Returns:
#         The result of the AppSync resolver.
#     """
#     identity = event.get("identity")

#     if identity and identity.get("claims"):
#         claims = identity.get("claims")
#         company_id = claims.get("custom:company_id")
#         cognito_user = claims.get("cognito:username")

#         logger.append_keys(
#             company_id=company_id,
#             cognito_user=cognito_user,
#         )
#     return app.resolve(event, context, data_model=CompanyEventModel)