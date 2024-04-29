 
# content of tests/conftest.py
import pytest
from dataclasses import dataclass

def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["info1: did you know that ...", "did you?"]

@pytest.fixture(scope="session")
def db_conn():
    db = " "
    url = " "
    with db.connect(url) as conn: 
        yield conn

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")

@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()
