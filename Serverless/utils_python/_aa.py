
from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias, TypedDict
from collections import namedtuple, deque, OrderedDict, defaultdict, ChainMap
from collections.abc import Callable, Iterable, Iterator

class MyClass(Exception):
    def __init__(self, *args):
        super().__init__(*args)

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("Logging is set up.")

import time
print(time.time()) 
print(time.strftime("%H:%M:%S%z"))
time.localtime()
time.perf_counter()

# raise Exception("")
# raise RuntimeError("")
# raise SystemError("")

# id len type isinstance repr
# iter next 
# any all chr ord 
# abs round sum min max pow
# sorted reversed filter map reduce zip enumerate
# getattr delattr setattr 

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str] = (1, "Hello")
my_tuple2: tuple[int, ...] = (1, )
my_dict: dict[str, int] = {"one": 1, "two": 2}
my_set: set[int] = {1, 2, 3}
my_string: str = "Hello, World!"

my_list2 = [i for i in range(0,100,10) if i%5==0]
my_list3 = [*range(5)]
print(my_list3)
my_list4 = list(range(5))
print(my_list4)

def nasty(val=[]):
    val.append(1)

def not_nasty(val=None):
    val = [] if val is None else val

my_lambda = lambda x: x * x

if my_string is None or my_list is not None or 1 == 1:
    pass # break continue

def add_wrapper(func) -> Callable[[int, int], int]:
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@add_wrapper
def add_numbers(a: int, b: int) -> int: 
    print(f"Adding {a} and {b}")
    return a + b

def main() -> None:
    print("{}".format(my_string))
    print("so, %s" % my_string)
    print(f"so, {my_string}")

    print(my_lambda(10))

    for i in "123456":
        print(i, end="-")
    print("\n")
        
    add_numbers(1, 2)

if __name__ == "__main__":
    main()


# ====================================================================================

import pytest
from pytest import decorator, fixture, mark, raises
from pytest_mock import mocker

@fixture(scope="module")
def mock_aws_client(mocker):
    mock_client = mocker.patch("boto3.client")
    mock_client.return_value = mocker.Mock()
    return mock_client

@fixture(scope="module")
def lambda_context():
    class LambdaContext:
        def __init__(self):
            self.function_name = "test_function"
            self.function_version = "1.0"
            self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
            self.memory_limit_in_mb = 128
            self.aws_request_id = "1234567890abcdef"
            self.log_group_name = "/aws/lambda/test_function"
            self.log_stream_name = "2023/10/01/[$LATEST]abcdef1234567890abcdef1234567890"
            self.identity = None
            self.client_context = None
    return LambdaContext()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_numbers():
    assert add_numbers(-1, 3) == 2

def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers("5", 3) 

