# https://docs.python.org/3/library/functools.html
from functools import cache, lru_cache, wraps, update_wrapper
import time

def main() -> None:
    
    # print(factorial(3))
    # print(factorial(14))
    # print(factorial(6))
    # print(factorial.cache_info())

    function(1, 2, 3)

    print("done")


# @cache
# # @lru_cache(maxsize=128, typed=False) #maxsize=None 
# def factorial(n):
#     return n * factorial(n-1) if n else 1

def func_wrapper_with_args(arg1: int):
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

# @func_wrapper
@func_wrapper_with_args(100)
def function(*args, **kwargs):
    """Docstring"""
    print(":".join([str(arg) for arg in args]))
    # print("args:", args, "kwargs: ", kwargs)
    return sum(args) + sum(kwargs.values())


if __name__ == "__main__":
    main()
