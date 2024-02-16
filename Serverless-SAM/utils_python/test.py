import os
import time
from timeit import timeit
import datetime
import json
from pathlib import Path
import pathlib
import pydantic
from pydantic import BaseModel
import typing
from typing import Set, List, Dict, Union, Optional, Any #not necessary after Python 3.9


# list | None
# str | int
def getData(default: Any, key: Optional[dict] = None):
    pass

def myUnion(input: Union[str, int]) -> None:
    print(input)

def myUtil(mylist: str | None=None) -> None:
    return mylist

def time_this() -> None:
    time.sleep(2)
    for i in range(100000):
        i += 1

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
    nums = [x for x in range(10) if x % 2 == 0]
    print(nums)
    print(typing.TYPE_CHECKING)

    #total_time = timeit(time_this())
    #print(f"Total time: {total_time:.3f}")    

    char = "c"
    match char:
        case "a":
            print("a")
        case "b":
            print("b")
        case _:
            print("default")

if __name__ == "__main__":
    main()