
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

@pytest.fixture(autouse=True)
def aws_env(monkeypatch):
    """
    Sets mock AWS credentials and region for testing.
    """
    monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'testing')
    monkeypatch.setenv('AWS_SECRET_ACCESS_KEY', 'testing')
    monkeypatch.setenv('AWS_SECURITY_TOKEN', 'testing')
    monkeypatch.setenv('AWS_SESSION_TOKEN', 'testing')
    monkeypatch.setenv('AWS_DEFAULT_REGION', 'us-east-1')

# scope: function(default), class, module, package, session
@pytest.fixture(scope="module") # autouse=True
def context():
    return "Context initialized"

# https://pytest-mock.readthedocs.io/en/latest/usage.html
# def test_foo(mocker):
#     mocker.patch('os.remove')
#     mocker.patch.object(os, 'listdir', autospec=True)
#     mocker.patch.object(
#                 sqs_queue.sqs_client, 'delete_message',
#                 side_effect=ClientError({'Error': {}}, 'DeleteMessage')
#             )
 
# Create a test function for MyClass format_name
def test_check_context(context):
    print("Context:", context)
    assert context == "Context initialized"
    # assert context == ["a", "b", "c", "d", "e", "f", "g"]
    # assert hasattr(x, "check")
    # assert isinstance(x, MyClass)
    # assert 0, context  # to show value

def test_usageerror():
    pytest.UsageError("usage error")

def test_skip():
    pytest.skip("skipping this test")

@pytest.mark.slow()
def test_slow():
    pass

def test_fail():
    pytest.fail("failing this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

# Use the raises helper to assert that some code raises an exception:
def test_raises():
    with pytest.raises(ValueError):
        raise ValueError("Invalid input")

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