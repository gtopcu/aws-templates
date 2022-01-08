""" 
https://www.tutorialspoint.com/python/python_multithreading.htm

The Threading Module

The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads.
The threading module exposes all the methods of the thread module and provides some additional methods: 

    - threading.active_count(): Returns the number of thread objects that are active
    - threading.currentThread(): Returns the number of thread objects in the caller's thread control
    - threading.enumerate(): Returns a list of all thread objects that are currently active

In addition to the methods, the threading module has the Thread class that implements threading. 
The methods provided by the Thread class are as follows:

    - run(): The run() method is the entry point for a thread.
    - start(): The start() method starts a thread by calling the run method.
    - join([time]): The join() waits for threads to terminate.
    - isAlive(): The isAlive() method checks whether a thread is still executing.
    - getName(): The getName() method returns the name of a thread.
    - setName(): The setName() method sets the name of a thread.

Creating Thread Using Threading Module

To implement a new thread using the threading module, you have to do the following:
    - Define a new subclass of the Thread class.
    - Override the __init__(self [,args]) method to add additional arguments.
    - Then, override the run(self [,args]) method to implement what the thread should do when started.

Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by 
invoking the start(), which in turn calls run() method.
"""

#!/usr/bin/python

exitFlag = 0

import threading
import time

class myThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Thread Starting " + self.name)
      time.sleep(3)
      print("Thread Exiting " + self.name)

# Create new threads
thread = myThread(1, "Thread-1")
thread.start()

print("Active thread count: ", threading.active_count())
print(threading.enumerate())


"""
Synchronizing Threads
The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to 
synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.

The acquire(blocking) method of the new lock object is used to force threads to run synchronously. 
The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with 
a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the lock to be released.

The release() method of the new lock object is used to release the lock when it is no longer required.
"""

#!/usr/bin/python

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting Thread: " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print(f"{threadName} {time.ctime()}")
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")


"""
Multithreaded Priority Queue

The Queue module allows you to create a new queue object that can hold a specific number of items. 
There are following methods to control the Queue:

    - get()   : removes and returns an item from the queue
    - put()   : adds item to a queue
    - qsize() : returns the number of items that are currently in the queue
    - empty() : returns True if queue is empty; otherwise, False
    - full()  : returns True if queue is full; otherwise, False
"""

#!/usr/bin/python

import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print("Starting " + self.name)
      process_data(self.name, self.q)
      print("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print(f"Processing {threadName} {data}")
      else:
         queueLock.release()
      time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print("Exiting Main Thread")
