# https://www.youtube.com/watch?v=T8UXgR-EtoM

# Faster list/set comprehension
# Formalized & multi-line f-strings
# Better error descriptions

####################################################################################################
# 1 - Generics

# class MyClass[T]:
#     def myFunc(input: T) -> T:
#         return T

# def myFunc[T](input: list[T]) -> T:
#     return input

# type Point = tuple[float, float]
# type Points[T] = tuple[T, T]

####################################################################################################
# 2 - TypedDict

# https://peps.python.org/pep-0589/

# from typing import TypedDict, Unpack

# class Movie(TypedDict, total=False)):
#     name: str
#     year: int

# def foo(**kwargs: Unpack[Movie]):
#     print(kwargs)
#     print(kwargs["name"])

# foo(name="The Matrix", year=1999)

####################################################################################################
# 3 - itertools.batched()

# from itertools import batched

# for batch in batched('ABCDEFG', 3):
#     print(batch)

####################################################################################################
# 4 - @override

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