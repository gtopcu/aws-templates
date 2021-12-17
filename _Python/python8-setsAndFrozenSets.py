# https://python-course.eu/python-tutorial/sets-and-frozen-sets.php

# Sets:     Contains an unordered collection of unique and immutable objects
#           Unlike lists or tuples can't have multiple occurrences of the same element
#
#
#
#

import os
os.system("clear") # Linux - OSX
#os.system("cls") # Windows

definingASet = { 'i', 'j', 's', 'a', 't', 'h', 'e', ' ' }
print(definingASet)

mySet = set("iiiiiijjjjjjj this is a set")
print(mySet)

# Passing a tuple
mySet2 = set((1, 2, 2, 3, 3, 3))
print(mySet2)

# Passing a list
x = set(["Perl", "Python", "Java"])
print(x)





"""
A set is a well-defined collection of objects.
The elements or members of a set can be anything: numbers, characters, words, names, letters of the alphabet, 
even other sets, and so on. 

Sets are usually denoted with capital letters.

The data type "set", which is a collection type, has been part of Python since version 2.4. 
A set contains an unordered collection of unique and immutable objects. The set data type is, 
as the name implies, a Python implementation of the sets as they are known from mathematics. 

This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

"""

