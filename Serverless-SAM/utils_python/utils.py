import os
import uuid
import json
import datetime
import time
#from pathlib import Path

def osGetCwd() -> str:
    os.getcwd()
    #os.listdir('.')
    #print(__file__)
    #print(Path().absolute())
    #print(pathlib.Path(__file__).parent / "examples")

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def sleep(seconds: int):
    time.sleep(seconds)

def getPerfCounter() -> float:
    return time.perf_counter

def generate_uuid():
    return str(uuid.uuid4())

def writeFile(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def readFile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
def parsedJSON(dict: object) -> str:
    return json.dumps(object, indent=4, sort_keys=True, separators=(". ", " = "))
    
