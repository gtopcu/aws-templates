import sys
from sys import getsizeof
import os
import uuid
import json
from datetime import datetime, date, time
import time
import pathlib
from pathlib import Path
from dotenv import load_dotenv

# sys.argv
# sys.path.insert(0, '/tmp/mydir')
# sys.exit(0) - Raises SystemExit exception, finally & cleanups run
# os._exit(0) - Immediate kill, no finals/cleanups run. Only POSIX files are closed

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
    
def os_get_cwd() -> str:
    os.getcwd()
    # os.listdir('.')
    # os.path.dirname(__file__)

def os_path_join(current_path:str, filename:str) -> str:
    return os.path.join(current_path, filename)
    # Path.joinpath(current_path, filename)

def os_path_isdir(path: str) -> bool:
    return os.path.isdir(path)

def pathlib_current_path() -> pathlib.Path: 
    return pathlib.Path(__file__)
    #print(__file__)
    #print(Path().absolute())
    #print(pathlib.Path(__file__).parent / "events.json")

def datetime_now(format: str = "%Y-%m-%dT%H:%M:%SZ"): #ISO8601 
    return datetime.datetime.now().strftime(format)
    datetime.datetime(2020, 5, 17) hour, minute, second, microsecond, tzone=None
    # datetime.datetime.now() + datetime.timedelta(days=1, hours=2)
    # print(now.isoformat())
    # print(now.strftime("%Y-%m-%d %H:%M:%S"))
    # print(now.astimezone())
    # print(f"{now:%Y-%m-%dT%H:%M:%SZ}") #ISO8601 
    # print(f"{now:%d/%m/%y (%H:%M:%S)}")
    # print(f"{now:%c}") #local
    # print(f"{now:%I%p}") #AM/PM

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
    try: 
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except IOError as e:
        raise e
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
    
