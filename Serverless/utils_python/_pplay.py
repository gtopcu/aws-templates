# TODO
# Amazon Q: Command + i
# Zoom In: Command+Shift 0
# Zoom Out: Command -

# python -m venv .venv
# source .venv/bin/activate
# source /Users/mac/GoogleDrive/VSCode/.venv/bin/activate
# pip -V
# pip install -U boto3

# pylint . --rcfile=.pylintrc .
# disable=all disable=invalid-name disable=missing-class-docstring (remove this line to get 

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
# class myPersonClass:
#     """ This is my nice Person class"""

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


# from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias, TypedDict, Callable
# from collections import namedtuple, deque, OrderedDict, defaultdict
# from collections.abc import Mapping, Sequence, Set, Generator, Callable, Iterable, Iterator, AsyncIterable
# my_dict: dict[str, Any]

# __init__.py
# __all__ = ("module1", "module2")
# from .module import func
# dir(module)

import logging
import os
import sys

# and or any all del len id type sorted reversed enumerate zip filter map reduce 
# is/not in/not any/all instanceof round floor min max avg pow sum
# print(str.__name__)
# import string
# string.ascii_letters

# args:list[str] = sys.argv[:2]
# sys.getsizeof("abc")
# sys.version
# sys.version_info

# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# os.getenv("PYTHONPATH")
# for path in sys.path:
#     print("Path: " + path)
# sys.path.append(os.getcwd() + "/.venv/lib/python3.13/site-packages")
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
# datetime.now(timezone.utc).isoformat(timespec="seconds")
# my_date + timedelta(hours=1)
# time.time()
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
# shutil.rmtree("build/lambda_package")
# shutil.make_archive("build/lambda", "zip", "build/lambda_package") # zip/tar
# subprocess.check_call([
#     "pip",
#     "install",
#     "-r", "lambda/requirements.txt",
#     "-t", "build/lambda_package"
# ])

# logger = logging.getLogger(__name__)
# logger.info("test")

# exit(1)

# class Cat:
#     def __new__(cls, name: str) -> None:
#         print(cls, name, "new")
#         super().__new__(cls)
#         isinstance(cls, Cat)
#         print(cls, name, "new")

#     def __init__(self, name:str) -> Self:
#         self.name = name
#         print("init")

# mycat = Cat("duman")
# print(mycat.name)

# name: str = "John"
# name.join("Doe")
# print("PK_%s" % ID)
# "request: {}"".format(json.dumps(event))
# " ".removeprefix("")
# " ".removesuffix("")
# ",".join(mylist)
# " ".casefold()
# " ".strip()
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

# pip install python-json-logger
# from pythonjsonlogger.json import JsonFormatter
# json_formatter = JsonFormatter()
# json_formatter.format(record=None, request=None, response=None, exception=None, extra=None)

