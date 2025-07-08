# https://docs.python.org/3/library/functools.html
from functools import cache, cached_property, lru_cache, wraps, reduce, partial
import time

from dataclasses import dataclass

def main() -> None:
    
    # print(factorial(3))
    # print(factorial.cache_info())

    function(1, 2, 3)
    print("done")
    
    reduce(lambda x, y: x + y, range(10))

@cache #cachetools provides TTL too
# @lru_cache(maxsize=128, typed=False)
def factorial(n):
    return n * factorial(n-1) if n else 1

@dataclass
class Dataclass:
    id: int
    @cached_property
    def calculate(self):
        return self.id * 10

# @functools.wraps copies these from the original function:
# __name__ - function name
# __doc__ - docstring
# __module__ - module name
# __qualname__ - qualified name
# __annotations__ - type hints
# __wrapped__ - reference to the original function
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets someone by name."""
    return f"Hello, {name}!"

print(greet.__name__)    # Output: "greet"
print(greet.__doc__)     # Output: "Greets someone by name."


# ----------------------------------------------------------------------------------------------------------------------------------------

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        print("starting..")
        val = func(*args, **kwargs)
        print("ended in:", (time.perf_counter_ns() - start) / 1000000, "ms")
        return val
    return wrapper

def my_decorator_with_args(arg1: int):
    print("Decorator arg: ", arg1)
    def func_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter_ns()
            print("starting..")
            val = func(*args, **kwargs)
            print("ended in:", (time.perf_counter_ns() - start) / 1000000, "ms") 
            return val
        return wrapper
    return func_wrapper

@my_decorator_with_args(100)
def function(*args, **kwargs):
    """Docstring"""
    print(":".join([str(arg) for arg in args]))
    # print("args:", args, "kwargs: ", kwargs)
    return sum(args) + sum(kwargs.values())

# ----------------------------------------------------------------------------------------------------------------------------------------


# https://www.geeksforgeeks.org/partial-functions-python/

# sample partial func1
def func(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# A partial function that calls f with a as 3, b as 1 and c as 4
g = partial(func, 3, 1, 4)
print(g(5))

# sample partial func2
def add(a, b, c):
    return 100 * a + 10 * b + c

add_part = partial(add, c = 2, b = 1)
print(add_part(3))


if __name__ == "__main__":
    main()
