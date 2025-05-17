

# Zoom In: Command+Shift 0
# Zoom Out: Command -

# Cursor: Command + K

# Amazon Q:
#   @workspace @git @history @env
#   /clean /doc /dev /test /review /transform
#   Inline Chat: Command + i 
#   Code complete: Option + C
#   Tab: Display all options
#   Left arrow to accept autocompletion

# GitHub Copilot(Ask/Edit/Agent modes): 
# @workspace @terminal @github @vscode 
# #codebase #file #folder #changes #fetch #problems #searchResults #findTestFiles #testFailure
# /help /clear /search /explain /new /fix /tests /startDebugging

# Command + i                  -> Inline Chat
# Command + Option + i         -> Sidebar Chat
# Option + ]                   -> Next Suggestion
# Option + [                   -> Previous Suggestion
# Command + Option + Shift + c -> Code Complete
# Command + Option + Shift + e -> Explain Code
# Command + Option + Shift + t -> Test Code
# Command + Option + Shift + f -> Fix Code
# Command + Option + Shift + d -> Debug Code
# Command + Option + Shift + s -> Search Code
# Command + Option + Shift + r -> Refactor Code
# Command + Option + Shift + a -> Ask Code
# Command + Option + Shift + o -> Open Code
# Command + Option + Shift + n -> New Code
# Command + Option + Shift + p -> Paste Code
# Command + Option + Shift + l -> List Code
# Command + Option + Shift + x -> Execute Code
# Command + Option + Shift + y -> Copy Code

# TODO
# When you run a Python file directly, __name__ is set to "__main__"
# When you import the file as a module, __name__ is set to the module's name
# __name__ = "__main__"
# __all__ = ("module1", "module2")
# __class__
# __file__
# __package__
# __doc__
# __annotations__
# __builtins__
# __dict__

# pylint . --rcfile=.pylintrc .
# disable=all disable=invalid-name disable=missing-class-docstring (remove this line)

# safety scan --detailed-output --apply-fixes

# ruff format .
# ruff check . --fix
# ruff check test.py --config ruff.toml
# ruff check test.py --fix

# """
# This better get 10/10!
# https://www.youtube.com/watch?v=RqdhVaX50mc
# """
# CamelCase(PascalCase) / snake_case
# class MyPersonClass:
#     """ This is my nice Person class"""

#     def __new__(cls, name:str) -> Self:
#         return MyPersonClass(name)

#     def __init__(self, name: str) -> None:
#         self.name = name

#     def get_name(self) -> str:
#         """
#         Returns the name of the person
#         :return: The name of the person
#         :rtype: str
#         """
#         """
#         Returns the name of the person
#         Args:
#             self: Current instance
#         Returns:
#             name: The name of the person
#         Raises:
#             ValueError: If name is not a string
#         """
#         return self.name

# BaseException ->     
#   Exception -> SystemExit     
#   StandardError -> ValueError: int("A"), KeyError: dict['key1'], TypeError: str[0]="a",
#   IndexError, AttributeError, NameError, AssertionError, StopIterationError, ArithmeticError,     
#   ZeroDivisionError, NotImplementedError, RuntimeError, SystemError

# from typing import Self, Any, Optional, Final, Literal, LiteralString, NewType, Type, TypeVar, TypeAlias, TypedDict, Generic
# from typing import Awaitable, Callable, Iterable, 
# from collections import namedtuple, deque, OrderedDict, defaultdict
# from collections.abc import Mapping, Sequence, Set, Generator, Callable, Iterable, Iterator, AsyncIterable

# my_dict: dict[str, Any] 
# PORT: Final[int] = 80080
# from typing import Literal, LiteralString
# MODE = Literal['r', 'rb', 'w', 'wb']
# SQL = LiteralString('SELECT * FROM students') # to avoid SQL injection

# __init__.py
# __all__ = ("module1", "module2")
# from .module import func
# dir(module)

# import logging
# import os
# import sys
# import json

# try:
#     cache = json.load(open("cache.json"))
# except (json.JSONDecodeError, FileNotFoundError):
#     cache = {}
#     raise
# finally:
#     json.dump(cache, open("cache.json", "w"))

# id len type isinstance issubclass str repr chr ord dir global nonlocal iter next 
# is in not and or not any all 
# if elif else try except finally raise assert break continue pass return yield
# abs round sum min max pow avg floor ceil
# sorted reversed map filter reduce zip enumerate
# getattr delattr setattr 

# print(str.__name__)
# import string
# string.digits, string.ascii_letters, string.punctuation, string.ascii_lowercase, string.ascii_uppercase, 

# args:list[str] = sys.argv[:2]
# sys.getsizeof("abc")
# sys.version
# sys.version_info

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# traceback.print_exception(type(err), err, err.__traceback__)

# from pprint import pprint
# bowie = dict(name="David Bowie", age=86)
# pprint(bowie, indent=4, sort_dicts=False)

# os.getenv("PYTHONPATH")
# for path in sys.path:
#     print("Path: " + path)
# sys.path.append(os.getcwd() + "/.venv/lib/python3.13/site-packages")
# sys.path.insert(0, str(Path(__file__).parent))
# os.path.join(__file__, "test.txt")

# Add the parent directory to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# sys.path.append(parent_dir)

# from pathlib import Path
# Path(__file__).resolve().parent.is_dir()
# Path(__file__).absolute().joinpath("..").mkdir(mode=0o777, parents=True, exist_ok=True)
# print(Path.home())
# print(Path.cwd())

# from datetime import datetime, timezone, timedelta
# import time
# datetime.now(timezone.utc).isoformat(timespec="seconds")
# my_date + timedelta(hours=1)
# time.time()
# time.sleep(2)
# time.strftime("%Y-%m-%d %H:%M:%S")
# time.perf_counter()
# datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# time.strptime("2024-03-24", "%Y-%m-%d")
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# date.today()
# date.day
# date.month
# date.year
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# birthday = datetime.strptime("2020-07-24", "%Y-%m-%d").date()
# age = (date.today() - birthday).days // 365
# print(age)

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

# os.getenv("DDB_TABLE", "table1")
# os.environ.get("DDB_TABLE", "table1")
# POSTGRE_IP = os.environ["POSTGRE_IP"]
# POSTGRE_PORT: int = os.environ.setdefault("POSTGRE_PORT", 5432)

# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, filename)
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"File not found: {file_path}")
# os.path.split(os.path.abspath(__file__))[0]
# os.path.splitext("note.txt") -> txt
# os.path.basename(__file__)
# os.path.expanduser(os.path.join("~", "myarchive"))
# os.getcwd()
# os.listdir()
# os.makedirs("test", exist_ok=True)
# os.rmdir("test")
# os.chmod("test.txt", 0o777)
# os.chown(("test.txt", 1000, 1000)
# os.system("clear")
# print(__name__)
# print(__file__)

# shutil.copytree("lambda", "build/lambda_package")
# shutil.make_archive("build/lambda", "zip", "build/lambda_package") # zip/tar
# shutil.rmtree("build/lambda_package")
# subprocess.check_call([
#     "pip",
#     "install",
#     "-r", "lambda/requirements.txt",
#     "-t", "build/lambda_package"
# ])


# exit(1)
# sys.exit(0)

# name: str = "John"
# name.join("Doe")
# print("PK_%s" % ID)
# "request: {}"".format(json.dumps(event))
# " ".removeprefix("")
# " ".removesuffix("")
# ",".join(mylist)
# " ".casefold()
# " ".strip()
# "str".isdigit()
# "str".isalnum()
# "mr. gokhan topcu".title()
# any(char in string.digits for char in pw)

# myset = {1, 2, 3}
# myset = myset | {3, 4}
# myset.add(2)
# myset.remove(1)
# myset.discard(1)
# myset.difference({1, 2})
# myset.intersection({1, 2})
# myset.issubset({1, 2, 3})
# myset.union({1, 2, 3, 4})
# myset.update({1, 2, 3, 4})
# myset = filter(lambda x: x/2==1, myset)
# sorted = sorted(myset, reverse=True)
# print(sorted)

# for i, j in enumerate(myset, 1):
#     print(i, j)

# Pack-unpack
# https://www.youtube.com/watch?v=-mS7K2K1IWk

# mylist = [1, 2, 3]
# print(*mylist)
# a, b, c = mylist
# print(a, b, c)
# mylist = [1, 2, 3, 4, 5]
# a, *b, c = mylist
# print(a, b, c)

# mylist1 = [1, 2, 3]
# mylist2 = [4, 5, 6]
# mylist3 = [*mylist1, "combined", *mylist2]
# print(mylist3)

# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# my_dict = {"a": 1, "b": 2, "c": 3}
# my_func(**my_dict)

# def my_func2(a: int, b: int, c: int):
#     print(a, b, c)
# my_func2(**my_dict)

# my_dict1 = {"a": 1, "b": 2, "c": 3}
# my_dict2 = {"d": 4, "e": 5, "f": 3}
# combined_dict = {**my_dict1, **my_dict2}
# print(combined_dict)
# my_dict3 = { **my_dict1, "timestamp": 1234567890 }

# def my_func3(**kwargs) -> None:
#     kwargs["a"] = 10
#     print(kwargs)
#     if "b" in kwargs:
#         print("b exists")
# my_func3(**combined_dict)

# mylist.extend([4, 5])
# mylist2 = list[dict[str, Any]]
# mylist2.append({"a": 1, "b": 2})

# mydict = {"a": 1, "b": 2, "c": 3}
# d = mydict.get("d", 4)
# d = mydict.pop("d", 4)
# i, j = mydict.popitem()
# mydict.fromkeys(list, 0)
# mydict.setdefault("d", 4)
# mydict.update({"d": 4})
# mydict.clear()

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(f"Error during operation: {str(e)}")

# matrix = [(0, 0), (0, 1), (0, 2),
#           (1, 0), (1, 1), (1, 2),
#           (2, 0), (2, 1), (2, 2)]

# matrix = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]

# for row, col in matrix:
#     print(row, col)

# my_list = [[x, y] for x in range(3) for y in range(3)]
# print(my_list)
# flattened = [val for sublist in my_list for val in sublist]
# print(flattened)

