
# *********************************************************************************************************
# Strings
# *********************************************************************************************************
# Strings are created by putting a sequence of characters in quotes. Strings can be surrounded by 
# single quotes, double quotes or triple quotes, which are made up of three single or three double quotes. 
# Strings are immutable. In other words, once defined, they cannot be changed. 

print("Hello" + " " + "World")

x = y = z = "Orange"

a = "Hello, World!"
print(len(a))

b = "Hello, World!"
print(b[2:5])

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)

myStr = "one sentence one man "
print(myStr.strip())
print(myStr.upper())
print(myStr.capitalize())
print(myStr.title())
print(myStr.find("t"))
print(myStr.index("t"))
print(myStr.count("o"))

s = "Glückliche Fügung"
s_bytes = s.encode('utf-8') 
print(s_bytes)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

myName = "name"
formatted = f"my name is {myName}"

#reverse a string
txt = "Hello World"[::-1]
print(txt)

def my_function(x):
  return x[::-1]


"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""


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

# A string in triple quotes can span several lines without using the escape character:
# city = """
# ... Toronto is the largest city in Canada 
# ... and the provincial capital of Ontario. 
# ... It is located in Southern Ontario on the 
# ... northwestern shore of Lake Ontario.
# ... """
# print(city)

# Multiplication on strings is defined, which is essentially a multiple concatenation:
# ".-." * 4
# OUTPUT:
# '.-..-..-..-.'