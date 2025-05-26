
# source .venv/bin/activate
from datetime import datetime, timezone
from dotenv import load_dotenv, find_dotenv
import os
import pytest
from dataclasses import dataclass

if not load_dotenv(find_dotenv()):
    raise Exception("Failed to load .env file")

for key, value in os.environ.items():
    print(f"{key}: {value}")

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

def test_lambda(lambda_context):
    print(lambda_context.function_name)

