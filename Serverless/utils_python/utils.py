
import uuid
import json
import time
from typing import Any
from dotenv import find_dotenv
from dotenv import load_dotenv

# pip install python-dotenv
# from dotenv import load_dotenv, find_dotenv 
# load_dotenv(find_dotenv())
# if not load_dotenv(find_dotenv()):
#     raise Exception("Failed to load .env file")
# print(os.getenv('DDB_TABLE'))

def get_docstring(input1: int) -> list[str]:
    """
    Sample function docstring

    Args:
        input1 (int): Input integer
    Returns:
        list[str]: Returns response as list of strings

    :param input1: Input integer
    :return: Returns docstring as str
    """
    return __doc__

def sleep(seconds: int) -> None:
    time.sleep(seconds)

def get_perf_counter() -> float:
    return time.perf_counter
    # print(f"Total: {(time.time() - start):.3f}s")
    # print(f"Total: {(time.perf_counter() - start) * 1000} ms")
    # time.perf_counter_ns()

def generate_uuid():
    return str(uuid.uuid4())

# https://docs.python.org/3/glossary.html#term-file-object
def write_file(filename, content):
    with open(filename, "w") as file: # wb
        # file.writelines(content)
        file.write(content)
        # file.flush()

# r(default, error if not exists), r+(read/write), w/a(create if not exists), x(create, error if exists)
# b/t(default)
def read_file(filename) -> str:
    with open(filename, "r", encoding="utf-8") as file: 
            # file.encoding
            # file.mode
            # file.closed
            # os.rename(filename, "test.txt")
            # os.remove("test.txt")
            # os.rmdir()
            # for line in file:
            #     print(line)
            # file.seek(26)
            # file.tell()
            # file.readline(10) # read 10 chars from line
            # lines: file.readlines(3) # read 3 lines
            # file.read(10) # read 10 chars
            return file.read()
    
        # file = open("data.txt", "r", encoding="utf-8")
        # for line in file:
        #     print(line)
        # file.close()

        # with path.open() as f:
        #     return json.load(f)

        # try:
        #     file = open(file=filename, mode="r", encoding="UTF-8")
        # except IOError, FileNotFoundError as e:
        #     raise e
        # else:
        #     return file.read()
        # finally:
        #     if file is not None:
        #         file.close()

def json_load(file) -> Any:
    with open(file, "r", encoding="utf-8") as f:
        # (object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
        return json.load(f)

def json_loads(input) -> Any:
    return json.loads(input)
    
def json_dumps(dict: object, formatted: bool) -> str:
    if formatted:
        return json.dumps(dict, indent=4, sort_keys=True, separators=(". ", " = "))
    #allow_nan, default, cls, skip_keys
    return json.dumps(dict) 

def json_dump(dict: object, file, formatted: bool) -> None:
    with open(file, "w", encoding="utf-8") as f:
        if formatted:
            json.dump(dict, f, indent=4, sort_keys=True, separators=(". ", " = "))
        else:
            json.dump(dict, f)
    
