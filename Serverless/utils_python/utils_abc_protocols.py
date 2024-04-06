
# https://www.youtube.com/watch?v=dryNwWvSd4M

####################################################################################################

# from abc import ABC, abstractmethod # Python 3.6
# from overrides import override # Python 3.11

# class MyAbstract(ABC):
#     @abstractmethod
#     def my_abstract_method(self):
#         pass

# class MyClass(MyAbstract):
#     @override 
#     def my_abstract_method(self):
#         print("Hello")

# var = MyClass()
# var.my_abstract_method()

####################################################################################################

from abc import ABC, abstractmethod # Python 3.6
from typing import Protocol, runtime_checkable # Python 3.8

# Duct-typing, no need for inheritence / if you cant control original code
# Can use isinstance() and issubclass(), raise TypeError if applied to a non-protocol class
@runtime_checkable
class Portable(Protocol):
    @abstractmethod
    def handle(self, data) -> int: ...

def do_handle(p: Portable, data) -> int:
    return p.handle(data)

class Mug(Portable):
    def handle(self, data) -> int:
        return super().handle(data)

mug = Mug()
print(isinstance(mug, Portable))

