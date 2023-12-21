import os
import time, datetime
import json
from pathlib import Path
import pydantic
from pydantic import BaseModel
from typing import List, Dict, Optional, Any


def getData(key: Optional[str], default: Any):
    pass


def main() -> None:
    #print(os.getcwd())
    #print(os.listdir('.'))
    print(Path().absolute())
    print(datetime.datetime.now())
    

if __name__ == "__main__":
    main()