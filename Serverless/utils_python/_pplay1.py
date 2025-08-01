# TODO
# __init__.py
# Zoom In: Command+Shift 0
# Zoom Out: Command -

# python --version
# pip -V

# pylint . --rcfile=.pylintrc .
# disable=all disable=invalid-name disable=missing-class-docstring (remove this line)

# safety scan --detailed-output --apply-fixes

# ruff format .
# ruff check . --fix
# ruff check test.py --config ruff.toml
# ruff check test.py --fix

# import argparse
# parser = argparse.ArgumentParser(description="sum the integers at the command line")
# parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),  help='log output config, default=sys.stdout') 
# parser.add_argument("query_text", type=str, help="The query text.")
# args = parser.parse_args()
# query_text = args.query_text

from typing import Self, Any, Optional, Final, Literal, LiteralString, Generic
from typing import Callable, Iterable, Iterator, AsyncIterable, Generator, Hashable
from typing import Type, NewType, TypeVar, TypeAlias, TypedDict, Required, NotRequired, ReadOnly
from typing import get_args, get_origin, get_type_hints, get_overloads

from collections import defaultdict, OrderedDict, deque, ChainMap, namedtuple

from typing import Annotated
from annotated_types import Gt, Ge, Le, Lt

from typing import Protocol, runtime_checkable, get_protocol_members # Python 3.8
from abc import ABC, abstractmethod

from uuid import uuid4, UUID # str(uuid4()) uuid.UUID(val)
from enum import StrEnum, IntFlag, auto

from functools import reduce, partial, cache, lru_cache, cached_property # cachetools(TTL)
from itertools import chain, cycle, batched, repeat, islice, combinations, permutations, pairwise, count, compress, accumulate, dropwhile, filterfalse

from decimal import Decimal, getcontext
from numbers import Number # isinstance(x, Number)

# print(eval("2*2"))
# func = eval("lambda x: x**x")
# result = func(2)
# exec("def func(x): return x+2")
# print(func(2))
# exec(compile(source="print('hello!')", filename="script.py", mode='eval'))

# pip freeze | grep -i llama
# cProfile py-spy flameGraph

# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv('.env')

# Load environment variables from .env file
# if not load_dotenv():
#     raise Exception("Failed to load .env file")

# OPEN_API_KEY = os.getenv("OPEN_AI_API_KEY")
# if not OPEN_API_KEY:
#     raise Exception("OPEN_API_KEY environment variable not set")

# print("================================")
# print(__name__)           # "__main__", "module/func name(inside func)"
# print(__class__)          #  = <class '__main__.MyClass'>
# print(__version__)        # requests.__version__
# print(__file__)           # requests.__file__ d:\VSCode\aws-templates\Serverless\utils_python\_pplay.py
# print(__package__)        # None
# print(__doc__)            # """module/func docstring"""
# print(__dict__)           # = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8c4c2d3a90>, '__spec__': ModuleSpec(name='aws-templates.Serverless.utils_python._pplay', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f8c4c2d3a90>, origin='aws-templates/Serverless/utils_python/_pplay.py'), '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'aws-templates/Serverless/utils_python/_pplay.py', '__cached__': None}
# print(__members__)        # Enum members
# print(__all__)            #  ("module1", "module2")
# print(__annotations__)    # {}
# print(__builtins__)       #  = <module 'builtins' (built-in)>
# print(__cached__)         #  None
# print(err.__traceback__)  # Last exception traceback - use in except
# print("================================")

# ================================================================================================================================

# __dict__ :  stores object/class writable attributes as a dictionary - can modify attributes dynamically
# Read-Only for Built-in Types: Built-in types like int or list do not have a modifiable __dict__
# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# obj = MyClass("Alice", 30)
# print(obj.__dict__)  # Output: {'name': 'Alice', 'age': 30}
# obj.__dict__['name'] = "Bob" # Modifying attributes dynamically
# print(obj.name)  # Output: Bob

# import pkg_resources
# installed_packages = [str(d) for d in pkg_resources.working_set] # # List all installed packages and their versions
# print("Installed packages:", installed_packages)

# -------------------------------------------------------------------------------------------------

# id len type isinstance issubclass str repr chr ord dir global nonlocal iter next 
# is in not and or not any all | is None is not None
# if elif try/except/else finally raise assert break continue pass return yield
# match/case/case _/default
# abs round sum min max pow avg floor ceil
# sorted reversed map filter zip enumerate
# getattr delattr setattr delattr
# / // & % **

# all(isinstance(my_cls, cls) for my_cls in classes)
# sum(item.value for item in items)
# filter(lambda x: x%3==0, list)
# functools.reduce(lambda a, i: a + i, my_list[1:], my_list[0])
# partial = functools.partial(my_func, 1, 2)
# partial(3) # calls my_func(1, 2, 3)
# @functools.wraps -> preserves __name__, __doc__ etc
# @functools.cache | lru_cache | cached_attribute(access via obj.argument)

# fib = [0, 1]
# while fib[-1] + fib[-2] < 100:
#     fib.append(fib[-1] + fib[-2])
# print(fib[::-1])

# -------------------------------------------------------------------------------------------------

# raise Exception("")
# raise RuntimeError("")
# raise SystemError("")
# raise ImportError("")
# raise NotImplementedError

# except ZeroDivisionError:
# logger.error("Error", exc_info=True | exc_info=e)
# logger.exception("Error with traceback")

# ================================================================================================================================

# class MyClass(Exception):
#     """ This is my nice Person class"""
#     _var = 0 # class variable - shared between all classes. self._var | cls._var | MyClass._var

#     # creates & returns a new instance, called before __init__
#     def __new__(cls, *args, **kwargs) -> Self: 
#         # print(f"__new__ called with {args} and {kwds}")
#         # return super().__new__(*args, **kwargs)
#         pass
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs) 
#         self.name = args[0] if args else None
#         self.instance_var = "InstanceVar"

#     # human-readable. Called by print() & str()
#     def __str__(self):
#         return f"{self.name} ({self.age} years old)"  # -> print(str(person)) Alice (30 years old) -> uses __str__

#     # developer-friendly. Can re-create the object. Used by the interpreter & debugge  
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"   # print(repr(person)) # Person('Alice', 30) -> uses __repr__

#     @property
#     def private_var(self):
#         return self.instance_var

#     @classmethod
#     def class_method(cls): # can access class variables/methods and static methods
#         cls._var = 4

#     @staticmethod
#     def static_method():
#         self.__class__(class_var=5)
#         MyClass.class_var = 5

#    # __radd__ : reverse add (other + self.value i.e. 3 + number)
#    def __add__(self, other): 
#        if type(self) is not type(other):
#            raise ValueError(f"Must be the same class to add: {self.__class__} and {other.__class__}")
#        return self.__class__(self.class_var + other.class_var)


# -------------------------------------------------------------------------------------------------
# import tqdm (loading..)

# print(sys.path)
# os.getenv("PYTHONPATH")
# for path in sys.path:
#     print("Path: " + path)
# sys.path.append(os.getcwd() + "/.venv/lib/python3.13/site-packages")
# sys.path.insert(0, str(Path(__file__).parent))
# sys.path.append(parent_dir)

# sys.stdin
# sys.stdout
# sys.stderr
# sys.version
# sys.version_info
# args:list[str] = sys.argv[:2]
# sys.getsizeof("abc")
# sys.exc_info()
# sys.exception()
# sys.exec_prefix
# sys.executable
# sys.excepthook
# sys.last_traceback
# sys.last_exc

# os.curdir
# os.cpu_count
# os.getcwd()
# os.listdir()
# os.getenv("DDB_TABLE", "table1")
# os.environ.get("DDB_TABLE", "table1")
# os.environ["POSTGRE_IP"]
# os.environ.setdefault("POSTGRE_PORT", 5432)

# os.path.basename(__file__)  # _pplay1.py
# os.path.dirname(__file__)   # D:\VSCode\aws-templates\Serverless\utils_python
# os.path.abspath(__file__)   # D:\VSCode\aws-templates\Serverless\utils_python\_pplay1.py
# os.path.realpath(__file__)  # D:\VSCode\aws-templates\Serverless\utils_python\_pplay1.py

# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# os.path.join(__file__, "test.txt")
# file_path = os.path.join(current_dir, filename)
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"File not found: {file_path}")
# os.path.split(os.path.abspath(__file__))[0]
# os.path.splitext("note.txt") -> txt
# os.path.expanduser(os.path.join("~", "myarchive"))
# os.makedirs("test", exist_ok=True)
# os.rmdir("test")
# os.chmod("test.txt", 0o777)
# os.chown(("test.txt", 1000, 1000)
# os.system("clear")
# os._exit(1)

# shutil.copytree("lambda", "build/lambda_package")
# shutil.make_archive("build/lambda", "zip", "build/lambda_package") # zip/tar
# shutil.rmtree("build/lambda_package")
# subprocess.run(["python", "app.py", "--docs_dir", "/docs")
# subprocess.check_call([
#     "pip",
#     "install",
#     "-r", "lambda/requirements.txt",
#     "-t", "build/lambda_package"
# ])
# exit(1)
# sys.exit(0)

# for dirpath, dirnames, filenames in os.walk('.'):
#     for filename in filename:
#         counter = 0
#         # print(os.path.join(dirname, filename))
#         if filename.endswith(".py"):
#             with open(os.path.join(dirname, filename), "r") as file:
#                 text = file.read()
#                 print(filename, len(text))

# for dirpath, dirnames, filenames in Path(__file__).parent.walk():
#     print(dirpath, dirnames, filenames)

# for p in Path(__file__).cwd().iterdir():
#     print(p.absolute())

# from pathlib import Path
# Path(__file__).cwd()
# Path(__file__).parent.joinpath("/data.txt")
# path.home().is_dir()
# path.resolve()
# path.absolute()
# path.mkdir(mode=0o777, parents=True, exist_ok=True)
# path.walk()
# path.glob("*.py")
# path.rglob("*.py")
# text = path.read_text("utf-8", errors="replace", newline="\n")
# data:bytes = path.read_bytes()
# text: str = data.decode("utf-8", errors="replace")

# from io import TextIOWrapper
# with path.open(mode="r", buffering=-1, encoding="utf-8", errors="replace", newline="\n") as file:
#     print(file.read(-1))

# -------------------------------------------------------------------------------------------------

# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(
#       level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
#       format="%(asctime)s %(levelname)-8s %(message)s %(name)s",
#       datefmt="%Y-%m-%d %H:%M:%S"
#     filename="app.log",
#     filemode="w", # overwrite the log file each time the program runs
#     stream=sys.stdout, # output to console
#     handlers=[
#         logging.StreamHandler(), 
#         logging.FileHandler("app.log", mode="w")], # overwrite the log file each time the program runs
#         logging.NullHandler(), # no output
#     ]
# )
# logger.info("Logging is set up.")
# logger.info("INFO", stack_info=True, stacklevel=5)
# logger.error("ERROR", exc_info=True)
# logger.exception(e)

# import traceback
# traceback.print_exception(type(err), err, err.__traceback__)
# traceback.print_exception(*sys.exc_info(), limit=5, file=sys.stdout)
# traceback.print_exc()

# -------------------------------------------------------------------------------------------------

# from datetime import datetime, timezone, timedelta
# datetime.now(timezone.utc).isoformat(timespec="seconds")
# datetime.now().strftime("%Y-%m-%d %H:%M:%S%z")
# datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# datetime.strptime(date_str[:10], "%Y-%m-%d").date()
# (datetime.now() - start_time).total_seconds()
# other_date = my_date + timedelta(hours=1, minutes=20)
# date.toisoformat/fromisoformat
# date.today()
# date.day
# date.month
# date.year

# import time
# time.sleep(1)
# time.time()
# time.perf_counter()
# time.time_ns()
# time.mktime((2024, 3, 24, 0, 0, 0, 0, 0, -1))
# time.localtime()
# time.gmtime()
# time.asctime((2024, 3, 24, 0, 0, 0, 0, 0, -1))
# time.strftime("%Y-%m-%d %H:%M:%S%z") #, time.localtime(epoch)
# time.strptime("2024-03-24", "%Y-%m-%d")
# time.monotonic()
# time.process_time() 
# time.thread_time()

# import timeit
# timeit.timeit("x = x**x", number=1000)
# timeit.repeat("x = x**x", repeat=3, number=1000)
# timeit.Timer("x = x**x").timeit(number=1000)
# timeit.Timer("x = x**x").repeat(repeat=3, number=1000)
# timeit.Timer("x = x**x").autorange()

# -------------------------------------------------------------------------------------------------

# print(str.__name__)
# import string
# string.digits, string.ascii_letters, string.punctuation, string.ascii_lowercase, string.ascii_uppercase, 
# b"\0AxhAu"
# r"db/data"
# u"unicode"

# print("{}".format(my_string))
# ("{0} {1}"").format(id, name)
# print("SELECT * FROM {table_name}".format(table_name=my_table))
# print("PK_%s" % id)
# print(f"PK_{id}")
# "Elapsed Time: {total_time:.2f}s"

# amount: str = 10_000_000
# name: str = "John"
# name.join("Doe")
# " ".encode(encoding="utf-8")
# ",".join(mylist)
# " ".split()
# " ".casefold()
# "".strip("\n```")
# " ".removeprefix("-")
# " ".removesuffix("-")
# "str".isdigit()
# "str".isalnum()
# "mr. s gokhan topcu".title()
# any(char in string.digits for char in "hello")

# -------------------------------------------------------------------------------------------------

# my_tuple: tuple[int, ...] = (1, ) + (2, 3)
# my_tuple: tuple[int, str] = (1, "Hello")
# my_tuple.index(1)
# my_tuple.count(1)

# my_set: set[int] = {0, 1, 2} | { 3, 4 } # set()
# if 0 in my_set | if 0 not in my_set 
# my_set.add(1)
# my_set.remove(1)
# my_set.discard(1)
# my_set.pop()
# my_set.update()
# my_set.union()
# my_set.copy()
# my_set.clear()
# my_set.issubset()
# my_set.issuperset()
# my_set.isdisjoint()
# my_set.difference() # set1-set2
# my_set.difference_update()
# my_set.intersection()
# my_set.intersection_update()
# my_set.symmetric_difference()
# my_set.symmetric_difference_update()

# my_list: list[int] = [0, 1, 2] + [3, 4]
# del my_list[0]
# my_list.append(3)
# my_list.extend([4, 5])
# my_list.insert(0, "A")
# my_list.pop()
# my_list.count(0)
# my_list.remove(0)
# my_list.copy()
# my_list.clear()
# my_list.sort(reverse=True)
# my_list.reverse()

# my_dict: dict[int, Any] = { 0:"A", 1:"B" } | { 2:"C" }
# my_dict2 = dict(one=1, two=2)
# del my_dict[0]
# my_dict.get(key="key", default=None)
# my_dict.pop(key="key", default=None)
# my_dict.popitem()
# my_dict.keys()
# my_dict.values()
# my_dict.items()
# my_dict.copy()
# my_dict.clear()
# my_dict.fromkeys(my_list)
# my_dict.setdefault(key="key", default=None)
# my_dict.update(my_dict)

# for _ in iter(my_list)
# my_list2 = [i for i in range(0,100,10) if not i%5==0]
# my_list3 = [*range(5)]
# my_list4 = list(range(5))
# matrix = [(x, y) for x in range(3) for y in range(3)]]
# flattened = [val for sublist in my_list for val in sublist]

# mylist = [1, 2, 3]
# print(*mylist)
# a, b, c = mylist
# mylist = [1, 2, 3, 4, 5]
# a, *b, c = mylist
# mylist3 = [*mylist1, *mylist2]

# my_dict: dict[str, Any] 
# my_dict = dict(name="David Bowie", age=86)
# my_func(**my_dict))
# combined_dict = {**my_dict1, **my_dict2}
# my_dict3 = { **my_dict1, "timestamp": 1234567890 }
# kwargs = {k: v for k, v in kwargs.items() if v is not None}

# from pprint import pprint
# pprint(my_dict, indent=4, sort_dicts=False)

# -------------------------------------------------------------------------------------------------

# def func() -> Literal["A", "B"]: ...
# def opt_func(val: int | None = None) -> int | None:
#     return val or None

# for _ in range(10,0,-1)
# def func(self, _) -> Iterable[str]: ...
# name, _, age = ("John", "dont need this", 30)

# my_lambda = lambda x: x * x
# PORT: Final[int] = 80080
# MODE = Literal['r', 'rb', 'w', 'wb']
# SQL = LiteralString('SELECT * FROM students')
# output: Annotated[list, my_func]

# def generics(cls: type[T], **kwargs) -> T:
# my_type: type = dict[str, Any]
# my_type: Type = int
# my_type: NewType = set[float] 
# my_type: TypeAlias = str
# my_type: TypeVar = list[int]

# from typing import get_args
# get_args(dict[str, int]) -> (str, int) 

# from numbers import Number
# T = TypeVar("T", bound=Number)
# T = TypeVar("T", bound="MyClass")

# if a==b and b==c or b==d
# if has_date = "start_date" in kwargs and "end_date" in kwargs
# return not True

# enum.name
# enum.value
# MyEnum.__members__ 
# MyEnum[enum_str]
# class MyStrEnum(StrEnum):
#     ASC = "ASCENDING"
#     def __str__(self) -> str:
#         return self.value

# class MyDict(TypedDict, total=False):
#     name: Required[str] = "default"
#     age: NotRequired[int] = 0
#     id: ReadOnly[uuid4] = uuid4()

# match record.event_name:
#     case DynamoDBRecordEventName.INSERT:
#     case _:
#     default: None

# import yaml
# with open(definition_path, "r") as f:
#   definition = yaml.safe_load(f)
# yaml.dump(definition)

# import pandas as pd
# df = pd.DataFrame(list)
# df.to_csv("output.csv")

# import numpy as np
# np.ones((3, 5))
# matrix = np.random.rand(3, 5)
# matrix = np.dot(10, matrix)

# -------------------------------------------------------------------------------------------------

# iterator:Iterator = iter(my_list)
# print(next(iterator)) # 1 2 3 StopIterationError

# # input can be generic, but return types should be specific
# def iterator_generator_func(input:Iterator[int]) -> Generator[int, None, None]: 
#     for i in range(5):
#         yield i
# iterator_generator_func((i for i in range(5)))
# iterator_generator_func([*range(5)])

# def generator():
#     yield 1
# print(next(generator))
# print(next(generator)) # StopIteration

# from contextlib import contextmanager, asynccontextmanager, AbstractContextManager
# @contextmanager -> enter() exit()
#  
# def some_generator(my_list:list):    
#     try:  
#         yield my_list.pop()
#     finally:  
#         print("Done")

# with some_generator([1,2,3]) as my_list:
#     print(my_list)

# -------------------------------------------------------------------------------------------------

# from typing import Protocol, runtime_checkable

# @runtime_checkable
# class MyProtocol(Protocol):
#     def __call__(self, x: int) -> int:
#         ...
#     def some_function(self, x: int) -> int: ...

# class GenProto[T](Protocol):  
#     def meth(self) -> T:  ...

# -------------------------------------------------------------------------------------------------

# if my_string is None or my_list is not None or 1 == 1:
#     pass # break continue

# def not_nasty(val: list[str] | None = None):
#     val = [] if val is None else val

# float('inf') #inf

# import random
# import string
# random_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
# print("random_str:" + random_str)

# r(default, error if not exists), r+(read/write), w/a(create if not exists), x(create, error if exists)
# b/t(default)
# with open("test.txt", "r+") as f:
#     f.write("Hello, World!")
    # f.read()
    # f.readlines()
    # f.readline()
    # f.writelines()
    # f.flush()
    # f.truncate(0)
    # f.seek(0)
    # f.tell()
    # f.close()
    # for line in f:
    #     print(line.strip())

# def my_func() -> Callable[[MyClass], bool]: ...
# def decorator(func: Callable[..., str]) -> None: ...
# def decorator(func) -> Callable[[int, int], int]: 
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         result = func(*args, **kwargs)
#         print("After function call")
#         return result
#     return wrapper

# @decorator
# def add_numbers(a: int, b: int) -> int: 
#     print(f"Adding {a} and {b}")
#     return a + b

# -------------------------------------------------------------------------------------------------

# from dataclasses import dataclass, Field, asdict, astuple, make_dataclass, is_dataclass, replace
# from pydantic import BaseModel, ConfigDict, Field, ValidationError
# cf.model_dump_json(by_alias=True, exclude_none=True)
# cf.model_validate()
# new_item = item.model_copy()
# cls.model_fields.get("id").get_default()
# typename: str = Field("DataSource", alias="__typename")) # must be serialised as __typename for graphql

# from decimal import Decimal, getcontext, setcontext
# setcontext(ExtendedContext)
# getcontext().prec = 3
# my_decimal = Decimal(1)
# print(my_decimal / Decimal(3))

# return { statusCode: 200, body: "Hello, World!" }

# -------------------------------------------------------------------------------------------------

# import orjson
# orjson.loads(body)

# with open("file.json", "r") as f:
#     data:dict[str, Any] = json.load(f)  # json.dump(f)

# my_dict = json.loads('{"name": "John", "age": 30, "money": 2.75}', parse_float=Decimal)
# json.dumps({"statusCode": 200, "body": "Hello, World!"}, sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False)
# json.dumps(my_dict, default=str)

# raises TypeError
# json.dumps({"key": "value"})    # {"key": "value"}
# json.dumps([1, 2, 3, "hello"])  # [1, 2, 3, "hello"]
# json.dumps("string")            # "string"
# json.dumps(3.14)                # 3.14
# json.dumps(True)                # true
# json.dumps(None)                # null

# # Using JSONEncoder
# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)

# json_string = json.dumps(data, cls=DateTimeEncoder)

# # Alternative: using default parameter
# json_string = json.dumps(data, default=datetime_serializer)
# def datetime_serializer(obj):
#     if isinstance(obj, datetime):
#         return obj.isoformat()
#     raise TypeError(f"Object {obj} is not JSON serializable")

# For Decimals:
# json.dumps(my_dict, default=decimal_serializer)
# def decimal_serializer(obj):
#     if isinstance(obj, Decimal):
#         return str(obj)  
#     raise TypeError(f"Type {type(obj)} is not JSON serializable")

# -------------------------------------------------------------------------------------------------

# import boto3, botoconfig, Session
# from botocore.exceptions import ClientError, ConditionCheckFailedException
# from boto3.dynamodb.conditions import Key, Attr
# from mypy_boto3_dynamodb.service_resource import Table
# client = boto3.resource("dynamodb")
# client = boto3.client(service_name="dynamodb", region_name="us-east-1")

# kwargs = { "Limit": 10, "ScanIndexForward": False } # gets the latest to oldest. index: A, B(str-ISO8601)
# while True:
#     response = table.scan(**kwargs)
#     count = response["Count"]
#     response["Items"] | response.get("Items", []) | response.get("Item")  
#     items.extend(response.get("Items", []))
#     if "LastEvaluatedKey" in response:
#       kwargs.update({"ExclusiveStartKey": response["LastEvaluatedKey"]})
#       kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
#     else:
#        break

# def lambda_handler(event, context):    
#     try:
#         item = json.loads(event["body"])
#         table.put_item(Item=item)
#         return {
#             'statusCode': 201 | 202 | 204,
#             'body': json.dumps("Created | Accepted | NoContent")
#         }
#     except ClientError as err:
#         logger.error(f"Error: {e}", exc_info=True)
#         logger.exception(e)
#         logger.error("Error Code: " + f"{err.response['Error']['Code']}")
#         logger.error("Error Message: " + f"{err.response['Error']['Message']}")
#         raise

# -------------------------------------------------------------------------------------------------

# import pytest
# from pytest import fixture
# from pytest_mock import mocker

# @fixture
# def mock_aws_client(mocker):
#     mock_client = mocker.patch("boto3.client")
#     mock_client.return_value = mocker.Mock()
#     return mock_client

# @fixture(scope="module")
# def lambda_context():
#     class LambdaContext:
#         def __init__(self):
#             self.function_name = "test_function"
#             self.function_version = "1.0"
#             self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
#             self.memory_limit_in_mb = 128
#             self.aws_request_id = "1234567890abcdef"
#             self.log_group_name = "/aws/lambda/test_function"
#             self.log_stream_name = "2023/10/01/[$LATEST]abcdef1234567890abcdef1234567890"
#             self.identity = None
#             self.client_context = None
#     return LambdaContext()

# @pytest.mark.parametrize("a, b, expected", [
#     (1, 2, 3),
#     (0, 0, 0),
#     (-1, 1, 0),
# ])
# def test_add_numbers():
#     assert add_numbers(-1, 3) == 2

# with(pytest.raises(pydantic.ValidationError)):
# def test_add_numbers_type_error():
#     with pytest.raises(TypeError):
#         add_numbers("5", 3) 

# -------------------------------------------------------------------------------------------------

# import asyncio # !!EventLoop!!
# from asyncio import TaskGroup, Task, create_task, Future, AbstractEventLoop, TimeoutError, CancelledError
 
# async def my_func(delay:float): # Coroutine[Any, Any, dict[str, str]]:
#     print(f"Waiting for {delay} seconds")
#     await asyncio.sleep(delay)
#     if delay == 4:
#         raise RuntimeError("Input validation failed")
#     return { "result": f"success - waited for {delay} seconds" }

# async def main():
    # coro = my_func(1) # does not start until awaited or used within a Task
    # result = await coro # await waits for coroutine to finish
    # print(result)

    # task1:Task = create_task(my_func(2))
    # task2:Task = create_task(my_func(4))
    # result1 = await task1 # await does not wait with tasks
    # result2 = await task2 # runs concurrently - like gather()
    # print(result1, result2) # only prints after both tasks are complete

    # result = asyncio.run(task)
    # task.add_done_callback()
    # task.cancel()
    # task.exception()
    # task.result()
    # await asyncio.Future()  # run forever
    # asyncio.get_running_loop() # get the running event loop, raise exception if there's none

    # coroutines = [task1(), task2()]
    # await asyncio.gather(*coroutines, return_exceptions=True) # runs concurrently
    # results:Future = await asyncio.gather(task1, task2, return_exceptions=True) # runs concurrently
    # for result in results:
    #     if isinstance(result, Exception):
    #         raise Exception("Error during async processing:" , result)
    #     print(result)

    # results = await asyncio.gather(*coroutines, return_exceptions=True)
    # err = None
    # for result, coro in zip(results, coroutines):
    #   if isinstance(result, Exception):
    #       err = result
    #       print(f"{coro.__name__} failed:")
    #       traceback.print_exception(type(err), err, err.__traceback__)
    #   if err:
    #       raise RuntimeError("One or more scripts failed.")

    # TaskGroup - provides error handling. If one task fails, all others are canceled
    # Only moves after the TaskGroup with block after all tasks are finished
    # async with asyncio.TaskGroup() as tg:
    #     task1 = tg.create_task(my_func(1))
    #     task2 = tg.create_task(my_func(2))
    # print("Both tasks have completed now.")

    # tasks = []
    # async with asyncio.TaskGroup() as tg:
    #     for i, sleep_time in enumerate([2, 1, 3], 1):
    #         task = tg.create_task(my_func(sleep_time))
    #         tasks.append(task)
    #         print(f"Scheduled task no {i}")
    
    # results = [task.result() for task in tasks]
    # for result in results:
    #     if isinstance(result, Exception):
    #         raise Exception("Error during async processing:" , result)
    #     print(result)


# Futures
# https://www.youtube.com/watch?v=Qb9s3UiMSTA&t=3s
# async def set_future_result(future, value):
#     await asyncio.sleep(2)
#     # Set the result of the future
#     future.set_result(value)
#     print(f"Set the future's result to: {value}")

# async def main():
#     loop:AbstractEventLoop = asyncio.get_running_loop() # get running event loop, raise exception if there's none
#     future:Future = loop.create_future()

#     # Schedule setting the future's result
#     asyncio.create_task(set_future_result(future, "Future result is ready!"))

#     # Wait for the future's result
#     result = await future
#     print(f"Received the future's result: {result}")


# Synchronization
# shared_resource = 0
# lock = asyncio.Lock()

# async def main():
#     global shared_resource    
#     try:
#         print("Locking..")
#         await lock.acquire()
#         print("Lock acquired")
#         await asyncio.sleep(2)
#     finally:
#         lock.release()
#         print("Lock released")

#     # auto lock.acquire & release
#     async with lock:  
#         print("Lock acquired")
#         await asyncio.sleep(2)
#     print("Lock released")

# Semaphore
# async def access_resource(semaphore, resource_id):
#     async with semaphore:
#         # Simulate accessing a limited resource
#         print(f"Accessing resource with id {resource_id}")
#         await asyncio.sleep(2)
#     print(f"Releasing resource with id {resource_id}")

# async def main():
#     semaphore = asyncio.Semaphore(2) # Allow 2 concurrent access
#     await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

# Event
# async def waiter(event):
#     print("Waiting for the event to be set..")
#     await event.wait() # waits until event.set() is called
#     print("Event has been set, exiting waiter")

# async def setter(event):
#     await asyncio.sleep(2)
#     event.set()
#     print("Event has been set")

# async def main():
#     event = asyncio.Event()
#     await asyncio.gather(waiter(event), setter(event))
    

# if __name__ == "__main__":    
#     print("Running..")
#     asyncio.run(main())
