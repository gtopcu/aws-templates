
# https://python-course.eu/python-tutorial/output-with-print.php

# The output of the print function is send to the standard output stream (sys.stdout) by default. 
# By redefining the keyword parameter "file" we can send the output into a different stream 
# e.g. sys.stderr or a file:

# We can see that we don't get any output in the interactive shell. The output is sent to the file "data.txt". 
# It's also possible to redirect the output to the standard error channel this way:

import sys
# output into sys.stderr:

print("This is not an Error: 42", file=sys.stderr)

fh = open("/Users/hukanege/Downloads/data.txt", "a") #w: write, r: read, a: append
print("42 is the answer, but what is the question?", file=fh)
fh.close()
print("Wrote to the file")