
from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias
# from collections import namedtuple, deque, OrderedDict, defaultdict
# from collections.abc import Mapping, Sequence, Set, Generator, Callable, Iterable, Iterator, AsyncIterable

# load_dotenv()
import os
import sys
import logging

os.getenv('DDB_TABLE', 'table1')
os.environ.get('DDB_TABLE', 'table1')
POSTGRE_IP = os.environ['POSTGRE_IP']
POSTGRE_PORT: int = os.environ.setdefault('POSTGRE_PORT', 5432)
os.getcwd()
os.path.join(__file__, 'test.txt')

args:list[str] = sys.argv[:1]
sys.getsizeof('abc')
sys.version
sys.version_info

logger = logging.getLogger(__name__)
logger.info('test')

exit(1)

# class Cat:
#     def __new__(cls, name: str) -> None:
#         print(cls, name, 'new')
#         super().__new__(cls)
#         isinstance(cls, Cat)
#         print(cls, name, 'new')

#     def __init__(self, name:str) -> Self:
#         self.name = name
#         print('init')

# mycat = Cat('duman')
# print(mycat.name)

name: str = "John"
# name.join("Doe")
print('my name is %s' % name)

# myset = {1, 2, 3}
# myset.add(2)
# myset = filter(lambda x: x/2==1, myset)
# sorted = sorted(myset, reverse=True)
# print(sorted)

# for i, j in enumerate(myset, 0):
#     print(i, j)

# mylist = [1, 2, 3]
# mylist.extend([4, 5])
# print(*mylist)
mylist2 = list[dict[str, Any]]
mylist2.append({'a': 1, 'b': 2})

# mydict = {'a': 1, 'b': 2, 'c': 3}
# mydict.update({'d': 4})
# i, j = mydict.popitem()
# print(i, j)

# print(__name__)
# print(__file__)

# def add(a: float, b: float) -> float:
#     return a + b

try:
    print(1/0)
except ZeroDivisionError as e:
    print(f'Error during operation: {str(e)}')