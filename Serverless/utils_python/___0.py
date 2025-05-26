

my_set = {0, 1, 2} # set()
# if 0 in my_set | if 0 not in my_set 
my_set.add(1)
my_set.remove(1)
my_set.discard(1)
my_set.pop()
my_set.update()
my_set.union()
my_set.copy()
my_set.clear()
my_set.issubset()
my_set.issuperset()
my_set.isdisjoint()
my_set.difference()
my_set.difference_update()
my_set.intersection()
my_set.intersection_update()
my_set.symmetric_difference()
my_set.symmetric_difference_update()

my_list = [0, 1, 2]
del my_list[0]
my_list.append(3)
my_list.extend([4, 5])
my_list.insert(0, "A")
my_list.pop()
my_list.count(0)
my_list.remove(0)
my_list.copy()
my_list.clear()
my_list.sort(reverse=True)
my_list.reverse()
my_list.



# import os
# from pathlib import Path

# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('.'):
#     for filename in filename:
#         counter = 0
#         # print(os.path.join(dirname, filename))
#         if filename.endswith(".py"):
#             with open(os.path.join(dirname, filename), "r") as file:
#                 text = file.read()
#                 print(filename, len(text))

# path = Path(__file__)
# print(path)

# path.glob("*.py")
# path.rglob("*.py")

# data:bytes = path.read_bytes()
# text: str = data.decode("utf-8", errors="replace")
# text = path.read_text("utf-8", errors="replace", newline="\n")

# from io import TextIOWrapper
# with path.open(mode="r", buffering=-1, encoding="utf-8", errors="replace", newline="\n") as file:
#     print(file.read(-1))

# for dirpath, dirnames, filenames in path.parent.walk():
#     print(dirpath, dirnames, filenames)

# path = Path().cwd()
# for p in path.iterdir():
#     print(p.absolute())

# from collections.abc import Generator
# def simple_generator() -> Generator[int, None, None]:
#     yield 1
#     yield 2

# gen = simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen)) # StopIteration

# def numbers_generator(n):
#     for i in range(n):
#         yield i

# gen = numbers_generator(2)
# print(next(gen))
# print(next(gen))
# print(next(gen)) # StopIteration

# mylist = [*range(5)]
# iter = iter(mylist)
# print(next(iter))
# print(next(iter))

# mylist = [i for i in range(5)]
# gen = (i for i in range(5))
# print(next(gen))

"""
In Python, yield is a keyword used to create generator functions. 
yield is like return, but instead of ending the function and returning a single value, it *pauses* the function and produces a value. 
The function can then be resumed from where it left off.

def simple_generator():
    yield 1
    yield 2

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen)) # StopIteration

## Key differences from return
- return ends the function completely
- yield pauses the function and can be called multiple times
- Functions with yield return a generator object, not the actual values

def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Blast off!"

for value in countdown(3):
    print(value)
# 3
# 2
# 1
# Blast off!

## Memory efficiency
Generators created with yield are memory-efficient because they generate values on-demand rather than creating all values at once:

# This would use a lot of memory for large ranges
def numbers_list(n):
    return [i for i in range(n)]

# This uses minimal memory
def numbers_generator(n):
    for i in range(n):
        yield i

## Common use cases
- Processing large datasets without loading everything into memory
- Creating infinite sequences
- Pipeline processing where you transform data step by step

The yield keyword essentially turns any function into an iterator that you can loop through or call next() on.
"""
