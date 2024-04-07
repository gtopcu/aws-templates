import dataclasses
from dataclasses import asdict, astuple, dataclass, field
from datetime import datetime
from pydantic import BaseModel
from typing import Type

# If init is true, an __init__() method is added to the class
# If repr is true, a __repr__() method is added
# If order is true, rich comparison dunder methods are added - __eq__ __lt__ __gt__ etc
# If unsafe_hash is true, a __hash__() method is added
# If frozen is true, fields may not be assigned to after instance creation
# If match_args is true, the __match_args__ tuple is added. 
# If kw_only is true, then by default all fields are keyword-only
# If slots is true, a new class with a __slots__ attribute is returned

@dataclass(kw_only=True)
class simpleDataclass:
    id: int
    name: str

@dataclass
# class Employee(pydantic.dataclasses.dataclass):
class Employee: #[T: BaseModel]:
    id: int
    #id2 : int = field()
    name: str
    #name2: str = field(default="GT")
    birthday: datetime = field(default_factory=datetime.now)
    addresses: list[str] = field(default_factory=list, compare=False, hash=False, repr=False)
    # model: Type[T]

if __name__ == '__main__':
    # emp1 = Employee(1, 'John')
    # print(emp1)
    # print(astuple(emp1))
    # print(asdict(emp1))
    # emp2 = dataclasses.replace(emp1, id=2)

    simpleDC = simpleDataclass(id=1, name="John") #kw-only