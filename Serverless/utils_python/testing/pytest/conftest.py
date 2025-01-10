 
# content of tests/conftest.py

import os
import pytest
from dataclasses import dataclass

# os.environ["DDB_TABLE_NAME"] = "table-1"

# @pytest.fixture(scope="session", autouse=True)
# def set_env():
#     mp = pytest.MonkeyPatch()
#     print("Setting monkeypatch globally..")
#     mp.setenv("DDB_TABLE_NAME", "table-1")
#     yield
#     mp.undo()  # Clean up after all tests are done

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
        function_version:str = "$LATEST"
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        memory_limit_in_mb: int = 128
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"
        log_group_name = "/aws/lambda/test"
        log_stream_name = "2024/01/01/[$LATEST]123456789"

        def get_remaining_time_in_millis(self):
            return 30000
            
    return LambdaContext()
