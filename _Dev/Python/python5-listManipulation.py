
# append(obj)
# pop({pos})
# extend(obj)
# remove(obj)
# index(x, {start}, {end})
# count(obj) -> int
# insert(index, obj)
# sort(reverse=True)
# reverse()
# copy()
# deepcopy

# append()  Put a new object to the end of the list, returns None
#
# pop()     Returns the element from the list and removes it 
#           Raises an IndexError exception, if the list is empty or the index is out of range
#           Can be called without an argument, s.pop() is equivalent to s.pop(-1)

lst = ["easy", "simple", "cheap", "free"]
lst.append("happy")
print(lst[-1])

popped = lst.pop(0)
print(lst)

# extend()  Extends a list by appending all the elements of an iterable like a list, a tuple or a string 
#           The argument doesn't have to be a list, can be any kind of iterable i.e. tuples, strings

lst = [42, 98, 77]
lst2 = [8, 69]
lst.extend(lst2)
print(lst)

lst = ["a", "b", "c"]
programming_language = "Python"
lst.extend(programming_language)
print(lst)

# Now with a tuple:
lst = ["Java", "C", "PHP"]
t = ("C#", "Jython", "Python", "IronPython")
lst.extend(t)
print(lst)

# There is an alternative to 'append' and 'extend'. '+' can be used to combine lists, but USE APPEND!!
level = ["beginner", "intermediate", "advanced"]
other_words = ["novice", "expert"]
print(level + other_words)

"""""

Be careful. Never ever do the following:

L = [3, 4]
L = L + [42]
L
OUTPUT:
[3, 4, 42]
Even though we get the same result, it is not an alternative to 'append' and 'extend':

L = [3, 4]
L.append(42)
L
OUTPUT:
[3, 4, 42]

L = [3, 4]
L.extend([42])
L
OUTPUT:
[3, 4, 42]

The augmented assignment (+=) is an alternative:
L = [3, 4]
L += [42]
L
OUTPUT:
[3, 4, 42]

In the following example, we will compare the different approaches and calculate their run times. 
To understand the following program, you need to know that time.time() returns a float number, 
the time in seconds since the so-called  The Epoch''1. time.time() - start_time calculates the time 
in seconds used for the for loops:

import time
n= 100000
start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)
OUTPUT:
29.277812480926514

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)
OUTPUT:
0.04687356948852539

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)
OUTPUT:
0.03689885139465332

This program returns shocking results:

We can see that the "+" operator is about 1268 times slower than the append method. 
The explanation is easy: If we use the append method, we will simply append a further element 
to the list in each loop pass. Now we come to the first loop, in which we use l = l + [i * 2]. 
The list will be copied in every loop pass. The new element will be added to the copy of the 
list and result will be reassigned to the variable l. After that, the old list will have to be 
removed by Python, because it is not referenced anymore. We can also see that the version with 
the augmented assignment ("+="), the loop in the middle, is only slightly slower than the version 
using "append".

"""

# remove():     Remove a certain value from a list without knowing the position

"""
s.remove(x) 
This call will remove the first occurrence of 'x' from the list 's'. If 'x' is not in the list, 
a ValueError will be raised. We will call the remove method three times in the following example to 
remove the colour "green". As the colour "green" occurrs only twice in the list, we get a ValueError 
at the third time:

colours = ["red", "green", "blue", "green", "yellow"]
colours.remove("green")
colours
OUTPUT:
['red', 'blue', 'green', 'yellow']
colours.remove("green")
colours
OUTPUT:
['red', 'blue', 'yellow']
colours.remove("green")
OUTPUT:
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-26-278a6b3f3483> in <module>
----> 1 colours.remove("green")
ValueError: list.remove(x): x not in list
Find the Position of an Element in a List
"""

# index(x, {start}, {end}): Can be used to find the position of an element within a list
#                           start & end optional    

"""
s.index(x[, i[, j]]) 
It returns the first index of the value x. A ValueError will be raised, if the value is not present. 
If the optional parameter i is given, the search will start at the index i. 
If j is also given, the search will stop at position j.

colours = ["red", "green", "blue", "green", "yellow"]
colours.index("green")
OUTPUT:
1
colours.index("green", 2)
OUTPUT:
3
colours.index("green", 3,4)
OUTPUT:
3
colours.index("black")
OUTPUT:
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-30-b6026e7dbb87> in <module>
----> 1 colours.index("black")
ValueError: 'black' is not in list
"""

# insert(index, object)     Inserts an object before the given index position

""""
 s.insert(index, object)

An object "object" will be included in the list "s". 
"object" will be placed before the element s[index]. 
s[index] will be "object" and all the other elements will be moved one to the right.

lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
lst
OUTPUT:
['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland']
The functionality of the method "append" can be simulated with insert in the following way:

abc = ["a","b","c"]
abc.insert(len(abc),"d")
abc
OUTPUT:
['a', 'b', 'c', 'd']

Footnotes:

1 Epoch time (also known as Unix time or POSIX time) is a system for describing instants in time, 
defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), 
Thursday, 1 January 1970, not counting leap seconds.


COPY and Deep Copy
https://python-course.eu/python-tutorial/shallow-and-deep-copy.php

# COPY - List references exactly the same objects, nested lists tuples dicts etc
person1 = ["Mike", ["5th Avenue", "NYC"]]
person2 = person1.copy()
person2[0] = "Sarah"
person2[1][0] = "6th Avenue"
print(person2)
print(person1)

# DEEP COPY - Creates new lists tuples dicts. Strings reference the same objects
from copy import deepcopy
person1 = ["Mike", ["5th Avenue", "NYC"]]
person2 = deepcopy(person1)
person2[0] = "Sarah"
person2[1][0] = "6th Avenue"
print(person2)
print(person1)


"""