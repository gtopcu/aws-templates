import os
import time, datetime
import json
from pathlib import Path
import pathlib
import pydantic
from pydantic import BaseModel
from typing import List, Dict, Optional, Any


# list | None
# str | int
def getData(default: Any, key: Optional[dict] = None):
    pass


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