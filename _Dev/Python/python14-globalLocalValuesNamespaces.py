
# https://python-course.eu/python-tutorial/global-local-variables-namespaces.php

"""
The way Python uses global and local variables is maverick. While in many or most other programming languages 
variables are treated as global if not declared otherwise, Python deals with variables the other way around. 
They are local, if not otherwise declared. The driving reason behind this approach is that global variables 
are generally bad practice and should be avoided. In most cases where you are tempted to use a global variable, 
it is better to utilize a parameter for getting a value into a function or return a value to get it out. 
Like in many other program structures, Python also imposes good programming habit by design.

So when you define variables inside a function definition, they are local to this function by default. 
That is, anything you will do to such a variable in the body of the function will have no effect on other 
variables outside of the function, even if they have the same name. In other words, the function body is 
the scope of such a variable, i.e. the enclosing context where this name is associated with its values.

All variables have the scope of the block, where they are declared and defined. They can only be used after the 
point of their declaration.

Just to make things clear: Variables don't have to be and can't be declared in the way they are declared in 
programming languages like Java or C. Variables in Python are implicitly declared by defining them, i.e. 
the first time you assign a value to a variable, this variable is declared and has automatically the data 
type of the object which has to be assigned to it. 

Global and local Variables in Functions
In the following example, we want to demonstrate, how global values can be used inside the body of a function:

def f(): 
    print(s) 
s = "I love Paris in the summer!"
f()
OUTPUT:
I love Paris in the summer!
The variable s is defined as the string "I love Paris in the summer!", before calling the function f(). The body of f() consists solely of the "print(s)" statement. As there is no local variable s, i.e. no assignment to s, the value from the global variable s will be used. So the output will be the string "I love Paris in the summer!". The question is, what will happen, if we change the value of s inside of the function f()? Will it affect the global variable as well? We test this in the following piece of code:

def f(): 
    s = "I love London!"
    print(s) 

s = "I love Paris!" 
f()
print(s)
OUTPUT:
I love London!
I love Paris!
What if we combine the first example with the second one, i.e. we first access s with a print() function, hoping to get the global value, and then assigning a new value to it? Assigning a value to it, means - as we have previously stated - creating a local variable s. So, we would have s both as a global and a local variable in the same scope, i.e. the body of the function. Python fortunately doesn't allow this ambiguity. So, it will raise an error, as we can see in the following example:

def f(): 
   print(s)
   s = "I love London!"
   print(s)
 
s = "I love Paris!"
f()
OUTPUT:
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-3-d7a23bc83c27> in <module>
      5 
      6 s = "I love Paris!"
----> 7 f()
<ipython-input-3-d7a23bc83c27> in f()
      1 def f():
----> 2    print(s)
      3    s = "I love London!"
      4    print(s)
      5 
UnboundLocalError: local variable 's' referenced before assignment
A variable can't be both local and global inside a function. So Python decides that we want a local variable due to the assignment to s inside f(), so the first print statement before the definition of s throws the error message above. Any variable which is changed or created inside a function is local, if it hasn't been declared as a global variable. To tell Python, that we want to use the global variable, we have to explicitly state this by using the keyword "global", as can be seen in the following example:

def f():
    global s
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)


s = "I am looking for a course in Paris!" 
f()
print(s)
OUTPUT:
I am looking for a course in Paris!
Only in spring, but London is great as well!
Only in spring, but London is great as well!
Local variables of functions can't be accessed from outside, when the function call has finished. Here is the continuation of the previous example:

def f():
    s = "I am globally not known"
    print(s) 

f()
print(s)
OUTPUT:
I am globally not known
Only in spring, but London is great as well!
The following example shows a wild combination of local and global variables and function parameters:

def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a, b, x, y = 1, 15, 3,4 
foo(17, 4)
print(a, b, x, y)
OUTPUT:
42 17 4 17
42 15 3 4
Global Variables in Nested Functions
We will examine now what will happen, if we use the global keyword inside nested functions. The following example shows a situation where a variable 'city' is used in various scopes:

def f():
    city = "Hamburg"
    def g():
        global city
        city = "Geneva"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
f()
print("Value of city in main: " + city)
OUTPUT:
Before calling g: Hamburg
Calling g now:
After calling g: Hamburg
Value of city in main: Geneva
We can see that the global statement inside the nested function g does not affect the variable 'city' of the 
function f, i.e. it keeps its value 'Hamburg'. We can also deduce from this example that after calling f() a 
variable 'city' exists in the module namespace and has the value 'Geneva'. This means that the global keyword 
in nested functions does not affect the namespace of their enclosing namespace! This is consistent to what 
we have found out in the previous subchapter: A variable defined inside of a function is local unless it is 
explicitly marked as global. In other words, we can refer to a variable name in any enclosing scope, but we 
can only rebind variable names in the local scope by assigning to it or in the module-global scope by using 
a global declaration. We need a way to access variables of other scopes as well. The way to do this are nonlocal 
definitions, which we will explain in the next chapter.

nonlocal Variables
Python3 introduced nonlocal variables as a new kind of variables. nonlocal variables have a lot in common 
with global variables. One difference to global variables lies in the fact that it is not possible to change 
variables from the module scope, i.e. variables which are not defined inside of a function, by using the nonlocal 
statement. We show this in the two following examples:

def f():
    global city
    print(city)
    
city = "Frankfurt"
f()
OUTPUT:
Frankfurt
This program is correct and returns 'Frankfurt' as the output. We will change "global" to "nonlocal" 
in the following program:

def f():
    nonlocal city
    print(city)
    
city = "Frankfurt"
f()
OUTPUT:
  File "<ipython-input-9-97bb311dfb80>", line 2
    nonlocal city
    ^
SyntaxError: no binding for nonlocal 'city' found
This shows that nonlocal bindings can only be used inside of nested functions. A nonlocal variable has to be defined in the enclosing function scope. If the variable is not defined in the enclosing function scope, the variable cannot be defined in the nested scope. This is another difference to the "global" semantics.

def f():
    city = "Munich"
    def g():
        nonlocal city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)
OUTPUT:
Before calling g: Munich
Calling g now:
After calling g: Zurich
'city' in main: Stuttgart
In the previous example the variable 'city' was defined prior to the call of g. We get an error if it isn't defined:

def f():
    #city = "Munich"
    def g():
        nonlocal city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)
OUTPUT:
  File "<ipython-input-11-5417be93b6a6>", line 4
    nonlocal city
    ^
SyntaxError: no binding for nonlocal 'city' found
The program works fine - with or without the line 'city = "Munich"' inside of f - , 
if we change "nonlocal" to "global":

def f():
    #city = "Munich"
    def g():
        global city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)
OUTPUT:
Before calling g: Stuttgart
Calling g now:
After calling g: Zurich
'city' in main: Zurich
Yet there is a huge difference: The value of the global x is changed now!
"""