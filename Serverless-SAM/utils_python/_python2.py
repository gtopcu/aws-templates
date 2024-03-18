# https://www.youtube.com/watch?v=T8UXgR-EtoM
# https://docs.python.org/3/library/typing.html

# Faster list/set comprehension
# Formalized & multi-line f-strings
# Better error descriptions
# Union types str | int

# from typing import Type
# type myTypeAlias = list[str]
# def myfunc(arg: myTypeAlias):
#     pass

# https://docs.python.org/3/library/typing.html#typing.Self
# from typing import Self, reveal_type
# class Foo:
#     def return_self(self) -> Self:
#         return self
# reveal_type(Foo().return_self())

# from typing import Literal, Annotated
# from annotated_types import Gt, Ge, Le, Lt
# type my_literal = Literal["a", "b", "c"]
# my_annotaded = Annotated[float, Gt(0), Le(200)]

# from typing import Final #@final for methods
# MAX_SIZE: Final = 9000

####################################################################################################
# Generics

# class MyClass[T]:
#     def myFunc(input: T) -> T:
#         return T

# def myFunc[T](input: list[T]) -> T:
#     return input

# type Point = tuple[float, float]
# type Points[T] = tuple[T, T]

####################################################################################################
# TypedDict

# https://peps.python.org/pep-0589/

# from typing import TypedDict, Unpack

# https://docs.python.org/3/library/typing.html#typing.TypedDict
# class Movie(TypedDict, total=False): #total: all fields required
#     name: Required[str]
#     year: int
#     rating: NotRequired[float]

# def foo(**kwargs: Unpack[Movie]):
#     print(kwargs)
#     print(kwargs["name"])

# foo(name="The Matrix", year=1999)

####################################################################################################

# from typing import LiteralString #for preventing SQL injection

# def run_query(sql: LiteralString) -> None:
#     pass

# def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
#     run_query("SELECT * FROM students")  # OK
#     run_query("SELECT * FROM users WHERE id = 1 OR 1=1") #SQL injection
#     run_query(literal_string)  # OK
#     run_query("SELECT * FROM " + literal_string)  # OK
#     run_query(arbitrary_string)  # type checker error
#     run_query(  # type checker error
#         f"SELECT * FROM students WHERE name = {arbitrary_string}"
#     )
# caller("SELECT * FROM students", "students")

####################################################################################################

# @override

# class Base:
#     def get_color() -> str:
#         return "blue"

# class GoodChild(Base):
#     @override
#     def get_color() -> str:
#         return "green"

# class BadChild(Base):
#     @override
#     def get_colour() -> str:
#         return "red"

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
