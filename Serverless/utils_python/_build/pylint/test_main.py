
# source .venv/bin/activate

import os
from dataclasses import dataclass
from datetime import datetime, timezone

import pytest
from dotenv import find_dotenv, load_dotenv

if not load_dotenv(find_dotenv()):
    raise Exception("Failed to load .env file")

for key, value in os.environ.items():
    print(f"{key}: {value}")

@dataclass
class LambdaContext:
    function_name: str = "testLambda"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
    aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

@pytest.fixture
def lambda_context():
    return LambdaContext()

def test_lambda(lambda_context:LambdaContext):
    print(lambda_context.function_name)
