from collections import deque, defaultdict, namedtuple, ChainMap
from collections.abc import Callable, Iterable, Iterator, Generator, Container
from collections.abc import Sized, Hashable, Sequence, Mapping, MutableSequence, MutableMapping
from collections.abc import Set, MutableSet, MappingView, KeysView, ItemsView, ValuesView
from typing import Any, Optional, TypedDict, TypeVar, Self, Final
from typing import Dict, Set, FrozenSet, Tuple, NamedTuple, OrderedDict
import heapq

import os, sys, shutil
from pathlib import Path
from sys import getsizeof
from timeit import timeit, repeat
import random
import glob
import pickle, shelve

import atexit
import math
from copy import deepcopy

from datetime import datetime, UTC
import time
from pytz import timezone
import copy

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
    # print(myset1 & myset2) # intersection
    # print(myset1 ^ myset2) # unique elements(symmetric difference)
    # myset1 = frozenset(myset1)

    # dict1 = { 0: 'A', 1: 'B', 2: 'C' }
    # dict2 = { 2: 'D', 4: 'E', 5: 'F' }
    # dict1 |= dict2
    # print(dict1)
    # dict1.update(dict2)
    # print(dict1)

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

    # os.system("clear")
    # os.getenv("ENV", "default")
    # os.putenv("ENV", "value")
    # os.environ.get(env_name, default)

    # print(__file__)
    # os.getcwd())
    # os.listdir('.')
    # os.curdir()
    # os.pardir()
    # os.mkdir("/dir")
    # os.makedirs("os/makedirs", exist_ok=False) # FileExistsError:
    # os.rmdir("dir")
    # os.remove("file")
    # os.rename("file1", "file2"))
    # os.chown("path", userID, groupID, follow_symlinks=False)
    # os.chmod("file", intMode)

    # os.path.join(current_path, filename)
    # os.path.isdir(path)
    # os.path.isfile(path)
    # os.path.exists(path)
    # os.path.getsize(path)
    # os.path.basename(path)
    # os.path.dirname(__file__)
    # os.path.abspath(__file__)
    # os.path.realpath(__file__)
    # os.path.islink(path)
    # os.path.expanduser('~') # Path.home()

    # shutil.rmtree("os/makedirs")
    # shutil.chown("path", "user", "group")   
    # shutil.move("/source", "target")      # same as mv
    

    # path = Path.home() 
    # path            # /Users/gtopcu
    # path.name       # gtopcu
    # path.stem       # gtopcu - filename without extension
    # path.suffix     # .py
    # path.drive      # empty
    # path.root       # /
    # path.anchor     # /
    
    # Path.cwd()        # /Users/gtopcu/My Drive/VSCode
    # Path(__file__)    # doesnt work in .ipynb
    # Path.parent()
    # Path.parents[0]   # Nth parent
    # Path.absolute()
    # Path.joinpath("Desktop").mkdir(exist_ok=True)
    # Path.chmod(path, intMode, follow_symlinks=True)
    # Path.group()
    # Path.exists()
    # Path.is_file()
    # Path.is_dir()
    # Path.is_symlink()
    # Path.iterdir()
    # Path.as_uri(path)
    # Path.resolve("path", strict=False)
    # Path.mkdir(Path, mode = 511, parents = False, exist_ok = False)
    # Path.rmdir() # must be empty
    # Path.unlink(missing_ok=True)
    # Path.touch(Path, mode = 438, exist_ok = True)
    # Path.owner(Path)
    # Path.match("pattern")
    # Path.glob(Path, pattern="*")
    # Path.rglob(Path, pattern="*")
    
    # print(glob.glob("?????.py")
    # print(glob.glob("*.py"))
    # print(glob.glob("*.*"))
    # print(glob.glob("[abc]*.py")) #[] first char should be a or
    # # print(glob.glob("[!abc]*.py")) #[] first char should NOT be a or b
    # globs = glob.iglob("**/utils_*.py", root_dir="/Users/gtopcu/", recursive=True, include_hidden=True)
    # print(globs.__next__())
    # for i, cglob in enumerate(globs, 1):
    #     print(i, cglob, sep=":")


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
    # print(my_list)
    # my_dict = dict(my_list) 
    # dict["key1"] -> Big O(1)

    # Heap queue / priority queue. hq[0] is always its smallest element.
    # Python only allows min heaps. For max heaps, multiply by -1 at push/pop
    # read O(1), add/remove O(log n)
    # When adding to heap[3], element at heap[3] is sent to the end of the queue
    # 
    # heapq.heapify(my_list) # transforms list into a min heap, in-place, in linear time
    # heapq.heappush(my_list, item) # pushes a new item on the heap
    # heapq.heappop(my_list) # pops the smallest item from the heap
    # heapq.heappushpop(my_list, item) # pushes a new item and then returns the smallest item; the heap size is unchanged
    # heapq.heapreplace(my_list, item) # pops and returns the smallest item; the heap size is unchanged
    # heapq.merge(iter1, iter2) # merges two sorted lists into one sorted list
    # heapq.nlargest(n, iter) # returns the n largest elements from the heap
    # heapq.nsmallest(n, iter) # returns the n smallest elements from the heap

    # print(sys.maxsize)        # 9223372036854775807
    # math.inf
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
    # print(math.pi)            # 3.141592653589793
    # print(math.e)             # 2.718281828459045
    # print(math.log(math.e))   # 1.0
    # print(math.pow(2, 100) < float("inf")) # True
    # math.prod(nums[0:i])

    # print(iter.next())
    # print(issubclass(Exception, BaseException))

    # kwargs(name=1234)
    # kwargs(**{"name":1234})

    # list = [0] * 5
    # stack = []
    # if not stack:
    #     print("empty")
    # else:
    #     print("not empty")        
    
    # list1 = [[1,2,3], *range(5)]
    # list2 = list1[:]
    # list2 = list(list1)
    # list2 = [x for x in list1]
    # list2 = list1.copy()
    # list2 = copy.copy(list1)
    # list2 = copy.deepcopy(list1)
    # list1[0][0] = 0
    # print(id(list1), id(list2))
    # print(id(list1[0][0]), list2[0][0])
    # print(list1)
    # print(list2)

    # x: list[list[int]]
    # list = [ [x]*4 for x in range(3) ]
    # print(list)
    # list = [ [0]*4 ]* 4 # not good, all innter arrays will be same object
    # print(list)
    # list = [[1]*4,[2]*4,[3]*4]
    # print(list)
    # list = [ {} ]
    # for i, number in enumerate(range(10)):
    #     print(i, number)
    # nums1 = [1, 2, 3]
    # nums2 = [4, 5, 6]
    # for i, j in zip(nums1, nums2):
    #     print(i, j)
    # custom_sorting = ["This", "is", "a", "number"]
    # custom_sorting.sort(key=len)
    # custom_sorting.sort(key=lambda x: len(x))
    # print(custom_sorting)

    # s = "abc"     # Immutable
    # s[0] = "d"    # TypeError
    # s += "def"    # OK, but new object
    # print(int("123") + int("123")) # 246
    # print(str(123) + str(123))     # 123123
    # print(ord("A"), chr(125))

    # LEGB: Local, Enclosing, Global, Built-in
    # global var
    # nonlocal var

    # from . import module
    # import builtins
    # print(dir(builtins))
    # print(sys.path)       # first checks builtins for imported modules, than sys.path/env vars
    # PYTHONPATH=usr/users/...
    # sys.path.append('/usr/bin/lib...') 
    # sys.path.append(os.path.abspath(module_path))

    # hasattr(object, name)
    # getattr(object, name) # AttributeError

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
    # decoded = data.decode("utf-8")
    # dataArray = bytearray(bytes)
    # dataArray.swapcase()

    print("done", end="\n")
    # vnenv set python interpreter
    # Control + L, Command + Click

    # atexit.unregister(func_exit)
    # sys.exit(0) - Raises SystemExit exception, finally & cleanups run
    # os._exit(0) - Immediate kill, no finals/cleanups run. Only POSIX files are closed

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

# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

if __name__ == "__main__":
    main()
