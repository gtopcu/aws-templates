import sys
from sys import getsizeof
import os
import uuid
import json
from datetime import datetime, date, time, UTC
import dateutil
import time
import pathlib
from pathlib import Path
from dotenv import load_dotenv


def get_docstring(input1: int) -> str
    """
    Sample function docstring

    :param input1: Input integer
    :return: Returns docstring as str
    """
    return __doc__

def load_dotenv() -> None:
    # Imports .env file
    load_dotenv()

def get_env(env_name: str, default:str | None) -> str | None:
    return os.getenv(env_name, str)    
    #os.environ.get(env_name, default)

def sleep(seconds: int) -> None:
    time.sleep(seconds)

def get_perf_counter() -> float:
    return time.perf_counter
    # time.perf_counter_ns()

def generate_uuid():
    return str(uuid.uuid4())

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename) -> str:
    with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    # try:
    #     file = open(file=filename, mode="r", encoding="UTF-8")
    # except IOError as e:
    #     raise e
    # else:
    #     return file.read()
    # finally:
    #     if file is not None:
    #         file.close()
    
def dump_JSON(dict: object) -> str:
    return json.dumps(object, indent=4, sort_keys=True, separators=(". ", " = "))
    
