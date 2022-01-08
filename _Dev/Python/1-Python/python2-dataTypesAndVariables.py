

# *********************************************************************************************************
# Variable Names
# *********************************************************************************************************
# A variable name and an identifier can consist of the uppercase letters "A" through "Z", 
# the lowercase letters "a" through "z", the underscore _ 
# and, except for the first character, the digits 0 through 9. 
# Python 3.x is based on Unicode. That is, variable names and identifier names can additionally 
# contain Unicode characters as well.

# The type of a variable can change during the execution of a script. Or, to be precise, 
# a new object, which can be of any type, will be assigned to it. 
i = 42          # data type is implicitly set to integer
i = 42 + 0.11   # data type is changed to float
i = "forty"     # and now it will be a string 

x = 20.5
print(type(x))

# *********************************************************************************************************
# Object References
# *********************************************************************************************************
# Python variables are references to objects, but the actual data is contained in the objects
# Every instance (object or variable) has an identity, i.e., an integer which is unique within 
# the script or program, i.e., other objects have different identities. 
x = 42
y = x
print(id(x))
print(id(y))
y = 43
print(id(x))
print(id(y))


# *********************************************************************************************************
# Python Keywords
# *********************************************************************************************************
# No identifier can have the same name as one of the Python keywords, although they are obeying 
# the above naming conventions. You can get the list of Python keywords in the interactive shell 
# by using help() in the interactive shell:

# and, as, assert, break, class, continue, def, del, elif, else,
# except, False, finally, for, from, global, if, import, in, is, 
# lambda, None, nonlocal, not, or, pass, raise, return, True, try, 
# while, with, yield 


# *********************************************************************************************************
# Numbers
# *********************************************************************************************************

# • Integer
#    ∙  Normal integers: 4321. Integers in Python3 can be of unlimited size
#    ∙  Octal literals(base 8): a = 0o10
#    ∙  Hexadecimal literals(base 16): a = 0xA0F 
#    ∙  Binary literals(base 2) Prefixed by a leading "0", followed by a "b" or "B": x = 0b101010
# 
# The functions hex, bin, oct can be used to convert an integer number into the corresponding string 
# representation of the integer number:
x = hex(19)
print(x)

#   • Floating-point numbers: 42.11, 3.1415e-10
#   • Complex numbers written as <real part> + <imaginary part>: x = 3 + 4j


# Integer Division
# • "true division" performed by "/"
# • "floor division" performed by "//" 

# True Division
# True division uses the slash (/) character as the operator sign
print(10 / 3)
#OUTPUT: 3.3333333333333335

# Floor Division
# The operator "//" performs floor division, i.e., the dividend is divided by the divisor - like in true 
# division - but the floor of the result will be returned. The floor is the largest integer number smaller 
# than the result of the true division. This number will be turned into a float, if either the dividend 
# or the divisor or both are float values. If both are integers, the result will be an integer as well. 
print(9 // 3)
#OUTPUT: 3
print(10 // 3)
#OUTPUT: 3
print(10.0 // 3)
#OUTPUT: 3.0
print(-7 // 3)
#OUTPUT: -3

