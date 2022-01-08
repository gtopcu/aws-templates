# https://www.tutorialspoint.com/python/python_multithreading.htm

# args is a tuple of arguments; use an empty tuple to call function without passing any arguments
# kwargs is an optional dictionary of keyword arguments

# thread.start_new_thread(function, args[, kwargs])

#!/usr/bin/python

"""
DEPRECATED - USE threading Module available after Python 2.4+
"""

import thread
import time

# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(time.ctime())

# Create two threads as follows
try:
   thread.start_new_thread(print_time, ("Thread-1", 2,))
   thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
   print("Error: unable to start thread")

while 1:
   pass