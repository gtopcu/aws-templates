
# https://python-course.eu/python-tutorial/sequential-data-types.php

# Sequences are one of the principal built-in data types besides numerics, mappings, files, instances 
# and exceptions. Python provides for six sequence (or sequential) data types:
# 
# strings
# byte sequences
# byte arrays
# lists
# tuples
# range objects
#
text = "Lists and Strings can be accessed via indices!"
print(text[0], text[10], text[-1])  

# Accessing lists:
cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
print(cities[0])
print(cities[2])
print(cities[-1])  

# Unlike other programming languages Python uses the same syntax and function names to work on 
# sequential data types. For example, the length of a string, a list, and a tuple can be determined 
# with a function called len():
countries = ["Germany", "Switzerland", "Austria", 
             "France", "Belgium", "Netherlands", 
             "England"]
print(len(countries))

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(len(fib))


# Bytes
# The byte object is a sequence of small integers. The elements of a byte object are in the range 0 to 255, 
# corresponding to ASCII characters and they are printed as such.
s = "Glückliche Fügung"
s_bytes = s.encode('utf-8') 
print(s_bytes)


# Python Lists
# Lists are related to arrays of programming languages like C, C++ or Java, but Python lists are by far more 
# flexible and powerful than "classical" arrays. For example, not all the items in a list need to have the same 
# type. Furthermore, lists can grow in a program run, while in C the size of an array has to be fixed at compile 
# time. Generally speaking a list is a collection of objects. To be more precise: A list in Python is an ordered 
# group of items or elements. It's important to notice that these list elements don't have to be of the same type. 
# It can be an arbitrary mixture of elements like numbers, strings, other lists and so on.

# The main properties of Python lists:
# They are ordered
# They can contain arbitrary objects
# Elements of a list can be accessed by an index
# They are arbitrarily nestable, i.e. they can contain other lists as sublists
# Variable size
# They are mutable, i.e. the elements of a list can be changed
arbitraryList = [42, "What's the question?", 3.1415]
print(arbitraryList)

nestedList = [["London","England", 7556900], ["Paris","France",2193031], ["Bern", "Switzerland", 123466]]
print(nestedList)

# Changing list
languages = ["Python", "C", "C++", "Java", "Perl"]
languages[4] = "Lisp"
languages.append("Haskell")
languages.insert(1, "Perl")
languages = languages.pop() #removes the last element of the list and returns it

# With a while loop:
shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []
while shopping_list != []:
    article = shopping_list.pop()  
    cart.append(article)
    print(article, shopping_list, cart)
print("shopping_list: ", shopping_list)
print("cart: ", cart)


# Tuples
# A tuple is an immutable list, i.e. a tuple cannot be changed in any way, once it has been created. 
# A tuple is defined analogously to lists, except the set of elements is enclosed in parentheses instead 
# of square brackets. The rules for indices are the same as for lists. Once a tuple has been created, 
# you can't add elements to a tuple or remove elements from a tuple.

# Where is the benefit of tuples?
# • Tuples are faster than lists.
# • If you know that some data doesn't have to be changed, you should use tuples instead of lists, 
#   because this protects your data against accidental changes.
# • The main advantage of tuples is that tuples can be used as keys in dictionaries, while lists can't.

# The following example shows how to define a tuple and how to access a tuple. Furthermore, we can see that 
# we raise an error, if we try to assign a new value to an element of a tuple:

t = ("tuples", "are", "immutable")
print(t[0])

#t[0] = "assignments to elements are not possible"
# OUTPUT: TypeError: 'tuple' object does not support item assignment


# Slicing
slogan = "Python is great"
first_six = slogan[0:6]
print(first_six)

starting_at_five = slogan[5:]
print(starting_at_five)

a_copy = slogan[:]
without_last_five = slogan[0:-5]
print(without_last_five)

# Syntactically, there is no difference on lists:
cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
first_three = cities[0:3]
print(first_three)

# Checking if an Element is Contained in List
abc = ["a","b","c","d","e"]
print("a" in abc)
print("a" not in abc)
