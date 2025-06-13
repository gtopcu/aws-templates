
import pytest

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
    setattr("requests.get", lambda x: MockResponse())
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

# Context manager that returns a new MonkeyPatch object which undoes any patching done inside the with block upon exit.
# Useful in situations where it is desired to undo some patches before the test ends,
# with monkeypatch.context() as mp:
#     mp.setattr(functools, "partial", 3)

# Patching objects/functions using monkeypatch:
# from pathlib import Path

# def get_ssh_path():
#     return Path.home() / ".ssh"

# def test_get_ssh_path(monkeypatch):
#     def mockreturn():
#         return Path("/tmp")

#     monkeypatch.setattr(Path, "home", mockreturn)
#     assert get_ssh_path() == Path("/tmp/.ssh")

#     # Optional: reset the monkeypatch if needed for rest of the test
#     monkeypatch.delattr(Path, "home")

# --------------------------------------------------------------------------------------------

# Patching function/API responses using monkeypatch:

# def get_cat_fact():
#     response = requests.get("https://meowfacts.herokuapp.com/")
#     return response.json()

# class MockResponse:
#     @staticmethod
#     def json():
#         return {"data": ["Cats can jump up to six times their length."]}

# def test_get_cat_fact(monkeypatch):
#     monkeypatch.setattr("requests.get", lambda x: MockResponse())
#     assert get_cat_fact() == {"data": ["Cats can jump up to six times their length."]}


# If you need to mock the MeowFacts API across multiple tests, you can move the logic into a reusable fixture:

# @pytest.fixture
# def mock_meowfacts_api(monkeypatch):
#     class MockResponse:
#         @staticmethod
#         def json():
#             return {"data": ["Cats sleep 70% of their lives."]}

#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr("requests.get", mock_get)

# def test_get_cat_fact(mock_meowfacts_api):
#     result = get_cat_fact()
#     assert result == {"data": ["Cats sleep 70% of their lives."]}


# To block all HTTP requests using the requests library, you can define a global patch in a conftest.py file.
# The autouse=True fixture automatically applies to all tests, ensuring that no test makes actual HTTP calls
# Use monkeypatch.context() to limit the scope of a patch to a specific block of code

# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     """Disable all HTTP requests by removing requests.sessions.Session.request."""
#     monkeypatch.delattr("requests.sessions.Session.request")


# --------------------------------------------------------------------------------------------

# https://pytest-mock.readthedocs.io/en/latest/usage.html
# https://docs.python.org/3/library/unittest.mock.html#patch
# def test_foo(mocker):
#     mocker.patch('os.remove')
#     mocker.patch.object(os, 'listdir', autospec=True)
#     mocker.patch.object(
#                 sqs_queue.sqs_client, 'delete_message',
#                 side_effect=ClientError({'Error': {}}, 'DeleteMessage')
#             )

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
 
def (lambda_context):
    print("Context:", lambda_context)
    assert lambda_context == "Context initialized"
    # assert lambda_context == ["a", "b", "c", "d", "e", "f", "g"]
    # assert hasattr(x, "check")
    # assert isinstance(x, MyClass)
    # assert 0, lambda_context  # to show value

# Verifies ValueError is raised with the given error detail
def test_raises():
    with pytest.raises(ValueError, match="Unsupported mail type"):
        pass
        # raise
        # raise ValueError("Invalid input")

def test_raises2():
    with pytest.raises(ZeroDivisionError) as exc_info:
        result = 1 / 0
        assert "division by zero" in str(exc_info.value)

def test_usageerror():
    pytest.UsageError("usage error")

def test_skip():
    pytest.skip("skipping this test")

@pytest.mark.unit
def test_unit():
    pass

@pytest.mark.slow
@pytest.mark.integration
def test_integration():
    pass

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

def test_fail():
    pytest.fail("failing this test")

def test_xfail():
    pytest.xfail("xfailing this test")

# Testing the add function with various sets of parameters
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert (a + b) == expected

# @pytest.mark.parametrize(
#     "value", ["foo", "bar", "baz"]
# )
# def test_dynamo_put(create_table, value):
#     dynamo_put("string", value)
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table("string")
#     response = table.get_item(
#         Key={
#             'string': value,
#             'mykey': 'foo'
#         }
#     )
#     print(response)
#     assert response["Item"]["string"] == value    