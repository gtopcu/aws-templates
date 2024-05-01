
# https://stackoverflow.com/questions/52827463/collections-iterable-vs-typing-iterable-in-type-annotation-and-checking-for-iter

from typing import Any, Optional, Self, Final
# from typing import Dict, Set, FrozenSet, Tuple
# from typing import TypedDict, TypeVar, TypeAlias, NewType, Literal, LiteralString, Annotated

# from collections import deque, defaultdict, namedtuple, ChainMap, Counter, OrderedDict, UserDict, UserList, UserString
# from collections.abc import Callable, Iterable, Iterator, Generator, Container
# from collections.abc import Sized, Hashable, Sequence, Mapping, MutableSequence, MutableMapping
# from collections.abc import Set, MutableSet, MappingView, KeysView, ItemsView, ValuesView

from collections.abc import Iterable

import heapq

import os, sys, shutil
from pathlib import Path
from sys import getsizeof
import random
import pickle, shelve
import copy

import atexit
import math

from datetime import datetime, UTC
import time

from functools import reduce
import traceback

from operator import add, sub, mul, itemgetter, attrgetter, methodcaller


# from . import database as db
# from .database import model
# import .database as db


# BIG_CONSTANT: int = 10000000


def main() -> None:

    # print(dir(random))
    # my_iterator = iter(my_list) = my_list.__iter__() # list: iterable
    # val = next(my_iterator)                          # my_iterator: iterator raises StopIteration

    # time = time.perf_counter()
    # print(f"Total time: {total_time:.3f}")

    # char = "c"
    # match char:
    #     case "a":
    #         print("a")
    #     case "b":
    #         print("b")
    #     case _:
    #         print("default")

    # my_tuple = (1, )
    # my_tuple = tuple((1, 2, 3))
    # my_tuple3 = my_tuple1 + my_tuple2
    # my_tuple.index(i)
    # my_tuple.count(i)
    
    # my_list = [x for x in range(10) if x % 2 == 0]
    # my_set = {i for i in range(10)}
    # my_set2 = set()
    # # my_frozenset = frozenset(my_list)
    # my_dict = {x: x ** 2 for x in range(10)}
    # my_deque = deque(my_list, maxlen=5)
    # my_defaultdict = defaultdict(lambda: "default")
    # my_defaultdict = defaultdict(int)
    # my_ordereddict = OrderedDict()
    
    # x, y = 1, 2
    # x = (12 * 3) if True else 6

    # list.count(2)
    # list.index(1)
    # list.insert(0, 1)
    # list.append(10)
    # list.extend(list2)
    # list.pop()    # pop last element
    # list.pop(idx) # pop item at idx - raises IndexError
    # list.remove(2)
    # list.reverse()
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
    # print(dict.pop("key"))
    # print(dict.get(10, 100)) # Returns None instead of KeyError
    # dict2 = dict.fromkeys([1, 2, 3], 0)
    # dict.update(dict2)
    # print(dict.setdefault(9, 81))
    # del dict[9]
    # list = sorted(dict, key=dict.get, reverse=True)
    # list = sorted(occurences, key=lambda x:occurences[x], reverse=True)

    # Student = namedtuple('Student', ['name', 'age', 'DOB'])
    # nt = Student('Nandini', '19', '2541997')
    # print(nt[1])
    # print(nt.name)
    
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
    # print(slice(None, 5).indices)
    # mydict = dict(zip(mylist1, mylist2)) # {0: 4, 1: 5, 2: 6}

    # myset1 = { x for x in range(0, 5) }
    # myset2 = { x for x in range(3, 7) }
    # print(myset1 | myset2)
    # myset1.update(myset2)
    # print(myset1)
    # print(myset1.union(myset2))
    # print(myset1 - myset2)
    # print(myset1 & myset2) # intersection
    # print(myset1 ^ myset2) # unique elements(symmetric difference)
    # myset1 = frozenset(myset1)

    # dict1 = { 0: 'A', 1: 'B', 2: 'C' }
    # dict2 = { 2: 'D', 4: 'E', 5: 'F' }
    # dict1 |= dict2
    # dict1.update(dict2)

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

    # print(f"{number:.2f}")
    # print(f"Total: {(time.time() - start):.3f}s")
    # print(f"Total: {(time.perf_counter() - start) * 1000} ms")

    # rand_int = random.randint(0, 10)
    # rand_flt = random.random()
    # random.shuffle(numbers)
    # random.choice(numbers)
    # random.seed("ABC")
    # random.randrange(0, 100, 10)
    # bytes = random.randbytes(10) # 0-255

    # with open("fruit.pickle", "wb") as file:
    #     pickle.dump(fruit, file)
    # with open("fruit.pickle", "rb") as file:
    #     fruit:Fruit = pickle.load(f)

    # shelve does not load the whole object like pickle
    # with shelve.open("shelve_file", writeback=True) as db:
    #     my_dict = { "key1": "value1", "key2": Fruit("apple") } # can store multiple objects
    #     db.update(my_dict)
        # print(type(db))
        # print(dict(db))
        # key = db.get("key", "default")
        # key1 = db["key1"]       # retrieve a COPY of the data. if writeback false, not updated
        # db["key"] = "value"
        # del db["key"]           # raises KeyError if not present
        # db.sync()
        # db.close()

    # def tuple_returning_func(): 
    #     return "str", 3, { 1, 2 } # Returns tuple, we could also write (x, y) 
    # x, y, z = tuple_returning_func() 

    # print(chr(12), " - ", ord('A'))
    # my_int = 5
    # print("here is: {}".format(my_int))

    # for item in reversed(range(0, 10)):
    #     print(item)

    # my_tuple_list = [(a, b) for a in range(2) for b in range(5, 7)]
    # print(my_tuple_list)
    # my_list = [a*b for a in range(2) for b in range(5, 10) if b % 2 ==0]

    # https://wiki.python.org/moin/TimeComplexity
    #     
    # list = array, stack - LIFO - Big O(1)
    # push: list.append(item)
    # pop:  list.pop()
    # peek: list[-1] 
    # deque = double-linked list / double-ended queue
    # dict = hashmap

    # my_list[0] -> Big 0(1)
    # my_list.insert(5, 3) -> Big O(k)
    # my_list.pop() -> Big O(1)
    # my_list.sort() -> Big O(n log n)
    # dq = deque(range(15), maxlen=10) 
    # dq[0] -> Big O(1)
    # dq.rotate(3) -> Big O(k)

    # my_list = [ ("k1","1"), ("k2","2"), (15, 3) ]
    # print(my_list)                  [('k1', '1'), ('k2', '2'), (15, 3)]
    # my_dict = dict(my_list) 
    # print(my_dict)                  {'k1': '1', 'k2': '2', 15: 3}
    # dict["key1"] -> Big O(1)

    # Heap queue / priority queue. hq[0] is always its smallest element.
    # Python only allows min heaps. For max heaps, multiply by -1 at push/pop or use _heapify_max
    # create O(n), read O(1), add/remove O(log n)
    # When adding to heap[3], element at heap[3] is sent to the end of the queue
    # 
    # heapq.heapify(my_list) # transforms list into a min heap, in-place, in linear time
    # heapq.heappush(my_list, item) # pushes a new item on the heap
    # heapq.heappop(my_list) # pops the smallest item from the heap
    # heapq.heappushpop(my_list, item) # pushes a new item and then returns the smallest item; the heap size is unchanged
    # heapq.heapreplace(my_list, item) # pops and returns the smallest item; the heap size is unchanged
    # heapq.nlargest(n, iter) # returns the n largest elements from the heap
    # heapq.nsmallest(n, iter) # returns the n smallest elements from the heap
    # heapq.merge(iter1, iter2) # merges two sorted lists into one sorted list
    # heapq._heapify_max(my_list) # max heap. or use heap.heapify([-x for x in my_lsit])

    # print(sys.maxsize)        # 9223372036854775807
    # math.inf
    # math.pi                  # 3.141592653589793
    # math.e                   # 2.718281828459045
    # print(float("inf"))
    # print(float("-inf"))
    # print(-3 // 2)            # -2
    # print(int(-3 / 2))        # -1
    # print(int(-1.9))          # -1
    # print(int(1.9))           # 1
    # print(-10 % 3)            # 2
    # print(math.fmod(-10, 3))  # -1.0
    # print(math.floor(3/2))    # 1
    # print(math.ceil(3/2))     # 2
    # print(math.sqrt(4))       # 2.0
    # print(math.pow(2, 3))     # 8.0
    # print(math.log(math.e))   # 1.0
    # print(math.pow(2, 100) < float("inf")) # True
    # math.prod(nums[0:10])

    # print(iter.next())
    # print(issubclass(Exception, BaseException))

    # kwargs(name=1234)
    # kwargs(**{"name":1234})

    
    # x: list[list[int]]
    # list = [0] * 5
    # list = [ [1]*4,[2]*4,[3]*4 ]
    # list = [ [x]*4 for x in range(3) ]
    # list = [ [0]*4 ]* 4 # not good, all innter arrays will be same object
    # list1 = [[1,2,3], *range(5)]
    # list2 = list1[:]
    # list2 = list(list1)
    # list2 = [x for x in list1]
    # list2 = list1.copy()
    # list2 = copy.copy(list1)
    # list2 = copy.deepcopy(list1)

    # mylist = [item for sublist in mylist for item in sublist]
    # for i, j in zip(list1, list2):
    # dict1 = dict(zip(list1, list2))
    # custom_sorting = ["This", "is", "a", "number"]
    # custom_sorting.sort(key=len)
    # custom_sorting.sort(key=lambda x: len(x))
    
    # for i in map(print, range(10)): ...
    # map(lambda x: print(x), range(10))
    # listMap = list(map(lambda x: x * x, range(10)))
    # listMap = [*map(lambda x: x * x, range(10))]
    # filter(lambda x: x % 2 == 0, range(10))
    # reduce(lambda x, y: x + y, range(10))

    # s = "abc"     # Immutable
    # s[0] = "d"    # TypeError
    # s += "def"    # OK, but new object
    # print(int("123") + int("123")) # 246
    # print(str(123) + str(123))     # 123123
    # print(ord("A"), chr(125))

    # LEGB: Local, Enclosing, Global, Built-in
    # global var
    # nonlocal var

    # hasattr(object, name)
    # getattr(object, name) # AttributeError
    # setattr(object, name, value)
    # delattr(object, name)

    # Ellipses
    # https://www.geeksforgeeks.org/what-is-three-dots-or-ellipsis-in-python3/
    # def use(handles: int) -> None: ...
    # def foo(x = ...): # Instead of passing None
    #     print("x:", x)
    #     return x
    # print(foo)
    # foo(1)
    # foo()

    # from typing import Callable
    # def inject(func: Callable[..., str]) -> None: ...
    # def inject(func: Callable[[str, [int]], str]) -> None: ...

    # data: bytes = "adfsdf".encode("utf-8")
    # data = b"bytestring"
    # decoded = data.decode("utf-8")
    # dataArray = bytearray(bytes)
    # dataArray.swapcase()
    # "asdf".casefold()
    # f"{val.casefold()}"

    # mytuple = tuple((1, 2))
    # x, y = mytuple # unpacking
    # tuple3 = tuple1 + tuple2
    # mylist.pop(1)           -> Any: IndexError
    # mydict.popitem()        -> Any: KeyError
    # mydict.pop("key1")      -> Any: KeyError
    # myset.pop()             -> Any: KeyError
    # myset.remove(element)   -> None: KeyError
    # myset.discard(element)  -> None: No error

    # mylist = [*range(3)]
    # mylist = list(map(lambda x: x*x, mylist))
    # (lambda x: x*x)(3)
    # func = lambda x,y: x*y

    # iterator = (x for x in range(6))
    # print(next(iterator))

    # name = "gokhan"
    # print("username_%s" % name)             # string interpolation
    # print("%s %d %.2f" % ("Hello", 1.2, 1.2))
    # print("{0} {1} {2}".format("Hello", 1.2, 1.2))

    # data = b'\x01'*1024)
    # print("SampleClass".__dict__)
    # sc = SampleClass("Gokhan", 40)
    # print(repr(sc))
    # print(hasattr(sc, "age"))
    # print(f"{1/10:.2f}")
    # pprint(tomldata, sort_dicts=True)
    
    # my_list = [0, 1, 2]
    # r: slice = slice(None, None, -1)
    # print(my_list[r])
    # list_getter: itemgetter = itemgetter(0, -1)
    # a, b = list_getter(my_list)
    # my_dict = { "a": 1, "b": 2 }
    # getter: itemgetter = itemgetter("a", "b")
    # a, b = getter(my_dict)

    # mylist = list(string)
    # mylist = [int(i) for i in string]    

    # generator_func(): 
    #   for i in range(3): 
    #       yield i 
    # generator = generator_func()
    # next(generator)
    # yield from generator

    # reduce(lambda x, y = x+y, my_list, init_value) -> GENERATOR!

    # print(mytype := (len("abc") > 2))     -> Walrus operator
    # if myval := get_value(): ...

    # import builtins
    # print(dir(builtins))
    # print(sys.path)       # first checks builtins for imported modules, than sys.path/env vars
    # PYTHONPATH=usr/users/...
    # sys.path.append('/usr/bin/lib...') 
    # sys.path.append(os.path.abspath(module_path))
    # sys.version

    # traceback.print_stack()
    # traceback.print_exc()
    # traceback.print_exception(type(err), err, err.__traceback__)

    # BaseException -> 
    #  Exception -> SystemExit 
    #               StandardError -> ValueError: int("A"), KeyError: dict['key1'], TypeError: str[0]='a', 
    #               IndexError, AttributeError, NameError, AssertionError, StopIteration, ArithmeticError, 
    #               ZeroDivisionError, NotImplementedError, RuntimeError, SystemError

    print("done", end="\n")
    # vnenv set python interpreter
    # Control + L, Command + Click

    # atexit.unregister(func_exit)
    # sys.exit(0) - Raises SystemExit exception, finally & cleanups run
    # os._exit(0) - Immediate kill, no finals/cleanups run. Only POSIX files are closed

    # import webbrowser
    # webbrowser.open("http://localhost:8080", new=0, autoraise=False

def __eq__(self, other: Self) -> bool:
    # return self.name == other.name and self.age == other.age
    self.__dict__ == other.__dict__

def generator_func(loop_count: int):
    for i in range(loop_count):
        yield i
        time.sleep(1)

def iterate(y:Iterable):
    for x in y: # it = iter(y)  # y.__iter__()
        # x = next(y)           # it.__next__() - StopIteration
        pass

@atexit.register
def func_exit() -> None:
    print("exiting..")

def outer(val: int, arr: list[int]):
    def inner():
        arr[0] = 1      # will modify outer arr
        nonlocal val    # will modify outer val
        val *= 2        

def kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    if value := kwargs.get("name"):
        print("name found =", value)

# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# name and age mandatory for both
def mandatoryArgs(self, /, name: str, age: int): ...
def mandatoryKwargs(self, *, name: str, age: int): ...

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
    # print("args:", args, "kwargs: ", kwargs)
    return sum(args) + sum(kwargs.values())

# f2(f1)
# def f1():
#     print("f1")
# def f2(func: Callable[[Any], Any]):
#     func()
# def callable(callable: Callable[[int, int], int], a: int, b: int) -> int:
#     return callable(a, b)



if __name__ == "__main__":
    main()


