# https://www.w3schools.com/python/python_string_formatting.asp
# https://python-course.eu/python-tutorial/formatted-output.php

import sys
print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

x = y = z = "Orange"

print(1, "b", sep=":", end="\n")
print(str(2.3*4.1))

price = 349.5123
print("%d" %(price))
print("%.2f" %(price)) 
txt = "Price is {:.2f} dollars"
print(txt.format(price))

str1 = "Hi"
str2 = "again"
print("%s %s" %(str1, str2))

hello = "helooo"
print(f"{hello}")

heloo2 = "{1} {0}"
print(heloo2.format("Gökhan", "Greetings"))

heloo2 = "helloo {}"
print(heloo2.format("Gökhan"))


"""
#print("{name:38s}: {n:5d}".format(name=novel[:-4], n=n))
#%[flags][width][.precision]type 

"""
