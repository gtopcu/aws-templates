
import datetime
import time
import uuid
import math
import random

now = datetime.datetime.now()
print(now.year)

print(time.time())
print(uuid.UUID)

print(int(math.sqrt(9)))
print(random.randint(0, 5))

a =  3.564
print("a = \n", a)
print("a", 1, "b", 2, sep=":", end="")


#%%timeit  
d = {"a":123, "b":34, "c":304, "d":99}
for key in d.keys():
    x = d[key]
#%%timeit  
d = {"a":123, "b":34, "c":304, "d":99}
for value in d.values():
    x = value
#%%timeit  


def function(l, r):
    # Write your code here
    print("running")

if __name__ == '__main__':
    n = int(input().strip())
    print("running")