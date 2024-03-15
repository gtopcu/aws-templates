####################################################################################################

# from abc import ABC, abstractmethod

# class MyAbstract(ABC):
#     @abstractmethod
#     def my_abstract_method(self):
#         pass

####################################################################################################

# https://docs.python.org/3/library/enum.html
from enum import Enum, auto, IntEnum, StrEnum, IntFlag
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def __repr__(self):
        return "<%s.%s>" % (self.__class__.__name__, self._name_)

# functional syntax
# Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
class Role(IntEnum): #or IntFlag
    AUTHOR = auto() #or object()
    EDITOR = auto()
    VIEWER = auto()
    ADMIN = AUTHOR | EDITOR | VIEWER

class StringEnum(StrEnum):
    str1 = "str1"
    str2 = "str2"

####################################################################################################

# https://dev.to/decorator_factory/type-hints-in-python-tutorial-3pel

# from typing import Any, Optional, Union

# def optional_union(input: str) -> Union[str, None] #Optional[str]
#     return None

# def myUtil(mylist: str | None=None) -> None:
#     return mylist

# print(typing.TYPE_CHECKING)

# from typing import Tuple

# def sum_numbers(numbers: Tuple[int, ...]) -> int:
#     total = 0
#     for number in numbers: 
#         total += number
#     return total

# print(sum_numbers((1, 2, 3)))

####################################################################################################

class Human:
    def __init__(self, name: str, age: int, jobs:list[str]=None) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Human(name={self.name}, age={self.age})"

    def __hash__(self) -> int:
        return self.age * 17

    def __int__(self) -> int:
        return self.age

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False  
        return self.name == other.name and self.age == other.age

    def __ne__(self, other) -> bool: # !=
        return not self.__eq__(other)
    
    # le, lt, ge, gt

    def __add__(self, other) -> int:
        #if not isinstance(other, Human):
        if not isinstance(other, self.__class__):
            return NotImplemented        
        return self.age + other.age

    def __iadd__(self, other):
        #if not isinstance(other, Human):
        if not isinstance(other, self.__class__):
            return NotImplemented        
        self.age += other.age
        print("doing +=")
        return self

    def __containts__(self, value):
        return value in self.jobs
    
    def __getitem__(self, key):
        return self.jobs[key]

myHuman = Human("John", 20, jobs=["programmer"])
print(myHuman)
print(repr(myHuman))
print(hash(myHuman))
print(int(myHuman))
myHuman2 = Human("Cash", 34)
print(myHuman + myHuman2)
myHuman += myHuman2
print(myHuman)
print("programmer" in myHuman)
print(myHuman[0])
