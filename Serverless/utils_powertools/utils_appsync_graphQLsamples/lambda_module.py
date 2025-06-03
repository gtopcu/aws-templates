# import os
# import uuid
# from datetime import datetime, date
# from typing import Optional

# from aws_lambda_powertools import Logger, Tracer
# from aws_lambda_powertools.event_handler import AppSyncResolver
# from aws_lambda_powertools.logging import correlation_paths
# from aws_lambda_powertools.utilities.data_classes import AppSyncResolverEvent
# from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
#     aws_datetime,
#     aws_date,
# )
# from aws_lambda_powertools.utilities.typing import LambdaContext

# DATA_BUCKET_NAME_ENV = "DATA_BUCKET_NAME"

# tracer = Tracer()
# logger = Logger()
# app = AppSyncResolver()


# class CompanyEventModel(AppSyncResolverEvent):
#     @property
#     def company_id(self) -> str:
#         return self.identity.get("claims")["custom:company_id"]


# @app.resolver(type_name="Mutation", field_name="processExpenseSource")
# @tracer.capture_method
# def process_expense_source_resolver(sourceId: str, companyId: str) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         process_expense_source(company_id=company_id, source_id=sourceId)
#     except Exception as e:
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "PROCESSED"}


# @app.resolver(type_name="Mutation", field_name="addFuelFormUpload")
# @tracer.capture_method
# def add_fuel_upload_form_resolver(
#     startDate: str,
#     fuelExpenseDetails: list[dict],
#     uploadType: str,
#     companyId: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
#     endDate: Optional[str] = None,
# ) -> str:
#     company_id = companyId if companyId else app.current_event.company_id
#     source_id = str(uuid.uuid4())
#     expense_source = FuelFormUploadSource(
#         source_id=source_id,
#         company_id=company_id,
#         source_type=SourceType[uploadType],
#         associated_facility=associatedFacility,
#         creation_datetime=aws_datetime(),
#         start_date=_date(startDate),
#         end_date=_date(endDate if endDate else aws_date()),
#         status=DataSourceStatus.READY_TO_PROCESS,
#         form_data=[FuelUsageDetails(**details) for details in fuelExpenseDetails],
#     )
#     get_cust_data_source_repository().save_cust_data_source(company_id, expense_source)
#     return source_id


# @app.resolver(type_name="Mutation", field_name="addEmployeeCommutingData")
# @tracer.capture_method
# def add_employee_commuting_resolver(
#     startDate: str,
#     employeeCommutingDetails: list[dict],
#     uploadType: str,
#     companyId: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
#     endDate: Optional[str] = None,
# ) -> str:
#     company_id = companyId if companyId else app.current_event.company_id
#     source_id = str(uuid.uuid4())
#     expense_source = EmployeeCommutingFormSource(
#         source_id=source_id,
#         company_id=company_id,
#         source_type=SourceType[uploadType],
#         associated_facility=associatedFacility,
#         creation_datetime=aws_datetime(),
#         start_date=_date(startDate),
#         end_date=_date(endDate if endDate else aws_date()),
#         status=DataSourceStatus.READY_TO_PROCESS,
#         form_data=[
#             EmployeeCommutingData(**details) for details in employeeCommutingDetails
#         ],
#     )
#     get_cust_data_source_repository().save_cust_data_source(company_id, expense_source)
#     return source_id


# @app.resolver(type_name="Mutation", field_name="addCompanyExpenseFile")
# @tracer.capture_method
# def add_company_expense_file_resolver(
#     startDate: str,
#     bucketKey: str,
#     bucketName: Optional[str] = None,
#     companyId: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
#     endDate: Optional[str] = None,
# ) -> str:
#     company_id = companyId if companyId else app.current_event.company_id
#     source_id = str(uuid.uuid4())

#     expense_source = CompanyExpensesFileS3Source(
#         source_id=source_id,
#         company_id=company_id,
#         associated_facility=associatedFacility,
#         creation_datetime=aws_datetime(),
#         start_date=_date(startDate),
#         end_date=_date(endDate if endDate else aws_date()),
#         status=DataSourceStatus.READY_TO_PARSE,
#         raw_file_bucket_name=os.environ.get(DATA_BUCKET_NAME_ENV),
#         raw_file_bucket_key=bucketKey,
#     )
#     get_cust_data_source_repository().save_cust_data_source(company_id, expense_source)
#     return source_id


# @app.resolver(type_name="Mutation", field_name="addBulkDataUploadFile")
# @tracer.capture_method
# def add_bulk_upload_file_resolver(
#     startDate: str,
#     bucketKey: str,
#     bucketName: Optional[str] = None,
#     companyId: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
#     endDate: Optional[str] = None,
# ) -> str:
#     company_id = companyId if companyId else app.current_event.company_id
#     source_id = str(uuid.uuid4())

#     expense_source = BulkDataUploadFileS3Source(
#         source_id=source_id,
#         company_id=company_id,
#         associated_facility=associatedFacility,
#         creation_datetime=aws_datetime(),
#         start_date=_date(startDate),
#         end_date=_date(endDate if endDate else aws_date()),
#         status=DataSourceStatus.READY_TO_PROCESS,
#         processed_file_bucket_name=os.environ.get("DATA_BUCKET_NAME"),
#         processed_file_bucket_key=bucketKey,
#     )
#     get_cust_data_source_repository().save_cust_data_source(company_id, expense_source)
#     return source_id


# @app.resolver(type_name="Mutation", field_name="addCompanyUtilityBill")
# @tracer.capture_method
# def add_company_utility_bill_resolver(
#     bucketKey: str,
#     bucketName: Optional[str] = None,
#     companyId: Optional[str] = None,
#     originalFileName: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
# ) -> str:
#     company_id = companyId if companyId else app.current_event.company_id
#     source_id = str(uuid.uuid4())
#     expense_source = UtilityBillS3Source(
#         source_id=source_id,
#         company_id=company_id,
#         associated_facility=associatedFacility,
#         original_file_name=originalFileName,
#         creation_datetime=aws_datetime(),
#         status=DataSourceStatus.READY_TO_PARSE,
#         raw_file_bucket_name=os.environ.get("DATA_BUCKET_NAME"),
#         raw_file_bucket_key=bucketKey,
#     )
#     get_cust_data_source_repository().save_cust_data_source(company_id, expense_source)
#     return source_id


# @app.resolver(type_name="Mutation", field_name="updateCompanyExpenseFile")
# @tracer.capture_method
# def update_company_exp_file_resolver(
#     companyId: Optional[str],
#     sourceId: str,
#     processedFileBucketKey: str,
#     processedFileBucketName: Optional[str] = None,
#     version: Optional[int] = 1,
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise Exception("Company id is required!")
#         update_company_expenses_file_source_with_processed_location(
#             company_id=company_id,
#             source_id=sourceId,
#             processed_file_bucket_name=os.environ.get("DATA_BUCKET_NAME"),
#             processed_file_bucket_key=processedFileBucketKey,
#             version=version,
#         )
#     except Exception as e:
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "UPDATED"}


# @app.resolver(type_name="Mutation", field_name="updateUtilityBillExtractedData")
# @tracer.capture_method
# def update_utility_bill_data_resolver(
#     sourceId: str,
#     companyId: Optional[str] = None,
#     newStartDate: Optional[str] = None,
#     newEndDate: Optional[str] = None,
#     updatedLineItems: Optional[list[dict]] = [],
# ) -> dict:
#     if not newStartDate and not newEndDate and not updatedLineItems:
#         raise ValueError("At least one field to update must be provided!")
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise Exception("Company id is required!")
#         update_utility_bill_data(
#             company_id=company_id,
#             source_id=sourceId,
#             new_start_date=_date(newStartDate),
#             new_end_date=_date(newEndDate),
#             updated_data=[UtilityBillExtractedLineItem(**i) for i in updatedLineItems],
#         )
#     except Exception as e:
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "UPDATED"}


# @app.resolver(type_name="Query", field_name="getAllCompaniesDataSourceSummaries")
# @tracer.capture_method
# def get_customer_data_source_summaries_resolver(sourceType: str) -> list[dict]:
#     try:
#         source_summaries = (
#             get_cust_data_source_repository().get_all_company_data_source_summaries(
#                 source_type=SourceType[sourceType]
#             )
#         )
#     except Exception as e:
#         logger.exception(e)
#         raise
#     else:
#         logger.info(f"Fetched {sourceType} source summaries")
#         return [
#             i.model_dump(mode="json", by_alias=True, exclude_none=True)
#             for i in source_summaries
#         ]


# @app.resolver(type_name="Query", field_name="getAllExpenseSourceSummaries")
# @tracer.capture_method
# def get_expense_source_summaries_resolver(
#     companyId: Optional[str] = None,
# ) -> list[dict]:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")

#         source_summaries = get_cust_data_source_repository().get_all_cust_data_source_summaries_for_company(
#             company_id=company_id
#         )
#     except Exception as e:
#         logger.exception(e)
#         raise
#     else:
#         logger.info(f"Fetched expense source summaries for: {companyId}")
#         return [
#             i.model_dump(mode="json", by_alias=True, exclude_none=True)
#             for i in source_summaries
#         ]


# @app.resolver(type_name="Query", field_name="getCustomerDataSourceSummariesByType")
# @tracer.capture_method
# def get_customer_data_source_summaries_by_type_resolver(
#     sourceType: str,
#     companyId: Optional[str] = None,
#     associatedFacility: Optional[str] = None,
# ) -> list[dict]:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")

#         source_type = SourceType[sourceType]
#         source_summaries = get_cust_data_source_repository().get_cust_data_source_summaries_for_company(
#             company_id=company_id,
#             source_type=source_type,
#             facility=associatedFacility,
#         )
#     except Exception as e:
#         logger.exception(e)
#         raise
#     else:
#         logger.info(f"Fetched expense source summaries for: {companyId}")
#         return [
#             i.model_dump(mode="json", by_alias=True, exclude_none=True)
#             for i in source_summaries
#         ]


# @app.resolver(type_name="Query", field_name="getCustomerDataSource")
# @tracer.capture_method
# def get_customer_data_source_resolver(
#     sourceId: str, companyId: Optional[str] = None
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")

#         expense_source = get_cust_data_source_repository().get_cust_data_source(
#             company_id=company_id, source_id=sourceId
#         )
#     except Exception as e:
#         logger.exception(e)
#         raise
#     else:
#         logger.info(
#             f"Fetched expense source: {expense_source.source_id} for: {companyId}"
#         )
#         return expense_source.model_dump(mode="json", by_alias=True, exclude_none=True)


# @app.resolver(type_name="Mutation", field_name="deleteCustomerDataSource")
# @tracer.capture_method
# def delete_customer_data_source_resolver(
#     sourceId: str, companyId: Optional[str] = None
# ) -> dict:
#     company_id = companyId if companyId else app.current_event.company_id
#     try:
#         if company_id is None:
#             raise ValueError("Company id is required!")

#         get_cust_data_source_repository().delete_cust_data_source(
#             company_id=company_id, source_id=sourceId
#         )
#     except Exception as e:
#         return _return_failure(e)
#     else:
#         return {"success": True, "message": "DELETED"}


# @app.resolver(type_name="Query", field_name="getExpenseSource")
# @tracer.capture_method
# def get_expense_source_resolver(sourceId: str, companyId: Optional[str] = None) -> dict:
#     return get_customer_data_source_resolver(sourceId, companyId)


# @logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
# @tracer.capture_lambda_handler
# def lambda_handler(event: dict, context: LambdaContext) -> dict:
#     logger.append_keys(
#         company_id=event.get("identity").get("claims").get("custom:company_id"),
#         cognito_user=event.get("identity").get("claims").get("cognito:username"),
#     )
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


# def _date(date_str: str) -> date | None:
#     try:
#         if date_str is None:
#             return None
#         res = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
#     except Exception:
#         raise Exception(f"Date {date_str} must be a valid date of format YYYY-MM-DD!")
#     else:
#         return res
