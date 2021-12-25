# https://python-course.eu/python-tutorial/passing-arguments.php

"""
Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object Reference" 
or "Call by Sharing".

If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value
The object reference is passed to the function parameters. They can't be changed within the function, because they 
can't be changed at all, i.e. they are immutable. It's different, if we pass mutable arguments. They are also passed 
by object reference, but they can be changed in place within the function. 

If we pass a list to a function, we have to consider two cases: Elements of a list can be changed in place, i.e. 
the list will be changed even in the caller's scope. If a new list is assigned to the name, the old list will 
not be affected, i.e. the list in the caller's scope will remain untouched.

First, let's have a look at the integer variables below. The parameter inside the function remains a reference 
to the argument's variable, as long as the parameter is not changed. As soon as a new value is assigned to it, 
Python creates a separate local variable. The caller's variable will not be changed this way:
"""

def ref_demo(x):
    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))

x = 9
print(id(x))
ref_demo(x)

"""
Python initially behaves like call-by-reference, but as soon as we change the value of such a 
variable, i.e. as soon as we assign a new object to it, Python "switches" to call-by-value. That is, a local 
variable x will be created and the value of the global variable x will be copied into it.


ide effects
A function is said to have a side effect, if, in addition to producing a return value, it modifies the caller's environment in other ways. For example, a function might modify a global or static variable, modify one of its arguments, raise an exception, write data to a display or file etc.

There are situations, in which these side effects are intended, i.e. they are part of the function's specification. But in other cases, they are not wanted , they are hidden side effects. In this chapter, we are only interested in the side effects that change one or more global variables, which have been passed as arguments to a function. Let's assume, we are passing a list to a function. We expect the function not to change this list. First, let's have a look at a function which has no side effects. As a new list is assigned to the parameter list in func1(), a new memory location is created for list and list becomes a local variable.

def no_side_effects(cities):
    print(cities)
    cities = cities + ["Birmingham", "Bradford"]
    print(cities)
locations = ["London", "Leeds", "Glasgow", "Sheffield"]
no_side_effects(locations)
OUTPUT:
['London', 'Leeds', 'Glasgow', 'Sheffield']
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
print(locations)
OUTPUT:
['London', 'Leeds', 'Glasgow', 'Sheffield']
This changes drastically, if we increment the list by using augmented assignment operator +=. To show this, we change the previous function rename it as "side_effects" in the following example:

def side_effects(cities):
    print(cities)
    cities += ["Birmingham", "Bradford"]
    print(cities)
 
locations = ["London", "Leeds", "Glasgow", "Sheffield"]
side_effects(locations)
OUTPUT:
['London', 'Leeds', 'Glasgow', 'Sheffield']
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
print(locations)
OUTPUT:
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
We can see that Birmingham and Bradford are included in the global list locations as well, because += acts as an in-place operation.

The user of this function can prevent this side effect by passing a copy to the function. A shallow copy is sufficient, because there are no nested structures in the list. To satisfy our French customers as well, we change the city names in the next example to demonstrate the effect of the slice operator in the function call:

def side_effects(cities):
    print(cities)
    cities += ["Paris", "Marseille"]
    print(cities)
 
locations = ["Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg"]
side_effects(locations[:])
print(locations) 
OUTPUT:
['Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg']
['Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Paris', 'Marseille']
['Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg']
print(locations)
OUTPUT:
['Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg']
We can see that the global list locations has not been effected by the execution of the function.


Variable Length of Parameters
We will introduce now functions, which can take an arbitrary number of arguments. Those who have some programming background in C or C++ know this from the varargs feature of these languages.

Some definitions, which are not really necessary for the following: A function with an arbitrary number of arguments is usually called a variadic function in computer science. To use another special term: A variadic function is a function of indefinite arity. The arity of a function or an operation is the number of arguments or operands that the function or operation takes. The term was derived from words like "unary", "binary", "ternary", all ending in "ary".

The asterisk "*" is used in Python to define a variable number of arguments. The asterisk character has to precede a variable identifier in the parameter list.

def varpafu(*x): 
    print(x)
varpafu()
OUTPUT:
()
varpafu(34,"Do you like Python?", "Of course")
OUTPUT:
(34, 'Do you like Python?', 'Of course')
We learn from the previous example that the arguments passed to the function call of varpafu() are collected in a tuple, which can be accessed as a "normal" variable x within the body of the function. If the function is called without any arguments, the value of x is an empty tuple.

Sometimes, it's necessary to use positional parameters followed by an arbitrary number of parameters in a function definition. This is possible, but the positional parameters always have to precede the arbitrary parameters. In the following example, we have a positional parameter "city", - the main location, - which always have to be given, followed by an arbitrary number of other locations:

def locations(city, *other_cities): print(city, other_cities)
locations("Paris")
locations("Paris", "Strasbourg", "Lyon", "Dijon", "Bordeaux", "Marseille")
OUTPUT:
Paris ()
Paris ('Strasbourg', 'Lyon', 'Dijon', 'Bordeaux', 'Marseille')
* in Function Calls
A * can appear in function calls as well, as we have just seen in the previous exercise: The semantics is in this case "inverse" to a star in a function definition. An argument will be unpacked and not packed. In other words, the elements of the list or tuple are singularized:

def f(x,y,z):
    print(x,y,z)

p = (47,11,12)
f(*p)
OUTPUT:
47 11 12
There is hardly any need to mention that this way of calling our function is more comfortable than the following one:

f(p[0],p[1],p[2])
OUTPUT:
47 11 12
Additionally, the previous call (f(p[0],p[1],p[2])) doesn't work in the general case, i.e. lists of unknown lengths. "Unknown" means that the length is only known at runtime and not when we are writing the script.

Arbitrary Keyword Parameters
There is also a mechanism for an arbitrary number of keyword parameters. To do this, we use the double asterisk "**" notation:

>>> def f(**args):
    print(args)
 
f()
OUTPUT:
{}
f(de="German",en="English",fr="French")
OUTPUT:
{'de': 'German', 'en': 'English', 'fr': 'French'}
Double Asterisk in Function Calls
The following example demonstrates the usage of ** in a function call:

def f(a,b,x,y):
    print(a,b,x,y)

d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)
OUTPUT:
append block extract yes
and now in combination with *:

t = (47,11)
d = {'x':'extract','y':'yes'}
f(*t, **d)
OUTPUT:
47 11 extract yes
Exercise
Write a function which calculates the arithmetic mean of a variable number of values.

Solution
def arithmetic_mean(x, *l):
     The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers 
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))
You might ask yourself, why we used both a positional parameter "x" and the variable parameter "l" in our function definition. We could have only used l to contain all our numbers. We wanted to enforce that we always have a non-empty list of numbers. This is necessary to prevent a division by zero error, because the average of an empty list of numbers is not defined.

In the following interactive Python session, we can learn how to use this function. We assume that the function arithmetic_mean is saved in a file called statistics.py.

from statistics import arithmetic_mean
arithmetic_mean(4,7,9)
6.666666666666667
arithmetic_mean(4,7,9,45,-3.7,99)
26.71666666666667
This works fine, but there is a catch. What if somebody wants to call the function with a list, instead of a variable number of numbers, as we have shown above? We can see in the following that we raise an error, as most hopefully, you might expect:

l = [4,7,9,45,-3.7,99]
arithmetic_mean(l)
OUTPUT:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-29-b0693d70ca11> in <module>
      1 l = [4,7,9,45,-3.7,99]
----> 2 arithmetic_mean(l)
NameError: name 'arithmetic_mean' is not defined
The rescue is using another asterisk:

arithmetic_mean(*l)
26.71666666666667

"""



