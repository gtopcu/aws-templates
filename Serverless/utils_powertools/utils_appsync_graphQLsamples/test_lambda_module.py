# import json
# import os
# import uuid
# from dataclasses import dataclass
# from datetime import date
# from pathlib import Path
# from typing import Optional

# import pytest
# import moto
# from moto import mock_aws

# from lambda_module import lambda_handler

# FILE_PATH = os.path.dirname(os.path.realpath(__file__))

# @pytest.fixture
# def lambda_environment():
#     os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
#     os.environ["ENVIRONMENT"] = "local-test"
#     os.environ["ENV_DATA_TABLE"] = "COMPANY_DATA"
#     os.environ["RDS_PASSWORD_ARN"] = (
#         "arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX"
#     )

# @pytest.fixture
# def lambda_context():
#     @dataclass
#     class LambdaContext:
#         function_name: str = FILE_PATH + "/test"
#         memory_limit_in_mb: int = 128
#         invoked_function_arn: str = (
#             "arn:aws:lambda:eu-west-1:123456789012:function:test"
#         )
#         aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

#     return LambdaContext()


# # Fixture to mock Docker-based Aurora DB
# @pytest.fixture(scope="session")
# def aurora_db_mock():
#     with DockerAuroraMock() as docker_mock:
#         yield docker_mock


# @pytest.fixture()
# def db_session(aurora_db_mock):
#     with (
#         moto.mock_aws(),  # Use Moto to mock AWS services in general
#         AuroraDBRepoFixture(
#             repo=get_processed_data_item_repository,
#             credentials=aurora_db_mock.mock_credentials,
#         ) as db_repo,
#     ):
#         yield db_repo


# @mock_aws
# class TestCustomerDataService:
#     def test_add_utility_bill_expense_source(self, lambda_environment, lambda_context):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(FILE_PATH + "/test/add_utility_bill_1_event.json").read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_utility_bill_expense_source_with_only_mandatory_input(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH + "/test/add_utility_bill_1_event_mandatory_fields_only.json"
#             ).read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_company_expenses_file_expense_source(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(FILE_PATH + "/test/add_expense_file_1_event.json").read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_company_expenses_file_expense_source_with_only_mandatory_input(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH + "/test/add_expense_file_1_event_mandatory_fields_only.json"
#             ).read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_fuel_form_upload_expense_source(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(FILE_PATH + "/test/add_fuel_form_upload_1_event.json").read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_employee_commuting_form_upload_expense_source(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH + "/test/add_employee_commuting_form_upload_1_event.json"
#             ).read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_add_fuel_form_upload_expense_source_with_only_mandatory_input(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()
#         mock_raw_data_item_repo()

#         # GIVEN
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH
#                 + "/test/add_fuel_form_upload_1_event_mandatory_fields_only.json"
#             ).read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert is_valid_uuid(result)

#     def test_delete_data_source_deletes_entry(self, lambda_environment, lambda_context):
#         repo = mock_data_src_repo()

#         company_id = "376d41ab-bafa-4eab-a03f-19968da396e2"
#         source_id = "49e40f76-9efd-446f-b076-de8531e97551"

#         repo.save_cust_data_source(
#             company_id=company_id,
#             expense_source=FuelFormUploadSource(
#                 company_id=company_id,
#                 source_id=source_id,
#                 associated_facility="Hill house",
#                 source_type=SourceType.FUEL_HEATING,
#                 creation_datetime="2023-12-21T11:28:21.543Z",
#                 start_date=date(2021, 11, 1),
#                 end_date=date(2022, 1, 1),
#                 status=DataSourceStatus.READY_TO_PROCESS,
#                 form_data=[],
#             ),
#         )

#         # GIVEN
#         fake_event = json.loads(
#             Path(FILE_PATH + "/test/deleteCustomerDataSource_event.json").read_text()
#         )

#         # WHEN
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN
#         assert result["message"] == "DELETED"
#         with pytest.raises(Exception) as excinfo:
#             repo.get_cust_data_source(company_id=company_id, source_id=source_id)
#             assert (
#                 f'Expense source with id "{source_id}" does not exist for company "{company_id}"!'
#                 in str(excinfo.value)
#             )

#     def test_get_all_companies_data_source_summary_returns_sources(
#         self, lambda_environment, lambda_context
#     ):
#         expense_src_repo = mock_data_src_repo()

#         company_one = "1afe7d22-49eb-4d4d-94c7-5c8668356714"
#         company_two = "1afe7d22-49eb-4d4d-94c7-5c8668356715"
#         es_one = FuelFormUploadSource(
#             source_id="es-one-src-id",
#             company_id=company_one,
#             associated_facility="Hill house",
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2021, 11, 1),
#             end_date=date(2022, 1, 1),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )
#         es_two = CompanyExpensesFileS3Source(
#             source_id="es-two-src-id",
#             company_id=company_one,
#             associated_facility=None,
#             source_type=SourceType.EXPENSE_FILE,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2022, 12, 21),
#             end_date=date(2023, 12, 20),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             raw_file_bucket_name="secr-ai-test-company",
#             raw_file_bucket_key="hh/ef/2aee60f0-1227-493b-94fd-ef960d43b041.jpg",
#         )
#         es_three = FuelFormUploadSource(
#             source_id="es-three-src-id",
#             company_id=company_two,
#             associated_facility=None,
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2022, 12, 21),
#             end_date=date(2023, 12, 20),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )

#         # GIVEN
#         expense_src_repo.save_cust_data_sources(
#             company_id=company_one, expense_sources=[es_one, es_two]
#         )
#         expense_src_repo.save_cust_data_sources(
#             company_id=company_two, expense_sources=[es_three]
#         )

#         # WHEN company_one FUEL_HEATING expense summaries fetched through token
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH + "/test/getAllCompanyDataSourcesBySourceType.json"
#             ).read_text()
#         )
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN all of company_one's data is returned
#         assert len(result) == 1

#         assert {
#             "companyId": es_two.company_id,
#             "sourceId": es_two.source_id,
#             "status": es_two.status.value,
#             "sourceType": es_two.source_type.value,
#             "startDate": str(es_two.start_date),
#             "endDate": str(es_two.end_date),
#             "creationDatetime": es_two.creation_datetime,
#             "rawFileBucketKey": es_two.raw_file_bucket_key,
#             "rawFileBucketName": es_two.raw_file_bucket_name,
#         } in result

#     def test_get_customer_data_source_summary_returns_sources_using_user_token_company(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()

#         company_one = "1afe7d22-49eb-4d4d-94c7-5c8668356714"
#         company_two = "376d41ab-bafa-4eab-a03f-19968da396e2"
#         es_one = FuelFormUploadSource(
#             source_id="es-one-src-id",
#             company_id=company_one,
#             associated_facility="Hill house",
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2021, 11, 1),
#             end_date=date(2022, 1, 1),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )
#         es_two = FuelFormUploadSource(
#             source_id="es-two-src-id",
#             company_id=company_two,
#             associated_facility="Hill house",
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2022, 12, 21),
#             end_date=date(2023, 12, 20),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )

#         # GIVEN
#         get_cust_data_source_repository().save_cust_data_source(company_one, es_one)
#         get_cust_data_source_repository().save_cust_data_source(company_two, es_two)

#         # WHEN company_one FUEL_HEATING expense summaries fetched through token
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH
#                 + "/test/getCustomerDataSourceSummariesByType_by_token_company_id.json"
#             ).read_text()
#         )
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN only company_one's data is returned
#         assert len(result) == 1
#         assert result[0] == {
#             "companyId": es_one.company_id,
#             "sourceId": es_one.source_id,
#             "status": es_one.status.value,
#             "sourceType": es_one.source_type.value,
#             "startDate": str(es_one.start_date),
#             "endDate": str(es_one.end_date),
#             "creationDatetime": es_one.creation_datetime,
#         }

#     def test_get_customer_data_source_summary_returns_sources_using_input_company_id(
#         self, lambda_environment, lambda_context
#     ):
#         mock_data_src_repo()

#         company_one = "1afe7d22-49eb-4d4d-94c7-5c8668356714"
#         company_two = "376d41ab-bafa-4eab-a03f-19968da396e2"
#         es_one = FuelFormUploadSource(
#             source_id="es-one-src-id",
#             company_id=company_one,
#             associated_facility="Hill house",
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2021, 11, 1),
#             end_date=date(2022, 1, 1),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )
#         es_two = FuelFormUploadSource(
#             source_id="es-two-src-id",
#             company_id=company_two,
#             associated_facility="Hill house",
#             source_type=SourceType.FUEL_HEATING,
#             creation_datetime="2023-12-21T11:28:21.543Z",
#             start_date=date(2022, 12, 21),
#             end_date=date(2023, 12, 20),
#             status=DataSourceStatus.READY_TO_PROCESS,
#             form_data=[],
#         )

#         # GIVEN
#         get_cust_data_source_repository().save_cust_data_source(company_one, es_one)
#         get_cust_data_source_repository().save_cust_data_source(company_two, es_two)

#         # WHEN company_one FUEL_HEATING expense summaries fetched through input company name
#         fake_event = json.loads(
#             Path(
#                 FILE_PATH
#                 + "/test/getCustomerDataSourceSummariesByType_by_input_company_id.json"
#             ).read_text()
#         )
#         result = lambda_handler(fake_event, lambda_context)

#         # THEN only company_two's data is returned
#         assert len(result) == 1
#         assert result[0] == {
#             "companyId": es_two.company_id,
#             "sourceId": es_two.source_id,
#             "status": es_two.status.value,
#             "sourceType": es_two.source_type.value,
#             "startDate": str(es_two.start_date),
#             "endDate": str(es_two.end_date),
#             "creationDatetime": es_two.creation_datetime,
#         }

#     def test_bulk(self, lambda_environment, lambda_context):
#         mock_fy_repo()
#         mock_data_src_repo()

#         fake_event = json.loads(
#             Path(FILE_PATH + "/test/for_testing_bulk_csv.json").read_text()
#         )
#         result = lambda_handler(fake_event, lambda_context)

#         print(f"Result {result}")


# def create_fuel_form_upload_source(
#     company_id: str,
#     associated_facility: str,
#     source_type: SourceType,
#     start_date: date,
#     end_date: date,
#     source_id: str,
# ) -> FuelFormUploadSource:
#     return FuelFormUploadSource(
#         company_id=company_id,
#         associated_facility=associated_facility,
#         source_id=source_id,
#         source_type=source_type,
#         creation_datetime="2023-12-21T11:28:21.543Z",
#         start_date=start_date,
#         end_date=end_date,
#         status=DataSourceStatus.READY_TO_PROCESS,
#         form_data=[],
#     )


# def create_utility_bill_upload_source(
#     company_id: str,
#     associated_facility: str,
#     start_date: date,
#     end_date: date,
#     source_id: str,
# ) -> UtilityBillS3Source:
#     return UtilityBillS3Source(
#         company_id=company_id,
#         associated_facility=associated_facility,
#         source_id=source_id,
#         source_type=SourceType.UTILITY_BILL,
#         creation_datetime="2023-12-21T18:34:31.336Z",
#         start_date=start_date,
#         end_date=end_date,
#         status=DataSourceStatus.READY_TO_PARSE,
#         raw_file_bucket_name="secr-ai-test-company",
#         raw_file_bucket_key="hh/eb/2aee60f0-1227-493b-94fd-ef960d43b041.jpg",
#     )


# def create_parsed_utility_bill_upload_source(
#     company_id: str,
#     associated_facility: str,
#     start_date: date,
#     end_date: date,
#     source_id: str,
# ) -> UtilityBillS3Source:
#     return UtilityBillS3Source(
#         company_id=company_id,
#         associated_facility=associated_facility,
#         source_id=source_id,
#         source_type=SourceType.UTILITY_BILL,
#         creation_datetime="2023-12-21T18:34:31.336Z",
#         start_date=start_date,
#         end_date=end_date,
#         status=DataSourceStatus.PARSED,
#         raw_file_bucket_name="secr-ai-test-company",
#         raw_file_bucket_key="hh/eb/2aee60f0-1227-493b-94fd-ef960d43b041.jpg",
#     )


# def create_expense_file_upload_source(
#     company_id: str,
#     associated_facility: Optional[str],
#     start_date: date,
#     end_date: date,
#     source_id: str,
# ) -> CompanyExpensesFileS3Source:
#     return CompanyExpensesFileS3Source(
#         company_id=company_id,
#         associated_facility=associated_facility,
#         source_id=source_id,
#         source_type=SourceType.EXPENSE_FILE,
#         creation_datetime="2023-12-21T18:34:31.336Z",
#         start_date=start_date,
#         end_date=end_date,
#         status=DataSourceStatus.READY_TO_PARSE,
#         raw_file_bucket_name="secr-ai-test-company",
#         raw_file_bucket_key="hh/ef/2aee60f0-1227-493b-94fd-ef960d43b041.jpg",
#     )


# def is_valid_uuid(val):
#     try:
#         uuid.UUID(str(val))
#         return True
#     except ValueError:
#         return False
