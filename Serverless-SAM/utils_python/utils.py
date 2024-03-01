import os
import uuid
import json
from datetime import datetime, date, time
import time
import pathlib
#from pathlib import Path
from dotenv import load_dotenv

def load_dotenv() -> None:
    # Imports .env file
    load_dotenv()

def get_env(env_name: str, default:str) -> str:
    return os.getenv(env_name, str)    
    
def os_get_cwd() -> str:
    os.getcwd()
    #os.listdir('.')

def os_path_join(current_path:str, filename:str) -> str:
    return os.path.join(current_path, filename)

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

def sleep(seconds: int) -> None:
    time.sleep(seconds)

def get_perf_counter() -> float:
    return time.perf_counter

def generate_uuid():
    return str(uuid.uuid4())

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
def parsed_JSON(dict: object) -> str:
    return json.dumps(object, indent=4, sort_keys=True, separators=(". ", " = "))
    
