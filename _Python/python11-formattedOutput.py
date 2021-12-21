
# https://python-course.eu/python-tutorial/formatted-output.php

print("Hello World")
print(1, "b", sep=":", end="\n")
print(str(2.3*4.1))

# output into sys.stderr & sys.stdout:
import sys
print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

#Formatted output
print("%d" %(42.565512))
print("%2.2f" %(42.565512)) 
print("{name:38s}: {n:5d}".format(name=novel[:-4], n=n))

#%[flags][width][.precision]type 

