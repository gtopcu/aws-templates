# https://www.youtube.com/watch?v=T8UXgR-EtoM
# https://docs.python.org/3/library/typing.html

# Union: str | int

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

# from typing import TypedDict, TypeVar, TypeAlias, NewType, Literal
# my_type = int -> type alias
# print(my_type(3))
# my_type = NewType("my_type", int)

# my_type = tuple[int, str]
# var: my_type = (10, "hi")

# Strings: TypeAlias = list[str]
# strings: Strings = ["hi", "hello"]
# Basket: TypeAlias = list[Fruit]  -> Fruit not defined yet

# Mode: TypeAlias = Literal["read", "write", "append"]

# from typing import LiteralString #for preventing SQL injection
# def run_query(sql: LiteralString) -> None:
#     pass


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

# TypedDict

# https://peps.python.org/pep-0589/

# from typing import TypedDict, Unpack, Required, NotRequired

# https://docs.python.org/3/library/typing.html#typing.TypedDict
# class Movie(TypedDict, total=False): #total: all fields required
#     name: Required[str]
#     year: int
#     rating: NotRequired[float]
#     duration: Required[int]

# movie: Movie = {"name": "The Matrix", "year": 1999, "duration": 136}

# my_typedict = TypedDict("MyDict", {"name": str, "age": Required[int]}, total=False)
# my_typedict = TypedDict("MyDict", name=str, age=Required[int]) # deprecated, will be removed in 3.13

# def foo(**kwargs: Unpack[Movie]):
#     print(kwargs)
#     print(kwargs["name"])

# foo(name="The Matrix", year=1999)

####################################################################################################

# from typing import overload
# @overload
# def utf8(value: None) -> None: ...
# @overload
# def utf8(value: bytes) -> bytes: ...
# @overload
# def utf8(value: str) -> bytes: ...


# from overrides import override

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
# Generics

# class MyClass[T: (int, float)]:
#     def myFunc(input: T) -> T:
#         return T

# def myFunc[T](input: list[T]) -> T:
#     return input

# type Point = tuple[float, float]
# type Points[T] = tuple[T, T]

