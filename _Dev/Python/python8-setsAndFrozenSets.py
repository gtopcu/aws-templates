# https://python-course.eu/python-tutorial/sets-and-frozen-sets.php

# Sets:     Contains an unordered collection of unique and immutable objects - Like HashSet
#           Thus cannot contain lists or dictionaries as elements
#           Unlike lists or tuples can't have multiple occurrences of the same element
#
#           add(e)
#           pop() - removes and returns an arbitrary element, throws KeyError if empty
#           discard(e)
#           remove(e) - throws KeyError if not present
#           update()
#           clear()
#           copy()
#           difference()
#           difference_update()
#           intersection()
#           union()
#           isdisjoint()
#           issubset()
#           issuperset()
#           symmetric_difference()           
#

import os
os.system("clear") # Linux - OSX
#os.system("cls") # Windows

definingASet = { 'i', 'j', 's', 'a', 't', 'h', 'e', ' ' }
print(definingASet)

mySet = set("iiijj this is a set")
print(mySet)

# Passing a tuple
mySet2 = set((1, 2, 2, 3, 3, 3))
print(mySet2)

# Passing a list
mySet3 = set(["Perl", "Python", "Java"])
print(len(mySet3), mySet3)

# Though sets can't contain mutable objects, sets are mutable:
cities = set(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print(cities)

# Frozensets are like sets except that they cannot be changed, i.e. they are immutable:
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")



"""
A set is a well-defined collection of objects.
The elements or members of a set can be anything: numbers, characters, words, names, letters of the alphabet, 
even other sets, and so on. 

Sets are usually denoted with capital letters.

The data type "set", which is a collection type, has been part of Python since version 2.4. 
A set contains an unordered collection of unique and immutable objects. The set data type is, 
as the name implies, a Python implementation of the sets as they are known from mathematics. 

This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.


Immutable Sets
Sets are implemented in a way, which doesn't allow mutable objects. The following example demonstrates 
that we cannot include, for example, lists as elements:

cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))

OUTPUT
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-5a60d6eeb901> in <module>
----> 1 cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
      2 
      3 cities
TypeError: unhashable type: 'list'

Tuples on the other hand are fine:
cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))

difference()
This method returns the difference of two or more sets as a new set, leaving the original set unchanged.

x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
x.difference(y) 
OUTPUT:
{'a', 'd', 'e'}
x.difference(y).difference(z)
OUTPUT:
{'a', 'e'}
Instead of using the method difference, we can use the operator "-":

x - y
OUTPUT:
{'a', 'd', 'e'}
x - y - z
OUTPUT:
{'a', 'e'}
difference_update()
The method difference_update removes all elements of another set from this set. x.difference_update(y) is the same as "x = x - y" or even x -= y works.

x = {"a","b","c","d","e"}
y = {"b","c"}
x.difference_update(y)
x = {"a","b","c","d","e"}
y = {"b","c"}
x = x - y
x
OUTPUT:
{'a', 'd', 'e'}
discard(el)
An element el will be removed from the set, if it is contained in the set. If el is not a member of the set, nothing will be done.

x = {"a","b","c","d","e"}
x.discard("a")
x    
OUTPUT:
{'b', 'c', 'd', 'e'}
x.discard("z")
x   
OUTPUT:
{'b', 'c', 'd', 'e'}
remove(el)
Works like discard(), but if el is not a member of the set, a KeyError will be raised.

x = {"a","b","c","d","e"}
x.remove("a")
x   
OUTPUT:
{'b', 'c', 'd', 'e'}
x.remove("z")    
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-18-7c787df95113> in <module>
----> 1 x.remove("z")
KeyError: 'z'
union(s)
This method returns the union of two sets as a new set, i.e. all elements that are in either set.

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x.union(y)   
OUTPUT:
{'a', 'b', 'c', 'd', 'e', 'f', 'g'}
This can be abbreviated with the pipe operator "|":

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x | y
OUTPUT:
{'a', 'b', 'c', 'd', 'e', 'f', 'g'}
intersection(s)
Returns the intersection of the instance set and the set s as a new set. In other words, a set with all the elements which are contained in both sets is returned.

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x.intersection(y)
OUTPUT:
{'c', 'd', 'e'}
This can be abbreviated with the ampersand operator "&":

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x  & y
OUTPUT:
{'c', 'd', 'e'}
isdisjoint()
This method returns True if two sets have a null intersection.
x = {"a","b","c"}
y = {"c","d","e"}
x.isdisjoint(y)
OUTPUT:
False
x = {"a","b","c"}
y = {"d","e","f"}
x.isdisjoint(y) 
OUTPUT:
True
issubset()
x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for "Subset of" and ">=" for "superset of"
"<" is used to check if a set is a proper subset of a set.  
x = {"a","b","c","d","e"}
y = {"c","d"}
x.issubset(y)
OUTPUT:
False
y.issubset(x)
OUTPUT:
True
x < y
OUTPUT:
False
y < x # y is a proper subset of x   
OUTPUT:
True
x < x # a set can never be a proper subset of oneself.
OUTPUT:
False
x <= x 
OUTPUT:
True
issuperset()
x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation for "issuperset of"
">" is used to check if a set is a proper superset of a set.    
x = {"a","b","c","d","e"}
y = {"c","d"}
x.issuperset(y)
OUTPUT:
True
x > y
OUTPUT:
True
x >= y
OUTPUT:
True
x >= x   
OUTPUT:
True
x > x
OUTPUT:
False
x.issuperset(x)
OUTPUT:
True
pop()
pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty.
x = {"a","b","c","d","e"}
x.pop()
OUTPUT:
'e'
x.pop()
OUTPUT:
'a'



"""

