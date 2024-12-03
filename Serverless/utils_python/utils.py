
import os
import time
import timeit
#import profile
import uuid
import json
import jsonpickle
from typing import Any
import random

# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
# from dotenv import load_dotenv, find_dotenv 
# load_dotenv(find_dotenv())
# load_dotenv(dotenv_path=ENV_FILENAME)
# if not load_dotenv(find_dotenv()):
#     raise Exception("Failed to load .env file")
# print(os.getenv('DDB_TABLE'))
# os.environ.get("DDB_TABLE")
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, filename)

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

def timeit_test() -> None:
    pass
    # time.perf_counter()
    # time.perf_counter_ns()
    # print(f"Total: {(time.time() - start):.3f}s")
    # print(f"Total: {(time.perf_counter() - start) * 1000} ms")
# if __name__ == "__main__":
    # timed: float = timeit.timeit(stmt="sleep(1)", setup="import random", timer=time.perf_counter, number=2, globals=globals())
    # print(f"Total: {timed:.3f}s")
    # print(f"Total: {round(timed, 1)}s")
    # timed_list: list[float] = timeit.repeat(stmt="sleep(1)", setup="import random", timer=time.time, number=1, repeat=3, globals=globals())
    # print(f"Total: {min(timed_list):.3f}")

def generate_uuid():
    return str(uuid.uuid4())

def generate_random_number():
    return random.randint(1, 100) # random.random()
    # rstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

# https://docs.python.org/3/glossary.html#term-file-object
def write_file(filename, content):
    with open(filename, "w") as file: # wb
        # file.writelines(content)
        file.write(content)
        # file.flush()

def read_file_curr_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r') as file:
        # return json.load(file)
        return file.read()

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
            # lines = file.readlines(3) # read 3 lines
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
    with open(file, "r", encoding="utf-8") as file:
        # (object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
        return json.load(file)

def json_loads(input) -> Any:
    return json.loads(input)
    # except json.JSONDecodeError:
    #   print("Message is not JSON format")  
    
def json_dumps(obj: object, formatted: bool) -> str:
    if formatted:
        return json.dumps(obj, indent=4, sort_keys=True, separators=(". ", " = "))
    #allow_nan, default, cls, skip_keys
    return json.dumps(obj) 

def json_dump(obj: object, file, formatted: bool) -> None:
    with open(file, "w", encoding="utf-8") as file:
        if formatted:
            json.dump(obj, file, indent=4, sort_keys=True, separators=(". ", " = "))
        else:
            json.dump(obj, file)
    
# def save_document_to_json(file_name, doc: Document):
#     jobj = jsonpickle.encode(doc)
#     with open(file_name, 'w') as f:
#         f.write(jobj)
#         f.close()

# def load_document_from_json(file_name):
#     with open(file_name, 'r') as f:
#         jobj = f.read()
#         f.close()
#         doc = jsonpickle.decode(jobj)
#         if not isinstance(doc, Document):
#             raise Exception('Document type is not correct')
#         return doc