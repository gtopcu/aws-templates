
from typing import Self
from abc import ABC, abstractmethod

# class AbstractHuman(ABC):
#     @abstractmethod
#     def calculate_work(self) -> int:
#         pass

class Human: #(AbstractHuman):

    name: str = "Gokhan" #   static var, access with Human.name. can have same name as instance var

    def __new__(cls, name: str, age: int, jobs:list[str]=None) -> Self:
        return super().__new__(cls)

    def __init__(self, name: str, age: int, jobs:list[str]=None) -> None:
        # super().__init__()
        self.name = name
        self.age = age      # instance var, access with human.name
        self.jobs = jobs
        self._title = "Mr."
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Human(name={self.name}, age={self.age})"

    def __hash__(self) -> int:
        return self.age * 17
    
    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Self:
        if self.age < 100:
            self.age += 1
            return self
        else:
            raise StopIteration

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

    @property
    def title(self) -> str:
        print("getting title")
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        print("setting title")
        self._title = title
    
    @title.deleter
    def title(self) -> None:
        print("deleting title")
        self._title = None

    #https://www.tutorialsteacher.com/python/classmethod-decorator
    @classmethod
    def get_class_name(cls) -> str:
        return Human.name

    @staticmethod
    def calculate_retirement(human: Self) -> int:
        return 65 - human.age

human = Human("John", 40, ["programmer"])
print(human)

print(human.name) # access by instance var -> John
print(Human.name) # access by class/static var -> Gokhan

print(human.title) # access by property -> Mr.
human.title = "Dr." # set by property
print(human.title)
del human.title # delete by property
print(human.title)

print(Human.get_class_name()) # access by class method
print(human.get_class_name()) # access by instance method

print(human.calculate_retirement(human)) # access by static method
print(Human.calculate_retirement(human)) # access by static method

# print(dir(human))
# iterator = iter(human) # Human.__iter__
# human2 = iterator.__next__() # or next(iterator)
# print(repr(human))
# print(hash(human))
# print(int(human))
# human2 = Human("Cash", 34)
# print(human + human2)
# human += human2
# print(human)
# print("programmer" in human)
# print(human[0])

