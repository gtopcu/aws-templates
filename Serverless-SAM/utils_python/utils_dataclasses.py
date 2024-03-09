import dataclasses
from dataclasses import asdict, astuple, dataclass, field
from datetime import datetime


@dataclass(frozen=True, #generates __hash__
           order=True) #generates __eq__ __lt__ __gt__ etc
# class Employee(pydantic.dataclasses.dataclass):
class Employee:
    id: int
    #id2 : int = field()
    name: str
    #name2: str = field(default="GT")
    birthday: datetime = field(default_factory=datetime.now)
    addresses: list[str] = field(default_factory=list, compare=False, hash=False, repr=False, default=[])

if __name__ == '__main__':
    emp1 = Employee(1, 'John')
    print(emp1)
    print(astuple(emp1))
    print(asdict(emp1))
    emp2 = dataclasses.replace(emp1, id=2)

