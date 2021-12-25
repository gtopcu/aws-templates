
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

def fizzBuzz(n):
    # Write your code here
    print("hello")

if __name__ == '__main__':
    n = int(input().strip())

fizzBuzz(n)
