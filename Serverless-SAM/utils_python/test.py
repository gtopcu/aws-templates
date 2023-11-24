import os
import time
import json
from pathlib import Path
import pydantic
from pydantic import BaseModel
from typing import List, Dict, Optional



def main() -> None:
    #print(os.getcwd())
    #print(os.listdir('.'))
    mypath = Path().absolute()
    print(mypath)

if __name__ == "__main__":
    main()