
from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias, TypedDict
from typing import Callable, Iterable, Iterator
from collections import namedtuple, deque, OrderedDict, defaultdict, ChainMap


class MyClass(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        print(__class__)

my_class = MyClass("Hello")

import traceback
from inspect import istraceback
import sys

sys.exc_info()
sys.exception()
sys.exec_prefix
sys.executable
sys.excepthook
sys.last_traceback
sys.last_exc
sys.stdin
sys.stdout
sys.stderr

traceback.print_exception(*sys.exc_info(), limit=5, file=sys.stdout)
traceback.print_exc()
traceback.print_last()
traceback.print_stack()
traceback.print_tb(limit=5)
traceback.extract_tb(limit=5)
traceback.walk_tb(limit=5)
traceback.extract_stack()
traceback.format_exception(limit=5, chain=True)
traceback.format_exception_only()
traceback.format_exc()
traceback.format_stack(limit=5)
traceback.format_tb(limit=5)
traceback.format_list()
traceback.format_stack()
traceback.format_tb()
traceback.clear_frames()

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
      level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
      format="%(asctime)s %(levelname)-8s %(message)s %(name)s",
      datefmt="%Y-%m-%d %H:%M:%S"
#     filename="app.log",
#     filemode="w", # overwrite the log file each time the program runs
#     stream=sys.stdout, # output to console
#     handlers=[
#         logging.StreamHandler(), 
#         logging.FileHandler("app.log", mode="w")], # overwrite the log file each time the program runs
#         logging.NullHandler(), # no output
#     ]
)
logger.info("Logging is set up.")
logger.info("INFO", stack_info=True, stacklevel=5)
logger.error("ERROR", exc_info=True)

import time
print(time.time()) 
print(time.strftime("%H:%M:%S%z"))
time.localtime()
time.perf_counter()

# raise Exception("")
# raise RuntimeError("")
# raise SystemError("")

# id len type isinstance str repr chr ord dir global nonlocal iter next 
# is in not and or not any all 
# if elif else try except finally raise assert break continue pass return yield
# abs round sum min max pow avg floor ceil
# sorted reversed map filter reduce zip enumerate
# getattr delattr setattr 

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str] = (1, "Hello")
my_tuple2: tuple[int, ...] = (1, )
my_dict: dict[str, int] = {"one": 1, "two": 2}
del my_dict["one"]
my_dict2: dict[str, int] = dict(one=1, two=2)
my_set: set[int] = {1, 2, 3}
my_string: str = "Hello, World!"

my_list2 = [i for i in range(0,100,10) if i%5==0]
my_list3 = [*range(5)]
print(my_list3)
my_list4 = list(range(5))
print(my_list4)

my_lambda = lambda x: x * x

iterator:Iterator = iter(my_list)
print(next(iterator)) # 1

if my_string is None or my_list is not None or 1 == 1:
    pass # break continue


def nasty(val=[]):
    val.append(1)

def not_nasty(val=None):
    val = [] if val is None else val

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

# import boto3
# from botocore.exceptions import ClientError, ConditionCheckFailedException
# client = boto3.client(service_name="dynamodb", region_name="us-east-1")
# try:
#     client.put_item()
# except botocore.exceptions.ClientError as e:
#     print(f"Error putting item: {e}")
#     raise e
#     err.response["Error"]["Code"]
#     err.response["Error"]["Message"]

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
from pytest import fixture
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

