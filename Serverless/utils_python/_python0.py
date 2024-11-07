from typing import Self
class Human:

    def __new__(cls, name) -> Self:
        super().__new__(cls)

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

myHuman = Human("John", 20, jobs=["programmer"])
print(myHuman)
print(dir(myHuman))
iterator = iter(myHuman) # Human.__iter__
myHuman2 = iterator.__next__() # or next(iterator)
print(repr(myHuman))
print(hash(myHuman))
print(int(myHuman))
myHuman2 = Human("Cash", 34)
print(myHuman + myHuman2)
myHuman += myHuman2
print(myHuman)
print("programmer" in myHuman)
print(myHuman[0])
