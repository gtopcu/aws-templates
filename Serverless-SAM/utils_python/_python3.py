from collections import deque, defaultdict, namedtuple, ChainMap
from collections.abc import Callable, Iterable, Iterator, Generator, Container, Self
from collections.abc import Sized, Hashable, Sequence, Mapping, MutableSequence, MutableMapping
from collections.abc import Set, MutableSet, MappingView, KeysView, ItemsView, ValuesView
from typing import Any, Optional, TypedDict, TypeVar, Self
from typing import Dict, Set, FrozenSet, Tuple, NamedTuple, OrderedDict
from datetime import datetime
import time
import os, sys
from sys import getsizeof
from timeit import timeit, repeat
import random
import atexit


# BIG_CONSTANT: int = 10000000

def main() -> None:

    # time = time.perf_counter
    # print(f"Total time: {total_time:.3f}")

    # char = "c"
    # match char:
    #     case "a":
    #         print("a")
    #     case "b":
    #         print("b")
    #     case _:
    #         print("default")

    # print(chr(100))

    # my_list = [x for x in range(10) if x % 2 == 0]
    # my_set = {i for i in range(10)}
    # my_set2 = set()
    # # my_frozenset = frozenset(my_list)
    # my_dict = {x: x ** 2 for x in range(10)}
    # my_deque = deque(my_list, maxlen=5)
    # print(my_deque)
    # my_defaultdict = defaultdict(lambda: "default")
    # my_defaultdict = defaultdict(int)
    # print(my_defaultdict["NoKeyError"])

    # x, y = 1, 2
    # x = (12 * 3) if True else 6
    # print(time.time())
    # print("Done")

    # myint = 10
    # myfloat = float(myint)
    # print(type(myfloat))

    # tuple1 = (1, )
    # print(type(tuple1))

    # list = [x for x in range(0, 10, 2)]
    # list2 = [x*x for x in range(0, 10) if x%2==1]
    # print(list.count(2))
    # print(list.index(1))
    # print(list.extend(list2))
    # print(list.pop(0))
    # print(list.remove(2))
    # print(list.reverse())
    # list.sort(reverse=True)
    # print(list)
    # for i, j in enumerate(list):
    #     print(i, j)
    # for filtered in filter(lambda x: x % 4 == 0, list):
    #     print(filtered)
    # for mapped in map(lambda x: x * x, list):
    #     print(mapped)
    # iterator = iter(list)
    # while iterator:
    #     print(next(iterator))

    # dict = {x: x**2 for x in range(0, 10)}
    # print(dict.popitem())
    # print(dict.pop(0))
    # print(dict.get(10, 100)) # Returns None instead of KeyError
    # print(dict[2])
    # print(dict)
    # dict2 = dict.fromkeys([1, 2, 3], 0)
    # print(dict2)
    # dict.update(dict2)
    # print(dict)
    # print(dict.setdefault(9, 81))
    # del dict[9]
    # print(dict)

    # Student = namedtuple('Student', ['name', 'age', 'DOB'])
    # S = Student('Nandini', '19', '2541997')
    # print(S[1])
    # print(S.name)
    
    # d1 = {'a': 1, 'b': 2}  
    # d2 = {'c': 3, 'd': 4}  
    # chain = ChainMap(d1, d2)
    # print (chain.maps) 
    # print (list(chain.keys())) 
    # print (list(chain.values())) 

    # mydict = {"a": 1, "b": 2}
    # defined_kwargs(**mydict)
    # defined_kwargs(**{"a": 1, "b": 2})
    # defined_kwargs(arg1=1, arg2=2)
    # defined_args(arg1=1, arg2=True, arg3=3)

    # my_range = range(10 ** 6)
    # print(getsizeof(my_range), "bytes", sep="-")
    # my_list: list[int] = list(my_range)
    # print(getsizeof(my_list), "bytes", sep="-")
    # map/filter/reduce = iterators so also low memory

    # mylist1 = list(range(4))
    # mylist2 = [4,5,6]
    # print(mylist1 + mylist2)
    # mylist1.extend(mylist2)
    # print(mylist1)
    # print(slice(None, 5).indices)

    # myset1 = { x for x in range(0, 5) }
    # myset2 = { x for x in range(3, 7) }
    # print(myset1 | myset2)
    # myset1.update(myset2)
    # print(myset1)
    # print(myset1.union(myset2))
    # print(myset1 - myset2)
    # print(myset1 & myset2) #intersection
    # print(myset1 ^ myset2) #unique elements(symmetric difference)

    # dict1 = { 0: 'A', 1: 'B', 2: 'C' }
    # dict2 = { 2: 'D', 4: 'E', 5: 'F' }
    # dict1 |= dict2
    # print(dict1)
    # dict1.update(dict2)
    # print(dict1)

    # print(__file__)
    # print(os.path.dirname(__file__))

    # numbers: list[int] = list(range(10))
    # print(numbers[::-2])
    # reversed = slice(None, None, -2)
    # print(numbers[reversed])
    # numbers: list[int] = [*range(10)]
    # print(numbers)

    # myfloat: float = 123.1234
    # print(f"{myfloat:.2f}")

    # users: dict[int, str] = { 1: "Joe", 2: "Mary" }
    # if user := users.get(0): #walrus operator
    #     print(user)
    # else:
    #     print("Not found!")
    # print(user)

    # n: int = 1_000_000_000
    # print(f"{n:_}")
    # print(f"{n:,}")
    # var: str = "hello"
    # print(f"{var:>20}:")
    # print(f"{var:20}:")
    # print(f"{var:#^20}:")

    # n: float = 1e9
    # n: float = 12345.6789
    # print(round(n, 2))
    # print(f"{n:,.3f}")

    # print(f"{2 + 3}")
    # print(f"{2 + 3 = }")
    # print(f"{bool(0) = }")
    # var: str = "hello"
    # print(f"{var = }")

    # now: datetime = datetime.now()
    # print(now)
    # print(now.isoformat())
    # print(now.strftime("%Y-%m-%d %H:%M:%S"))
    # print(now.astimezone())
    # print(f"{now:%Y-%m-%dT%H:%M:%SZ}") #ISO8601 
    # print(f"{now:%d/%m/%y (%H:%M:%S)}")
    # print(f"{now:%c}") #local
    # print(f"{now:%I%p}") #AM/PM

    # rand_int = random.randint(0, 10)
    # rand_flt = random.random()

    # print(issubclass(Exception, BaseException))
    # sys.exit(0) - Raises SystemExit exception, finally & cleanups run
    # os._exit(0) - Immediate kill, no finals/cleanups run. Only POSIX files are closed

    print("done", end="\n")
    #atexit.unregister(func_exit)

@atexit.register
def func_exit() -> None:
    print("exiting..")

def input_none(input:str | None=None):
    print(input)
    return print("Returning")

def int_or_none(danger: list[dict] = None) -> int | None:
    danger = [] if danger is None else danger
    return None

# print("Output: " + str(f(1, 2, 3, a=4, b=5)))
# func_wrapper(f)()
def func_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        print("starting..")
        val = func(*args, **kwargs)
        print("ended in: ", (time.perf_counter_ns() - start) / 1000000, "ms") 
        return val
    return wrapper

@func_wrapper
def f(*args: int, **kwargs: int):
    print(":".join([str(arg) for arg in args]))
    #print("args:", args, "kwargs: ", kwargs)
    return sum(args) + sum(kwargs.values())

# f2(f1)
# def f1():
#     print("f1")
# def f2(func: Callable[[Any], Any]):
#     func()
# def callable(callable: Callable[[int, int], int], a: int, b: int) -> int:
#     return callable(a, b)

# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

if __name__ == "__main__":
    main()
