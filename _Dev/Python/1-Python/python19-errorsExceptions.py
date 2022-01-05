# https://python-course.eu/python-tutorial/errors-and-exception-handling.php

# Custom exceptions
class MyException(Exception):
    pass

#raise MyException("An exception doesn't always prove the rule!")

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except Exception as e:
    print("Exception: " + str(e))
finally:
    print("Finally executed")
    
# The try ... except statement has an optional else clause. An else block has to be positioned after all 
# the except clauses. An else clause will be executed if the try clause doesn't raise an exception
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    text = fh.readlines()
    fh.close()
if text:
    print(text[100])

# The main difference is that in the first case, all statements of the try block can lead to the same 
# # error message "cannot open ...", which is wrong, if fh.close() or fh.readlines() raise an error.

