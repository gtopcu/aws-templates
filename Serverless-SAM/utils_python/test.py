from collections import deque, defaultdict, namedtuple, ChainMap
# #import frozenset
# import datetime
# import time
# import os

# BIG_CONSTANT: int = 10000000


def main() -> None:

    # time = time.perf_counter
    # print(f"Total time: {total_time:.3f}")

    # char = "c"
    # match char:
    #     case "a":
    #         print("a")
    #     case "b":
    #         print("b")
    #     case _:
    #         print("default")

    # print(chr(100))

    # my_list = [x for x in range(10) if x % 2 == 0]
    # my_set = {i for i in range(10)}
    # my_set2 = set()
    # # my_frozenset = frozenset(my_list)
    # my_dict = {x: x ** 2 for x in range(10)}
    # my_deque = deque(my_list, maxlen=5)
    # print(my_deque)
    # my_defaultdict = defaultdict(lambda: "default")
    # my_defaultdict = defaultdict(int)
    # print(my_defaultdict["NoKeyError"])

    # x, y = 1, 2
    # x = (12 * 3) if True else 6
    # print(time.time())
    # print("Done")

    # myint = 10
    # myfloat = float(myint)
    # print(type(myfloat))

    # tuple1 = (1, )
    # print(type(tuple1))

    # list = [x for x in range(0, 10, 2)]
    # list2 = [x*x for x in range(0, 10) if x%2==1]
    # print(list.count(2))
    # print(list.index(1))
    # print(list.extend(list2))
    # print(list.pop(0))
    # print(list.remove(2))
    # print(list.reverse())
    # list.sort(reverse=True)
    # print(list)
    # for i, j in enumerate(list):
    #     print(i, j)
    # for filtered in filter(lambda x: x % 4 == 0, list):
    #     print(filtered)
    # for mapped in map(lambda x: x * x, list):
    #     print(mapped)
    # iterator = iter(list)
    # while iterator:
    #     print(next(iterator))

    # dict = {x: x**2 for x in range(0, 10)}
    # print(dict.popitem())
    # print(dict.pop(0))
    # print(dict.get(10, 100))
    # print(dict[2])
    # print(dict)
    # dict2 = dict.fromkeys([1, 2, 3], 0)
    # print(dict2)
    # dict.update(dict2)
    # print(dict)
    # print(dict.setdefault(9, 81))
    # del dict[9]
    # print(dict)

    # Student = namedtuple('Student', ['name', 'age', 'DOB'])
    # S = Student('Nandini', '19', '2541997')
    # print(S[1])
    # print(S.name)
    
    # d1 = {'a': 1, 'b': 2}  
    # d2 = {'c': 3, 'd': 4}  
    # chain = ChainMap(d1, d2)
    # print (chain.maps) 
    # print (list(chain.keys())) 
    # print (list(chain.values())) 

    # mydict = {"a": 1, "b": 2}
    # defined_kwargs(**mydict)
    defined_kwargs(**{"a": 1, "b": 2})
    #defined_kwargs(arg1=1, arg2=2)
    
    print("done", end="\n")

# def int_or_none() -> int | None:
#     return None
    
def defined_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        # print(type(key))
        print(key, value)

# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

if __name__ == "__main__":
    main()
