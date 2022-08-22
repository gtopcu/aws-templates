
import os
import sys
import datetime
import time
from tkinter import E

os.system("clear")
sys.argv[0]

print("hi")
#print(os.getenv("ltr"), "default")
#print(os.environ["USER"])
#print(dict(os.environ))
#print(os.environ)

now = datetime.datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	

#myVar = " adfhDf "
#print(myVar.strip().upper())

#myTuple = (1, 1, 2, 2, 3)
#print(myTuple.index(2))

# myList = [3, 1, 2]
# myList.sort()
# myList.reverse()
# myList.append(4)
# print(myList)

myDict = { "Gokhan": 37, "Goknur": "31" }
print(myDict)
for key, value in myDict.items():
    print(key, value)


