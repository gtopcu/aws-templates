# from collections import deque, defaultdict, namedtuple
# #import frozenset
# import datetime
# import time
# import os

# BIG_CONSTANT: int = 10000000


def main() -> None:
    # x, y = 3, 4
    # print(x, y)

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

    # print( (12 * 3) if True else 6 )
    # #print(time.time())
    # print(BIG_CONSTANT)
    # print("Done")

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

    dict = {x: x**2 for x in range(0, 10)}
    print(dict)
    print()


if __name__ == "__main__":
    main()
