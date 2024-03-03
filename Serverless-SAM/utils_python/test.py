
from collections import deque, defaultdict
import datetime
import time
import os

def main() -> None:
    
    # x, y = 3, 4
    # print(x, y)
    
    #print(f"Total time: {total_time:.3f}")    

    # char = "c"
    # match char:
    #     case "a":
    #         print("a")
    #     case "b":
    #         print("b")
    #     case _:
    #         print("default")

    # print(chr(100))

    my_list = [x for x in range(10) if x % 2 == 0]
    my_set = {i for i in range(10)}
    my_dict = {x: x ** 2 for x in range(10)}
    my_deque = deque(my_list, maxlen=5)
    print(my_deque)
    my_defaultdict = defaultdict(lambda: "default")    
    my_defaultdict = defaultdict(int)    
    print(my_defaultdict["NoKeyError"])

    print( (12 * 3) if True else 6 )    
    #print(time.time())
    print()
    print("Done")

if __name__ == "__main__":
    main()