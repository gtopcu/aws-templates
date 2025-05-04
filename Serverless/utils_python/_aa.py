
from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias, TypedDict
from collections import namedtuple, deque, OrderedDict, defaultdict, ChainMap

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("Logging is set up.")

import time
print(time.time()) 
print(time.strftime("%H:%M:%S%z"))
time.localtime()
time.perf_counter()

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str] = (1, "Hello")
my_dict: dict[str, int] = {"one": 1, "two": 2}
my_set: set[int] = {1, 2, 3}
my_string: str = "Hello, World!"


def main() -> None:
    print("{}".format(my_string))
    print("so, %s" % my_string)
    print(f"so, {my_string}")

    for i in "123456":
        print(i, end="-")

if __name__ == "__main__":
    main()


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    """
    Subtract the second number from the first.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The result of subtracting b from a.
    """
    return a - b  


""" 
import pytest

def test_subtract_numbers_positive():
    assert subtract_numbers(5, 3) == 2

def test_subtract_numbers_type_error():
    with pytest.raises(TypeError):
        subtract_numbers("5", 3) 
"""
