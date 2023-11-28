from dataclasses import dataclass, field, astuple, asdict
from datetime import datetime

@dataclass(frozen=True, order=True)
class Employee:
    id: int
    name: str = field(default="GT")
    date: datetime
    addresses: list[str] = field(default_factory=list, compare=False, hash=False, repr=False)

if __name__ == '__main__':
    emp = Employee(1, 'John')
    print(emp)
    print(astuple(emp))
    print(asdict(emp))

