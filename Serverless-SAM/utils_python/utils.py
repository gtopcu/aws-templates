import os
import uuid
import json
import datetime, time
from pathlib import Path

def osGetCwd() -> str:
    os.getcwd()
    #Path().absolute()

def osListCurrentDir() -> list[str]:
    return os.listdir('.')

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
    with open(filename, "r") as file:
        return file.read()
    
