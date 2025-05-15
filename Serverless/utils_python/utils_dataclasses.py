import dataclasses
from dataclasses import dataclass, field, asdict, astuple
from datetime import datetime
# from pydantic import BaseModel, Field, dataclasses
from typing import Type
from uuid import uuid4, UUID
from typing import Any, Optional
from functools import cached_property

# If init is true, an __init__() method is added to the class
# If repr is true, a __repr__() method is added
# If order is true, rich comparison dunder methods are added - __eq__ __lt__ __gt__ etc
# If unsafe_hash is true, a __hash__() method is added
# If frozen is true, fields may not be assigned to after instance creation
# If match_args is true, the __match_args__ tuple is added. 
# If kw_only is true, then by default all fields are keyword-only
# If slots is true, a new class with a __slots__ attribute is returned

# @dataclass(init=True, kw_only=True, unsafe_hash=True, order=True, frozen=True, slots=True)
# class SimpleDataclass:
#     id: int
#     name: str | None = None
#     address: Optional[str]
#     age: int = 0
#     birthday: datetime = field(default_factory=datetime.now)
#     addresses: list[str] = field(default_factory=list, compare=False, hash=False, repr=False)
#     user_id: str = field(default_factory=lambda: f"{uuid4()}")

#     @cached_property
#     def get_user_id(self) -> str:
#         return self.user_id
#     @property
#     def get_name(self) -> str:
#         return self.name

#     def __init__(self, id: int, name: str | None = None, address: Optional[str] = None, age: int = 0):
#         self.id = id
#         self.name = name
#     def __post_init__(self):
#         if self.name is None:
#             raise ValueError("Name cannot be None")
#         if self.age < 0:
#             raise ValueError("Age cannot be negative")
#     def __str__(self):
#         return f"SimpleDataclass(id={self.id}, name={self.name}, address={self.address}, age={self.age}, birthday={self.birthday}, addresses={self.addresses}, user_id={self.user_id})"
#     def __repr__(self):
#         return f"SimpleDataclass(id={self.id}, name={self.name}, address={self.address}, age={self.age}, birthday={self.birthday}, addresses={self.addresses}, user_id={self.user_id})"
#     def __eq__(self, other):
#         if not isinstance(other, SimpleDataclass):
#             return NotImplemented
#         return self.id == other.id and self.name == other.name and self.address == other.address and self.age == other.age and self.birthday == other.birthday and self.addresses == other.addresses and self.user_id == other.user_id

# @dataclass
# class DoubleLinkedList:
#     value: int = 3
#     next: "DoubleLinkedList | None" = None
#     prev: "DoubleLinkedList | None" = None

#     def my_function(self, new_value: "int | None" = None):
#         if new_value is not None:
#             self.value = new_value

# my_double_linked_list1 = DoubleLinkedList(1)
# my_double_linked_list1.my_function(2)
# print(my_double_linked_list1)
# my_double_linked_list2 = DoubleLinkedList(1, DoubleLinkedList(2, DoubleLinkedList(3)))
# print(my_double_linked_list2)


# @dataclass(kw_only=True)
# class SimpleDataclass:(BaseModel):
#     id: int
#     name: str

# my_dataclass = SimpleDataclass(id=1, name="John")
# my_dataclass.update_name("Jane")
# print(my_dataclass)

# @dataclass
# class Employee(pydantic.dataclasses.dataclass):
# class Employee: #[T: BaseModel]:
#     id: int
#     #id2 : int = field()
#     name: Optional[str]
#     #name2: str = field(default="GT")
#     birthday: datetime = field(default_factory=datetime.now)
#     addresses: list[str] = field(default_factory=list, compare=False, hash=False, repr=False)
#     user_id: str = field(default_factory=lambda: f"{uuid4()}")
#     # model: Type[T]

# if __name__ == '__main__':
#     emp1 = Employee(1, 'John')
    # print(emp1)
    # print(astuple(emp1))
    # print(asdict(emp1))
    # emp2 = dataclasses.replace(emp1, id=2)
    # simpleDC = simpleDataclass(id=1, name="John") #kw-only