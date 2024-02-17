import os
import time
from timeit import timeit
import datetime
import json
from pathlib import Path
import pathlib
import typing

def main() -> None:
    # print(os.getcwd())
    # print(os.listdir('.'))
    # print(Path().absolute())
    # print(datetime.datetime.now())
    # print(dir(int))
    # print(__file__)
    # print(pathlib.Path(__file__).parent / "examples")
    x, y = 3, 4
    # print(x, y)
    # print(nums)

    #total_time = timeit(time_this())
    #print(f"Total time: {total_time:.3f}")    

    # char = "c"
    # match char:
    #     case "a":
    #         print("a")
    #     case "b":
    #         print("b")
    #     case _:
    #         print("default")

    # nums = [x for x in range(10) if x % 2 == 0]

    print(chr(10))

if __name__ == "__main__":
    main()