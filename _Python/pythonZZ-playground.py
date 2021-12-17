
import datetime
import time
import math
import random

import os
os.system("clear") # Linux - OSX
#os.system("cls") # Windows

"""
x = 10
y = 100
print(str(x))
print(len(str(y)))
print(id(x))

for i in range(0, 10):
    print(i, sep="-", end="")

print("\ndone")

def myFunction(l, r):
    # Write your code here
    print("function inputs:", l, "-", r)

if __name__ == '__main__':
    myFunction(5, 6)
    print("running")

if x==9:
    print(9)
elif x==8:
    print(8)
else:
    print("Could not guess")

try:
    myFunction(1, 2)
except ValueError:
    print("Exception value error")

s = "Glückliche Fügung"
s_bytes = s.encode('utf-8') 
print(s_bytes)

myList = ["one", "two"]
myList.append("three")
myList.extend(["four"])
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)
myList.reverse()
print(myList)
print(myList.count("one"))

myStr = "one sentence one man"
print(myStr.upper())
print(myStr.capitalize())
print(myStr.title())
print(myStr.find("t"))
print(myStr.index("t"))
print(myStr.count("o"))

print(1 is not 1)
print('c' is 'C')
print("b" in "book")

myList2 = [1, 2, 3]
check = 1 in myList2
print(check)

if(2 in myList2):
    print(True)

myTuple = (1, 2, 3)
print(myTuple.count(0))
print(myTuple.index(3))
print(myTuple[2])

# Converting dictionaries & lists
myDict = { 
            "Gökhan": 36, 
            "Nurhan": 60
        }

myList = list(myDict)
print(myList)

myList2 = []
for key, value in myDict.items():
    myList2.append(key + "-" + str(value))
print(myList2)

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"," Switzerland"]
country_specialities = list(zip(countries, dishes))
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

iterable = zip(countries, dishes)
for country, dish in iterable:
    print(country, dish)

l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1, l2)
for i in c:
    print(i)

"""




















