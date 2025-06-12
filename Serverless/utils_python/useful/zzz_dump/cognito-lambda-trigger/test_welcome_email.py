import os
from unittest.mock import patch
import boto3
import pytest
from moto import mock_aws
from lambda_module import lambda_handler
from secr.domain.model.company import Company
from secr.repository.dynamodb.table_mocks import mock_company_repo


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
    os.environ["ENVIRONMENT"] = "DEV"


@pytest.fixture
def lambda_event():
    """Generates a mock lambda even for CustomMessage_AdminCreateUser"""
    return {
        "triggerSource": "CustomMessage_AdminCreateUser",
        "request": {
            "userAttributes": {
                "custom:company_id": "a1b718e5-b0b7-40c9-a9e6-00804d44af25",
                "email": "test@test.com",
            },
            "codeParameter": "12345",
            "usernameParameter": "test@test.com",
        },
        "response": {},
    }


@pytest.fixture
def mock_logger():
    with patch("lambda_module.logger") as logger:
        yield logger


@pytest.fixture()
def setup_ses():
    with mock_aws():
        ses_client = boto3.client("ses", region_name="eu-west-2")
        ses_client.verify_email_identity(EmailAddress="support@climatise.com")
        yield


@mock_aws()
def test_lambda_handler_sends_email_onboarding_false(
    aws_credentials,
    lambda_event,
    mock_logger,
    setup_ses,
):
    mock_company_repo_instance = mock_company_repo()
    unsaved_initial_company = Company(
        company_name="Test Company",
        sub_domain="secr-ai-test-company",
        energy_calculation_method="MARKET_BASED",
        location="here",
        company_id="a1b718e5-b0b7-40c9-a9e6-00804d44af25",
        admin_email="test@test.com",
        s3_bucket_name="test-company-bucket",
        is_onboarded="False",
    )
    mock_company_repo_instance.initialise_company(unsaved_initial_company)

    with patch(
        "secr.repository.dynamodb.dd_company_repository.get_company_repository",
        return_value=mock_company_repo_instance,
    ):
        # Assert that the response has been generated in result correctly.
        result = lambda_handler(lambda_event, None)

        # Check that the logger.info was called with the expected message
        mock_logger.info.assert_called_with(
            "Returning event to cognito. Is_onboarded = False"
        )

        # Ensure the event is returned correctly
        assert result == lambda_event


@mock_aws()
def test_lambda_handler_sends_email_onboarding_true(
    aws_credentials,
    lambda_event,
    mock_logger,
    setup_ses,
):
    mock_company_repo_instance = mock_company_repo()
    unsaved_initial_company = Company(
        company_name="Test Company",
        sub_domain="secr-ai-test-company",
        energy_calculation_method="MARKET_BASED",
        location="here",
        company_id="a1b718e5-b0b7-40c9-a9e6-00804d44af25",
        admin_email="test@test.com",
        s3_bucket_name="test-company-bucket",
        is_onboarded="True",
    )
    mock_company_repo_instance.initialise_company(unsaved_initial_company)

    with patch(
        "secr.repository.dynamodb.dd_company_repository.get_company_repository",
        return_value=mock_company_repo_instance,
    ):
        # Assert that the response has been generated in result correctly.
        result = lambda_handler(lambda_event, None)

        # Check that the logger.info was called with the expected message
        mock_logger.info.assert_called_with(
            "Returning event to cognito. Is_onboarded = True"
        )

        # Ensure the event is returned correctly
        assert result == lambda_event
