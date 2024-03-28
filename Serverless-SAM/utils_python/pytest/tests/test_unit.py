
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

# scope: function(default), class, module, package, session
@pytest.fixture(scope="module") # autouse=True
def context():
    return "Context initialized"

# # Create a test function for MyClass format_name
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

def test_fail():
    pytest.fail("failing this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

@pytest.mark.slow()
def test_slow():
    pass

# Use the raises helper to assert that some code raises an exception:
def raise_exception():
    raise SystemExit(1)

def test_raises():
    with pytest.raises(SystemExit):
        raise_exception()