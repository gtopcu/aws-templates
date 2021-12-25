# https://python-course.eu/python-tutorial/functions.php

def greet(name):
    print("Hi " + name)

def multiply(x, y):
    return "Result: " + str(x * y)

def doNothing():
    pass

print("Program starts")

greet("Peter")  
print(multiply(2, 3))

# Default values
def greet2(name="everybody"):
    print("Hi " + name)
greet2()

# Careful - persistent across multiple calls
def spammer(bag=[]):
    bag.append("spam")
    return bag
print("spammer.__defaults__", spammer.__defaults__)

# Re-created every time, immutable
def spammer(bag=None):
    if bag is None:
        bag = []
    bag.append("spam")
    return bag

# Docstring
# The first statement in the body of a function is usually a string statement called a Docstring, 
# which can be accessed with the function_name.__doc__. For example:
def hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")
print("The docstring of the function hello: " + hello.__doc__)

# Keyword Parameters
def sumsub(a, b, c=0, d=0):
    return a - b + c - d

print(sumsub(12, 4))
print(sumsub(42, 15, d=10))

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

def varpafu(*x): 
    print(x)
varpafu(34,"Do you like Python?", "Of course")
#OUTPUT is a tuple: (34, 'Do you like Python?', 'Of course')

#city is mandatory
def locations(city, *other_cities): 
    print(city, other_cities)
locations("Paris")
locations("Paris", "Strasbourg", "Lyon")

# Keywords
def f(**args):
    print(args)
f(de="German",en="English",fr="French")

# Double Asterisk in Function Calls
def f(a,b,x,y):
    print(a,b,x,y)
d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)
#OUTPUT: append block extract yes
#and now in combination with *:
t = (47,11)
d = {'x':'extract','y':'yes'}
f(*t, **d)
# OUTPUT: 47 11 extract yes

# Global variables
def f():
    global s
    print(s)
    s = "dog"       # globally changed
    print(s)     
def g():
    s = "snake"     # local s
    print(s) 
s = "cat" 
f()
print(s)
g()
print(s)

# Returning multiple values with lists/tuples:
def fib_interval(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    old, new = 0, 1
    while True:
        if new < x:
            old, new = new, old+new
        else:
            if new == x: 
                new = old + new
            return (old, new)
            
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    lub, sup = fib_interval(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))



"""

Local and Global Variables in Functions
Variable names are by default local to the function, in which they get defined.

def f(): 
    print(s)      # free occurrence of s in f
    
s = "Python"
f()
OUTPUT:
Python
def f(): 
    s = "Perl"     # now s is local in f
    print(s)
    
s = "Python"
f()
print(s)
OUTPUT:
Perl
Python
def f(): 
    print(s)        # This means a free occurrence, contradiction to bein local
    s = "Perl"      # This makes s local in f
    print(s)


s = "Python" 
f()
print(s)
OUTPUT:
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-25-81b2fbbc4d42> in <module>
      6 
      7 s = "Python"
----> 8 f()
      9 print(s)
<ipython-input-25-81b2fbbc4d42> in f()
      1 def f():
----> 2     print(s)
      3     s = "Perl"
      4     print(s)
      5 
UnboundLocalError: local variable 's' referenced before assignment
If we execute the previous script, we get the error message: UnboundLocalError: local variable 's' referenced before assignment.

The variable s is ambigious in f(), i.e. in the first print in f() the global s could be used with the value "Python". After this we define a local variable s with the assignment s = "Perl".

def f():
    global s
    print(s)
    s = "dog"
    print(s) 
s = "cat" 
f()
print(s)
OUTPUT:
cat
dog
dog
We made the variable s global inside of the script. Therefore anything we do to s inside of the function body of f is done to the global variable s outside of f.

def f():
    global s
    print(s)
    s = "dog"       # globally changed
    print(s)     

def g():
    s = "snake"     # local s
    print(s) 

s = "cat" 
f()
print(s)
g()
print(s)
OUTPUT:
cat
dog
dog
snake
dog


Arbitrary Number of Parameters
There are many situations in programming, in which the exact number of necessary parameters cannot be determined a-priori. An arbitrary parameter number can be accomplished in Python with so-called tuple references. An asterisk "*" is used in front of the last parameter name to denote it as a tuple reference. This asterisk shouldn't be mistaken for the C syntax, where this notation is connected with pointers. Example:

def arithmetic_mean(first, *values):
     "This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values"

    return (first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
OUTPUT:
61.0
42502.3275
38.5
45.0
This is great, but we have still have one problem. You may have a list of numerical values. Like, for example,

x = [3, 5, 9]
You cannot call it with

 arithmetic_mean(x)
because "arithmetic_mean" can't cope with a list. Calling it with

 
arithmetic_mean(x[0], x[1], x[2])
OUTPUT:
5.666666666666667
is cumbersome and above all impossible inside of a program, because list can be of arbitrary length.

The solution is easy: The star operator. We add a star in front of the x, when we call the function.

 arithmetic_mean(*x)
OUTPUT:
5.666666666666667
This will "unpack" or singularize the list.

A practical example for zip and the star or asterisk operator: We have a list of 4, 2-tuple elements:

my_list = [('a', 232), 
           ('b', 343), 
           ('c', 543), 
           ('d', 23)]
We want to turn this list into the following 2 element, 4-tuple list:

 [('a', 'b', 'c', 'd'), 
 (232, 343, 543, 23)] 
This can be done by using the *-operator and the zip function in the following way:

list(zip(*my_list))
OUTPUT:
[('a', 'b', 'c', 'd'), (232, 343, 543, 23)]
Arbitrary Number of Keyword Parameters
In the previous chapter we demonstrated how to pass an arbitrary number of positional parameters to a function. It is also possible to pass an arbitrary number of keyword parameters to a function as a dictionary. To this purpose, we have to use the double asterisk "**"

def f(**kwargs):
    print(kwargs)
f()
OUTPUT:
{}
f(de="German",en="English",fr="French")
OUTPUT:
{'de': 'German', 'en': 'English', 'fr': 'French'}
One use case is the following:

def f(a, b, x, y):
    print(a, b, x, y)
d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)
OUTPUT:
append block extract yes

"""

