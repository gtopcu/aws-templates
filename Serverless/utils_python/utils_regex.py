# https://www.w3schools.com/python/python_regex.asp
import re

# ^abc: Matches any string that starts with "abc". (^ : begins with)
# abc$: Matches any string that ends with "abc". ($ : ends with)
# .  : 0 or more
# +  : 1 or more
# \d : digits
# \s : whitespace

REGEX_EMAIL = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
REGEX_NUMBERS = r"\d+"
REGEX_NAME = r"^[a-zA-Z]+$"

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
x = re.split("\s", txt, 2)
print(x)
x = re.findall("ai", txt)
print(x)
x = re.sub("\s", "9", txt, 3)
print(x)

re.sub('"https?:[^ ]*"', '""', url)
email_pattern = re.compile(REGEX_EMAIL)

name_pattern = re.compile(REGEX_NAME)
if not name_pattern.match("Test input"):
    raise ValueError("Invalid name")

# pattern = re.compile(fwd, re.IGNORECASE)
# subject = pattern.sub('', subject)
# value = email.lower()
# emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', value)

"""
    The Match object has properties and methods used to retrieve information about the search, and the result:
    .span() returns a tuple containing the start-, and end positions of the match.
    .string returns the string passed into the function
    .group() returns the part of the string where there was a match
"""

x = re.search(r"\bS\w+", txt) #search for uppercase S
print(x.span())
print(x.string)
print(x.group())

# import string
# regex = re.compile("[%s]" % re.escape(string.punctuation + " " + string.digits))
# text = regex.sub("", txt)