
# pip install pylint
# pylint _pplay.py  
# pylint: disable=all disable=invalid-name disable=missing-class-docstring (remove this line to get the results)
# pylint --rcfile=.pylintrc .

"""
This better get 10/10!
https://www.youtube.com/watch?v=RqdhVaX50mc
"""
# CamelCase(PascalCase) / snake_case
class myPersonClass: 
    """ This is my nice Person class"""

    def __init__(self, name: str) -> None:
        self.name = name
    
    def get_name(self) -> str:
        """
        Returns the name of the person
        :return: The name of the person
        :rtype: str 
        """
        """
        Returns the name of the person
        Args:
            self: Current instance
        Returns:
            Name of the person
        """
        return self.name


# from typing import Self, Any, Optional, Final, Literal, NewType, TypeAlias
# from collections import namedtuple, deque, OrderedDict, defaultdict
# from collections.abc import Mapping, Sequence, Set, Generator, Callable, Iterable, Iterator, AsyncIterable

# load_dotenv()
import os
import sys
import logging

# os.getenv('DDB_TABLE', 'table1')
# os.environ.get('DDB_TABLE', 'table1')
# POSTGRE_IP = os.environ['POSTGRE_IP']
# POSTGRE_PORT: int = os.environ.setdefault('POSTGRE_PORT', 5432)

# os.path.join(__file__, 'test.txt')
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, filename)
# os.getcwd()
# os.listdir()
# print(__name__)
# print(__file__)

# args:list[str] = sys.argv[:2]
# sys.getsizeof('abc')
# sys.version
# sys.version_info

# logger = logging.getLogger(__name__)
# logger.info('test')

# exit(1)

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

# name: str = "John"
# name.join("Doe")
# print('my name is %s' % name)

# myset = {1, 2, 3}
# myset.add(2)
# myset = filter(lambda x: x/2==1, myset)
# sorted = sorted(myset, reverse=True)
# print(sorted)

# for i, j in enumerate(myset, 0):
#     print(i, j)


# Pack-unpack 
# https://www.youtube.com/watch?v=-mS7K2K1IWk

# mylist = [1, 2, 3]
# print(*mylist)
# a, b, c = mylist
# print(a, b, c)
# mylist = [1, 2, 3, 4, 5]
# a, *b, c = mylist
# print(a, b, c)

# mylist1 = [1, 2, 3]
# mylist2 = [4, 5, 6]
# mylist3 = [*mylist1, 'combined', *mylist2]
# print(mylist3)

# my_dict = {'a': 1, 'b': 2, 'c': 3} 

# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# my_func(**my_dict)

# def my_func2(a: int, b: int, c: int):
#     print(a, b, c)
# my_func2(**my_dict)

# my_dict1 = {'a': 1, 'b': 2, 'c': 3} 
# my_dict2 = {'d': 4, 'e': 5, 'f': 3} 
# combined_dict = {**my_dict1, **my_dict2}
# print(combined_dict)

# def my_func3(**kwargs) -> None:
#     kwargs['a'] = 10
#     print(kwargs)
#     if 'b' in kwargs:
#         print('b exists')
# my_func3(**combined_dict)

# mylist.extend([4, 5])
# mylist2 = list[dict[str, Any]]
# mylist2.append({'a': 1, 'b': 2})

# mydict = {'a': 1, 'b': 2, 'c': 3}
# mydict.update({'d': 4})
# i, j = mydict.popitem()
# print(i, j)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(f'Error during operation: {str(e)}')


# matrix = [(0, 0), (0, 1), (0, 2),
#           (1, 0), (1, 1), (1, 2),
#           (2, 0), (2, 1), (2, 2)]

# matrix = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]

# for row, col in matrix:
#     print(row, col)
