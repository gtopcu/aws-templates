import os
import time
import datetime
import json
from pathlib import Path
import pathlib
import pydantic
from pydantic import BaseModel
from typing import Set, List, Dict, Union, Optional, Any #not necessary after Python 3.9


# list | None
# str | int
def getData(default: Any, key: Optional[dict] = None):
    pass

def myUnion(input: Union[str, int]) -> None:
    print(input)

def myUtil(mylist: str | None=None) -> None:
    return mylist

def main() -> None:
    print(os.getcwd())
    print(os.listdir('.'))
    print(Path().absolute())
    #print(datetime.datetime.now())
    #print(dir(int))
    #print(__file__)
    #print(pathlib.Path(__file__).parent / "examples")
    x, y = 3, 4
    print(x, y)

if __name__ == "__main__":
    main()