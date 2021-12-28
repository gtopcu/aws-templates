
# https://python-course.eu/python-tutorial/file-management.php

"""
"Pickling" denotes the process which converts a Python object hierarchy into a byte stream, 
and "unpickling" on the other hand is the inverse operation, i.e. the byte stream is converted back into an 
object hierarchy - "serialization" or "flattening" a data structure.

An object can be dumped with the dump method of the pickle module:

pickle.dump(obj, file[,protocol, *, fix_imports=True])

dump() writes a pickled representation of obj to the open file object file. The optional protocol argument 
tells the pickler to use the given protocol:

Protocol version 0 is the original (before Python3) human-readable (ascii) protocol and is backwards compatible 
with previous versions of Python.
Protocol version 1 is the old binary format which is also compatible with previous versions of Python.
Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of new-style classes.
Protocol version 3 was introduced with Python 3.0. It has explicit support for bytes and cannot be unpickled by 
Python 2.x pickle modules. It's the recommended protocol of Python 3.x. The default protocol of Python3 is 3.

If fix_imports is True and protocol is less than 3, pickle will try to map the new Python3 names to the old 
module names used in Python2, so that the pickle data stream is readable with Python 2.

Objects which have been dumped to a file with pickle.dump can be reread into a program by using the method 
pickle.load(file). pickle.load recognizes automatically, which format had been used for writing the data. 

A simple example:
"""

import pickle
cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

# The file data.pkl can be read in again by Python in the same or another session or by a different program:

import pickle
f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)
#OUTPUT: ['Paris', 'Dijon', 'Lyon', 'Strasbourg']

"""
Only the objects and not their names are saved. That's why we use the assignment to villes in the previous example, 
i.e. data = pickle.load(f).

In our previous example, we had pickled only one object, i.e. a list of French cities. But what about pickling 
multiple objects? The solution is easy: We pack the objects into another object, so we will only have to pickle 
one object again. We will pack two lists "programming_languages" and "python_dialects" into a list pickle_objects 
in the following example:
"""

import pickle
fh = open("data.pkl","bw")
programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)
pickle.dump(pickle_object,fh)
fh.close()

# The pickled data from the previous example, - i.e. the data which we have written to the file data.pkl, 
# - can be separated into two lists again, when we reread the data:
import pickle 
f = open("data.pkl","rb") 
(languages, dialects) = pickle.load(f) 
print(languages, dialects)


"""
shelve Module
One drawback of the pickle module is that it is only capable of pickling one object at the time, 
which has to be unpickled in one go. Let's imagine this data object is a dictionary. It may be desirable 
that we don't have to save and load every time the whole dictionary, but save and load just a single value 
corresponding to just one key. The shelve module is the solution to this request. A "shelf" - as used in the 
shelve module - is a persistent, dictionary-like object. The difference with dbm databases is that the values 
(not the keys!) in a shelf can be essentially arbitrary Python objects -- anything that the "pickle" module 
can handle. This includes most class instances, recursive data types, and objects containing lots of shared 
sub-objects. The keys have to be strings.

The shelve module can be easily used. Actually, it is as easy as using a dictionary in Python. Before we can 
use a shelf object, we have to import the module. After this, we have to open a shelve object with the shelve 
method open. The open method opens a special shelf file for reading and writing:

"""

import shelve 
s = shelve.open("MyShelve")
"""
If the file "MyShelve" already exists, the open method will try to open it. If it isn't a shelf file, - i.e. 
a file which has been created with the shelve module, - we will get an error message. If the file doesn't exist, 
it will be created. We can use s like an ordinary dictionary, if we use strings as keys:
"""
s["street"] = "Fleet Str"
s["city"] = "London"
for key in s:
    print(key)

# A shelf object has to be closed with the close method:
s.close()

# We can use the previously created shelf file in another program or in an interactive Python session:

"""
$ python3
Python 3.2.3 (default, Feb 28 2014, 00:22:33) 
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.

import shelve
s = shelve.open("MyShelve")
s["street"]
'Fleet Str'
s["city"]
'London'

It is also possible to cast a shelf object into an "ordinary" dictionary with the dict function:
s
≤shelve.DbfilenameShelf object at 0xb7133dcc>
>>> dict(s)
{'city': 'London', 'street': 'Fleet Str'}
The following example uses more complex values for our shelf object:

import shelve
tele = shelve.open("MyPhoneBook")
tele["Mike"] = {"first":"Mike", "last":"Miller", "phone":"4689"}
tele["Steve"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
tele["Eve"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
tele["Eve"]["phone"]
'9069'
The data is persistent!

To demonstrate this once more, we reopen our MyPhoneBook:

$ python3
Python 3.2.3 (default, Feb 28 2014, 00:22:33) 
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
    import shelve
    tele = shelve.open("MyPhoneBook")
    tele["Steve"]["phone"]
'8745'
"""