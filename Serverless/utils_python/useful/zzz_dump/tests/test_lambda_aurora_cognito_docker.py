import pytest
import os
import json
from pathlib import Path
from dataclasses import dataclass
import boto3
import moto
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient

from decimal import Decimal
from datetime import date


FILE_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def lambda_environment():
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    os.environ["ENVIRONMENT"] = "local-test"
    os.environ["DATA_BUCKET_NAME"] = "dev-secr-customer-data-bucket"
    os.environ["RDS_PASSWORD_ARN"] = (
        "arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX"
    )


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "processed_customer_data_service"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            "arn:aws:lambda:eu-west-2:092241524551:function:test"
        )
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()


@pytest.fixture
def cognito_context():
    with moto.mock_cognitoidp():
        cognito_client: CognitoIdentityProviderClient = boto3.client("cognito-idp")
        user_pool_id = cognito_client.create_user_pool(PoolName="TestUserPool")["UserPool"]["Id"]
        cognito_client.create_group(UserPoolId=user_pool_id, GroupName="admin")
        os.environ["USER_POOL_ID"] = user_pool_id
        yield user_pool_id


# Fixture to mock Docker-based Aurora DB
@pytest.fixture(scope="session")
def aurora_db_mock():
    with DockerAuroraMock() as docker_mock:
        yield docker_mock


# Fixture to mock the database session using Aurora and processed data repository
@pytest.fixture()
def db_session(aurora_db_mock):
    with (
        moto.mock_aws(),  
        AuroraDBRepoFixture(
            repo=get_processed_data_item_repository,
            credentials=aurora_db_mock.mock_credentials,
        ) as db_repo,
    ):
        yield db_repo


# Example Test Class for Processed Data Filter
class TestprocessedDataFilter:
    def test_processed_data_filter_facility_filter(
        self, lambda_environment, lambda_context ,db_session
    ):
        mock_data_src_repo()  # Mock data source repository for DynamoDB interactions
        
        # Create and save mock data in the session
        company_id = "9c524cb2-966c-4828-8023-2ce716dbeecf"
        # company_id = "15c06a67-ef38-4d79-bf8d-23ccea3ca578"
        item_one = get_fuel_item(company_id)
        db_session.save_processed_data_items([item_one])

        # Load the JSON input from a file for testing
        inputjson = json.loads(
            Path(FILE_PATH + "/test/test_process_data_filter.json").read_text()
        )

        # Call the Lambda handler
        result: dict = lambda_handler(inputjson, lambda_context)
        print(result)
        # Perform assertions to check the results
        assert isinstance(result, dict)
        # assert "data" in result

    
    def test_update_processed_data_item(
        self, lambda_environment, lambda_context ,db_session
    ):
        mock_data_src_repo()  # Mock data source repository for DynamoDB interactions
        company_id = "24039d42-f9e4-4b16-a089-42fe4d88565d"



        data_item = ProcessedCustomerDataItem(
            company_id=company_id,
            source_id="5fd5303c-cc43-493f-abed-beb2016f54eb",
            line_item_number=2,
            source_type=SourceType.FUEL_VEHICLE,
            supplier="omkar1",
            category=Category.SCOPE_3_PURCHASE,
            fuel_type=FuelType.DIESEL,
            # original_value=Decimal("202.1"),
            # original_unit=ActivityUnit.LITRE,
            unit_conversion_factor_used=Decimal("4.54608251986351"),
            # converted_value=Decimal("44.455858"),
            # converted_unit=StandardUnit.GBP,
            original_spend_value=Decimal("202.1"),
            original_spend_unit=StandardUnit.GBP,
            converted_spend_value=Decimal("202.1"),
            converted_spend_unit=StandardUnit.GBP,
            original_activity_unit=None,
            original_activity_value=None,
            converted_activity_unit=None,
            converted_activity_value=None,
            scope=1,
            conversion_factor_identifier="FUEL:DIESEL:LITRE:DEFAULT",
            emission_conversion_factor_used=Decimal("0.139"),
            kg_co2e_total_value=Decimal("21231.0"),
            energy_conversion_factor_used=Decimal("9.301"),
            kwh_value=Decimal("21231.0"),
            start_date=date(2022, 4, 1),
            end_date=date(2022, 4, 1),
            status=DataItemStatus.PROCESSED,
            supplier_id="a776a611-d3d9-4a31-b5db-3c1de51099dc",
            custom_emission_factor=Decimal("1.0"),
            custom_measurement_unit="KG",
            custom_measurement=Decimal("1.0"),
        )
        
        db_session.save_processed_data_items([data_item])

        # Load the JSON input from a file for testing
        inputjson = json.loads(
            Path(FILE_PATH + "/test/test_update_processed_data_item.json").read_text()
        )

        # Call the Lambda handler
        result: dict = lambda_handler(inputjson, lambda_context)
        print(result)
        # Perform assertions to check the results
        assert isinstance(result, dict)