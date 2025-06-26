
from dataclasses import dataclass
import pytest

import requests
# from requests import Response, Timeout

"""
https://docs.pytest.org/en/8.0.x/
https://docs.pytest.org/en/8.0.x/reference/fixtures.html#fixture

pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories

Each test has a unique instance of the class, but class attributes are shared
(this does not refer to the same object)

"""

# def test_debug():
#     if __debug__: # default True
#         raise AssertionError

# --------------------------------------------------------------------------------------------
# MONKEYPATCH:
# --------------------------------------------------------------------------------------------
# https://docs.pytest.org/en/stable/how-to/monkeypatch.html
# https://pytest-with-eric.com/mocking/pytest-monkeypatch/

# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     """Remove requests.sessions.Session.request for all tests."""
#     monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture(scope="class", autouse=False)
def aws_env(monkeypatch):
    """
    setattr(requests, "get", lambda x: MockResponse(x))
    setattr("requests.get", "{'mock_key': 'mock_response'}")
    delattr("requests.get", "{'mock_key': 'mock_response'}")
    
    setattr(obj, name, value): Set an attribute on an object for the duration of the test
    delattr(obj, name): Delete an attribute from an object
    setitem(mapping, name, value): Set a key-value pair in a dictionary
    delitem(mapping, name): Remove a key from a dictionary
    setenv(name, value): Set an environment variable
    delenv(name): Remove an environment variable
    syspath_prepend(path): Add a path to sys.path
    chdir(path): Change the current working directory
    context(): Apply patches in a controlled scope
    """
    monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'testing')
    assert monkeypatch.getenv('AWS_DEFAULT_REGION') == 'us-east-1'

import functools
from functools import partial
from pytest import MonkeyPatch

with MonkeyPatch.context() as mp:
    mp.setattr(functools, "partial", 3)

# Patching objects/functions using monkeypatch:
from pathlib import Path

def get_ssh_path():
    return Path.home() / ".ssh"

def test_get_ssh_path(monkeypatch):
    def mock_return():
        return Path("/tmp")
    monkeypatch.setattr(Path, "home", mock_return)

    monkeypatch.setattr(Path, "home", lambda: Path("/tmp"))
    monkeypatch.setattr(Path, "home", Path("/tmp"))
    
    assert get_ssh_path() == Path("/tmp/.ssh")
    # monkeypatch.delattr(Path, "home")

# --------------------------------------------------------------------------------------------

# Patching Requests
from pytest import MonkeyPatch

with MonkeyPatch.context() as mp:
    mp.setattr("requests.get", "{'mock_key': 'mock_response'}")
    mp.setattr(requests, "get", lambda x: MockResponse(x))
    mp.delattr(requests, "get")

# Blocking all HTTP requests - define in conftest.py file and use autouse=True
# mp.delattr("requests.sessions.Session.request") 
 
 
# Patching with  mock class
def get_json(url):
    response = requests.get(url)
    return response.json()

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_get_json(monkeypatch):
    # Any args may be passed - mock_get() will always return the mocked object
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)

    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

# --------------------------------------------------------------------------------------------

# https://pytest-mock.readthedocs.io/en/latest/usage.html
# https://docs.python.org/3/library/unittest.mock.html#patch
# from pytest_mock import mocker

# def test_foo(mocker):
#     mocker.patch('os.remove')
#     mocker.patch.object(os, 'listdir', autospec=True)
#     mocker.patch.object(
#                 sqs_queue.sqs_client, 'delete_message',
#                 side_effect=ClientError({'Error': {}}, 'DeleteMessage')
#             )
#
# def mock_aws_client(mocker):
#     mock_client = mocker.patch("boto3.client")
#     mock_client.return_value = mocker.Mock()
#     return mock_client

# --------------------------------------------------------------------------------------------

# can also place in conftest.py / use monkeypatch.setenv()
# @pytest.fixture(scope="session", autouse=True)
# def set_env():
#     os.environ["FLAG"] = "1"

# scope: function(default), class, module, package, session
@pytest.fixture(scope="class", autouse=False)
# pytest.mark.usefixtures("lambda_context")
def lambda_context():
    return "Context initialized"
 
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

def test_context(lambda_context):
    print("Context:", lambda_context)
    # assert lambda_context == "Context initialized"
    # assert lambda_context == ["a", "b", "c", "d", "e", "f", "g"]
    # assert hasattr(x, "check")
    # assert isinstance(x, MyClass)
    # assert 0, lambda_context  # to show value

# Verifies ValueError is raised with the given error detail
def test_raises():
    with pytest.raises(ValueError, match="Unsupported type"):
        raise
        # raise ValueError("Invalid input")

    # with pytest.raises(ZeroDivisionError) as exc_info:
    #     result = 1 / 0
    #     assert "division by zero" in str(exc_info.value)

@pytest.mark.unit
@pytest.mark.slow
@pytest.mark.integration
def test_unit():
    pass

@pytest.mark.parametrize("value", ["foo", "bar", "baz"])
def test_param(value: str):
    print(value)

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert (a + b) == expected

def test_usageerror():
    pytest.UsageError("usage error")

def test_skip():
    pytest.skip("skipping this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

def test_fail():
    pytest.fail("failing this test")

def test_xfail():
    pytest.xfail("xfailing this test")