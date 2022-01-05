
import datetime
import time
import uuid
import math
import random
import os
import sys

for arg in sys.argv:
    print(arg)

now = datetime.datetime.now()
print(now.year)

print(time.time())
time.sleep(1000)
print(uuid.UUID)
print(int(math.sqrt(9)))
print(random.randint(0, 5))

def fizzBuzz(n):
    # Write your code here
    print("hello")

if __name__ == '__main__':
    n = int(input().strip())

fizzBuzz(n)


# Arbitrary Number of Parameters
def sumAll(*x):
    total = 0
    for i in x:
        total += i
    return total
x = [3, 5, 9]
print("Sum: " + str(sumAll(*x)))

def func(x,y,z):
    print(x,y,z)
p = (47,11,12)
func(*p)

# output into sys.stderr & sys.stdout:
import sys
print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

#Formatted output
print("%d" %(42.565512))

x = lambda a, b : a * b
print(x(5, 6))



