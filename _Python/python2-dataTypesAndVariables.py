

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


# *********************************************************************************************************
# Strings
# *********************************************************************************************************

# String literals can either be enclosed in matching single (') or in double quotes ("):
# s = 'I am a string enclosed in single quotes.'
# s2 = "I am another string, but I am enclosed in double quotes."

# Single quotes will have to be escaped with a backslash \, if the string is defined with single quotes:
# s3 = 'It doesn\'t matter!'
# This is not necessary, if the string is represented by double quotes:
# s3 = "It doesn't matter!"

# Analogously, we will have to escape a double quote inside a double quoted string:
txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
print(txt) 

# Strings can be subscripted or indexed. Similar to C, the first character of a string has the index 0.
s = "Hello World"
print(s[0])

# The last character of a string can be accessed this way:
print(s[len(s)-1])

# Yet, there is an easier way in Python. The last character can be accessed with -1, 
# the second to last with -2 and so on:
print(s[-1])
print(s[-2])


# Some operators and functions for strings
# • Concatenation
#   Strings can be glued together (concatenated) with the + operator 
#   "Hello" + "World" will result in "HelloWorld"
#
# • Repetition
#   String can be repeated or repeatedly concatenated with the asterisk operator 
#   "": "-" 3 will result in "---"
#
# • Indexing
#   "Python"[0] will result in "P"
#
# • Slicing
#   Substrings can be created with the slice or slicing notation, i.e., two indices in square brackets 
#   separated by a colon: "Python"[2:4] will result in "th"
#
# • Size
# len("Python") will result in 6


# Like strings in Java and unlike C or C++, Python strings cannot be changed - Immutable
a = "Linux"
b = "Linux"
print(a is b)


# Escape Sequences in Strings
# To end our coverage of strings in this chapter, we will introduce some escape characters and 
# sequences. The backslash () character is used to escape characters, i.e., to "escape" the special 
# meaning, which this character would otherwise have. Examples for such characters are newline, 
# backslash itself, or the quote character. 
# String literals may optionally be prefixed with a letter 'r' or 'R'; these strings are called raw strings. 
# Raw strings use different rules for interpreting backslash escape sequences.

#   Escape Sequence	        Meaning
#   \newline	            Ignored
#   \\	                    Backslash (\)
#   \'	                    Single quote (')
#   \"	                    Double quote (")
#   \a	                    ASCII Bell (BEL)
#   \b	                    ASCII Backspace(BS)
#   \f	                    ASCII Formfeed (FF)
#   \n	                    ASCII Linefeed (LF)
#   \N{name}	            Character named name in the Unicode database (Unicode only)
#   \r	                    ASCII Carriage Return (CR)
#   \t	                    ASCII Horizontal Tab (TAB)
#   \uxxxx	                Character with 16-bit hex value xxxx (Unicode only)
#   \Uxxxxxxxx	            Character with 32-bit hex value xxxxxxxx (Unicode only)
#   \v	                    ASCII Vertical Tab (VT)
#   \ooo	                Character with octal value ooo
#   \xhh	                Character with hex value hh


# Byte Strings
# Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings. 
# Every string or text in Python 3 is Unicode, but encoded Unicode is represented as binary data. 
# The type used to hold text is str, the type used to hold data is bytes. It's not possible to mix text 
# and data in Python 3; it will raise TypeError. While a string object holds a sequence of characters 
# (in Unicode), a bytes object holds a sequence of bytes, out of the range 0 to 255, 
# representing the ASCII values. Defining bytes objects and casting them into strings:
x = "Hallo"
t = str(x)
u = t.encode("UTF-8")
print(u)
# OUTPUT:
# b'Hallo'    

