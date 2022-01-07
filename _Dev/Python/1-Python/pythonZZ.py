"""
x = [ "2", "1" , "-1"]
y = sorted(x)
print(y)

sortme = "heey sort me"
print(sortme)

say = "helloooo"
for c in (enumerate)(say):
    print(c)

print(say[::-1])
print("%d" %(42.565512))

joined = " / ".join(x)
print(joined)

x = 10 ** 2
print(x)
x = 10 // 3
print(x)
x = 10 / 3
print(x)
print(f"hey! {x}")

z = 10
def f1():
    z = 11
    def f2():
        #global z
        z=12
        print(z)
    f2()
f1()
print(z)

def funx(x, y, z=1):
    print(str(x) + " " + str(y) + " " + str(z))
funx(1, 2)
funx(y=5, x=10)
#funx(y=3, 6, x=9) will give error

def funy(func, *arg):
    func(*arg)
funy(funx, 1, 2, 3)

from urllib import *
import datetime
import time
import uuid
import math

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

q = queue.Queue()

def f():
    print("hola")

threading.Thread(target=f).start()
"""

x = 9
y = 10

