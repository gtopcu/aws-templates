
# https://python-course.eu/python-tutorial/file-management.php

# The output of the print function is send to the standard output stream (sys.stdout) by default. 
# By redefining the keyword parameter "file" we can send the output into a different stream 
# e.g. sys.stderr or a file:

# We can see that we don't get any output in the interactive shell. The output is sent to the file "data.txt". 
# It's also possible to redirect the output to the standard error channel this way:

# output into sys.stderr & sys.stdout:

import sys
print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

from typing import IO, TextIO, BinaryIO, ByteString, Iterable
from io import FileIO, TextIOWrapper, StringIO, BytesIO, DEFAULT_BUFFER_SIZE
from io import BufferedRandom, BufferedReader, BufferedWriter

import os
os.system("clear") # Linux - OSX
#os.system("cls") # Windows

# fh.tell()
# fh.seek(offset, startpoint_for_offset)

# Read the whole file including the carriage returns and line feeds
fh = open("filename.txt").read().lower()
fh.close()

# Read line by line - no need for closing, auto-closes even if exception occurs
with open("filename.txt", "r") as fh:
    for line in fh:
        print(line.strip())

# Proper try-else-catch-finally
text = []
try:
    fh = open("filename.txt", 'r')
except IOError:
    print("Cannot open file")
else:
    text = fh.readlines()
    fh.close()
if text:
    print(text[100])

# Text file
try: 
    fh = open(  
                "/Users/hukanege/Downloads/textData.txt", 
                "wt", #r(t/b):read(default), w(t/b):truncate&write, a(t/b):append, x(t/b):create
                buffering=1,
                encoding="UTF-8",
                #newline="\n"
            ) 
    print("42 is the answer, but what is the question?", file=fh, end=None)
    fh.write("more data1")
    fh.write("more data2")
    #print(fh.read())
    #print(fh.readline(10))
    fh.flush()
except FileExistsError: 
    print("File already exists")
except FileNotFoundError:
    print("File not found")
except OSError:
    print("OS error")
finally:
    fh.close()
    print("Closed text file")


# Binary file
# locale.getpreferredencoding(False)
print("Default buffer size:", DEFAULT_BUFFER_SIZE)
try:
    fhb = open(
                "/Users/hukanege/Downloads/encoded.data", 
                "wb", #w+b:opens and truncates the file to 0 bytes,
                buffering=8192
            )    
    fhb.write("Encoded".encode("utf-8"))
    fh.flush()
except FileExistsError: 
    print("File already exists")
except FileNotFoundError:
    print("File not found")
except OSError:
    print("OS Error")
finally:
    fhb.close()
    print("Closed binary file")


# Read and Write to the Same File
# In the following example we will open a file for reading and writing at the same time. 
# If the file doesn't exist, it will be created. If you want to open an existing file for read and write, 
# you should better use "r+", because this will not delete the content of the file.

fh = open('colours.txt', 'w+')
fh.write('The colour brown')
#Go to the 12th byte in the file, counting starts with 0
fh.seek(11)   
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)


"""
(file: _OpenFile, mode: OpenTextMode = ..., buffering: int = ..., encoding: str | 
None = ..., errors: str | None = ..., newline: str | None = ..., closefd: bool = ..., opener: _Opener | None = ...) 
-> TextIOWrapper

Open file and return a stream. Raise OSError upon failure.

file is either a text or byte string giving the name (and the path if the file isn't in the current working directory) 
of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, 
it is closed when the returned I/O object is closed, unless closefd is set to False.)

mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means 
open for reading in text mode. Other common values are 'w' for writing (truncating the file if it already exists), 
'x' for creating and writing to a new file, and 'a' for appending (which on some Unix systems, means that all writes 
append to the end of the file regardless of the current seek position). In text mode, if encoding is not specified 
the encoding used is platform dependent: locale.getpreferredencoding(False) is called to get the current locale 
encoding. (For reading and writing raw bytes use binary mode and leave encoding unspecified.) 

The available modes are:

Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newline mode (deprecated)

The default mode is 'rt' (open for reading text). 
For binary random access, the mode 'w+b' opens and truncates the file to 0 bytes, 
while 'r+b' opens the file without truncation. 

The 'x' mode implies 'w' and raises an FileExistsError if the file already exists.

Python distinguishes between files opened in binary and text modes, even when the underlying operating system doesn't. 
Files opened in binary mode (appending 'b' to the mode argument) return contents as bytes objects without any decoding. 
In text mode (the default, or when 't' is appended to the mode argument), the contents of the file are returned as 
strings, the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.

'U' mode is deprecated and will raise an exception in future versions of Python. It has no effect in Python 3. 

Use newline to control universal newlines mode.

buffering is an optional integer used to set the buffering policy. 
Pass 0 to switch buffering off (only allowed in binary mode), 
1 to select line buffering (only usable in text mode), 
and an integer > 1 to indicate the size of a fixed-size chunk buffer. 

When no buffering argument is given, the default buffering policy works as follows:
Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine 
the underlying device's "block size" and falling back on io.DEFAULT_BUFFER_SIZE. On many systems, the buffer will 
typically be 4096 or 8192 bytes long.

"Interactive" text files (files for which isatty() returns True) use line buffering. Other text files use the policy 
described above for binary files.

encoding is the name of the encoding used to decode or encode the file. This should only be used in text mode. 
The default encoding is platform dependent, but any encoding supported by Python can be passed. 
See the codecs module for the list of supported encodings.

errors is an optional string that specifies how encoding errors are to be handled---this argument should not be used 
in binary mode. Pass 'strict' to raise a ValueError exception if there is an encoding error 
(the default of None has the same effect), or pass 'ignore' to ignore errors. 
(Note that ignoring encoding errors can lead to data loss.) See the documentation for codecs.register or 
run 'help(codecs.Codec)' for a list of the permitted encoding error strings.

newline controls how universal newlines works (it only applies to text mode). 
It can be None, '', '\n', '\r', and '\r\n'. It works as follows:

On input, if newline is None, universal newlines mode is enabled. 
Lines in the input can end in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned 
to the caller. If it is '', universal newline mode is enabled, but line endings are returned to the caller untranslated. 
If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is 
returned to the caller untranslated.

On output, if newline is None, any '\n' characters written are translated to the system default line separator, 
os.linesep. If newline is '' or '\n', no translation takes place. If newline is any of the other legal values, 
any '\n' characters written are translated to the given string.

If closefd is False, the underlying file descriptor will be kept open when the file is closed. This does not work 
when a file name is given and must be True in that case.

A custom opener can be used by passing a callable as *opener*. The underlying file descriptor for the file object 
is then obtained by calling *opener* with (*file*, *flags*). *opener* must return an open file descriptor 
(passing os.open as *opener* results in functionality similar to passing None).

open() returns a file object whose type depends on the mode, and through which the standard file operations such 
as reading and writing are performed. When open() is used to open a file in a text mode ('w', 'r', 'wt', 'rt', etc.), 
it returns a TextIOWrapper. When used to open a file in a binary mode, the returned class varies: 
in read binary mode, it returns a BufferedReader; 
in write binary and append binary modes, it returns a BufferedWriter, 
and in read/write mode, it returns a BufferedRandom.

It is also possible to use a string or bytearray as a file for both reading and writing. 
For strings StringIO can be used like a file opened in a text mode, 
and for bytes a BytesIO can be used like a file opened in a binary mode.


Resetting the Files Current Position
It's possible to set - or reset - a file's position to a certain position, also called the offset. To do this, we use the method seek. The parameter of seek determines the offset which we want to set the current position to. To work with seek, we will often need the method tell which "tells" us the current position. When we have just opened a file, it will be zero. Before we demonstrate the way of working of both seek and tell, we create a simple file on which we will perform our commands:

open("small_text.txt", "w").write("brown is her favorite colour")
;
OUTPUT:
''
The method tell returns the current stream position, i.e. the position where we will continue, when we use a "read", "readline" or so on:

fh = open("small_text.txt")
fh.tell()
OUTPUT:
0
Zero tells us that we are positioned at the first character of the file.

We will read now the next five characters of the file:

fh.read(5)
OUTPUT:
'brown'
Using tellagain, shows that we are located at position 5:

fh.tell()
OUTPUT:
5
Using read without parameters will read the remainder of the file starting from this position:

fh.read()
OUTPUT:
' is her favorite colour'
Using tellagain, tells us about the position after the last character of the file. This number corresponds to the number of characters of the file!

fh.tell()
OUTPUT:
28
With seekwe can move the position to an arbitrary place in the file. The method seek takes two parameters:

fh.seek(offset, startpoint_for_offset)

where fh is the file pointer, we are working with. The parameter offset specifies how many positions the pointer will be moved. The question is from which position should the pointer be moved. This position is specified by the second parameter startpoint_for_offset. It can have the follwoing values:

0: reference point is the beginning of the file
1: reference point is the current file position
2: reference point is the end of the file
if the startpoint_for_offset parameter is not given, it defaults to 0.

WARNING: The values 1 and 2 for the second parameter work only, if the file has been opened for binary reading. We will cover this later!

The following examples, use the default behaviour:

fh.seek(13)
print(fh.tell())   # just to show you, what seek did!
fh.read()          # reading the remainder of the file
OUTPUT:
13
'favorite colour'
It is also possible to move the position relative to the current position. If we want to move k characters to the right, we can just set the argument of seek to fh.tell() + k

k = 6
fh.seek(5)    # setting the position to 5
fh.seek(fh.tell() + k)   #  moving k positions to the right
print("We are now at position: ", fh.tell())
OUTPUT:
We are now at position:  11
seek doesn't like negative arguments for the position. On the other hand it doesn't matter, if the value for the position is larger than the length of the file. We define a function in the following, which will set the position to zero, if a negative value is applied. As there is no efficient way to check the length of a file and because it doesn't matter, if the position is greater than the length of the file, we will keep possible values greater than the length of a file.

def relative_seek(fp, k):
    rel_seek moves the position of the file pointer k characters to
    the left (k<0) or right (k>0) 
    
    position = fp.tell() + k
    if position < 0:
        position = 0
    fh.seek(position)
    

with open("small_text.txt") as fh:
    print(fh.tell())
    relative_seek(fh, 7)
    print(fh.tell())
    relative_seek(fh, -5)
    print(fh.tell())
    relative_seek(fh, -10)
    print(fh.tell())
OUTPUT:
0
7
2
0
You might have thought, when we wrote the function relative_seek why do we not use the second parameter of seek. After all the help file says "1 -- current stream position;". What the help file doesn't say is the fact that seek needs a file pointer opened with "br" (binary read), if the second parameter is set to 1 or 2. We show this in the next subchapter.

Binary read
So far we have only used the first parameter of open, i.e. the filename. The second parameter is optional and is set to "r" (read) by default. "r" means that the file is read in text mode. In text mode, if encoding (another parameter of open) is not specified the encoding used is platform dependent: locale.getpreferredencoding(False) is called to get the current locale encoding.

The second parameter specifies the mode of access to the file or in other words the mode in which the file is opened. Files opened in binary mode (appending 'b' to the mode argument) return contents as bytes objects without any decoding.

We will demonstrate this in the following example. To demonstrate the different effects we need a string which uses characters which are not included in standard ASCII. This is why we use a Turkish text, because it uses many special characters and Umlaute. the English translation means "See you, I'll come tomorrow.".

We will write a file with the Turkish text "Görüşürüz, yarın geleceğim.":

txt = "Görüşürüz, yarın geleceğim." 
number_of_chars_written = open("see_you_tomorrow.txt", "w").write(txt)
We will read in this files in text mode and binary mode to demonstrate the differences:

text = open("see_you_tomorrow.txt", "r").read()
print("text mode: ", text)
text_binary = open("see_you_tomorrow.txt", "rb").read()
print("binary mode: ", text_binary)
OUTPUT:
text mode:  Görüşürüz, yarın geleceğim.
binary mode:  b'G\xc3\xb6r\xc3\xbc\xc5\x9f\xc3\xbcr\xc3\xbcz, yar\xc4\xb1n gelece\xc4\x9fim.'
In binary mode, the characters which are not plain ASCII like "ö", "ü", "ş", "ğ" and "ı" are represented by more than one byte. In our case by two characters. 14 bytes are needed for "görüşürüz":

text_binary[:14]
OUTPUT:
b'G\xc3\xb6r\xc3\xbc\xc5\x9f\xc3\xbcr\xc3\xbcz'
"ö" for example consists of the two bytes "\xc3" and "\xb6".

text[:9]
OUTPUT:
'Görüşürüz'
There are two ways to turn a byte string into a string again:

t = text_binary.decode("utf-8")
print(t)
t2 = str(text_binary, "utf-8")
print(t2)
OUTPUT:
Görüşürüz, yarın geleceğim.
Görüşürüz, yarın geleceğim.
It is possible to use the values "1" and "2" for the second parameter of seek, if we open a file in binary format:

with open("see_you_tomorrow.txt", "rb") as fh:
    x = fh.read(14)
    print(x)
    # move 5 bytes to the right from the current position:
    fh.seek(5, 1)
    x = fh.read(3)
    print(x)
    print(str(x, "utf-8"))
    # let's move to the 8th byte from the right side of the byte string:
    fh.seek(-8, 2)
    x = fh.read(5)
    print(x)
    print(str(x, "utf-8"))
OUTPUT:
b'G\xc3\xb6r\xc3\xbc\xc5\x9f\xc3\xbcr\xc3\xbcz'
b'\xc4\xb1n'
ın
b'ece\xc4\x9f'
eceğ
Read and Write to the Same File
In the following example we will open a file for reading and writing at the same time. If the file doesn't exist, it will be created. If you want to open an existing file for read and write, you should better use "r+", because this will not delete the content of the file.

fh = open('colours.txt', 'w+')
fh.write('The colour brown')

#Go to the 12th byte in the file, counting starts with 0
fh.seek(11)   
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)
OUTPUT:
brown
16
The colour green
"How to get into a Pickle"
Pickle 

We don't really mean what the header says. On the contrary, we want to prevent any nasty situation, like losing the data, which your Python program has calculated. So, we will show you, how you can save your data in an easy way that you or better your program can reread them at a later date again. We are "pickling" the data, so that nothing gets lost.

Python offers a module for this purpose, which is called "pickle". With the algorithms of the pickle module we can serialize and de-serialize Python object structures. "Pickling" denotes the process which converts a Python object hierarchy into a byte stream, and "unpickling" on the other hand is the inverse operation, i.e. the byte stream is converted back into an object hierarchy. What we call pickling (and unpickling) is also known as "serialization" or "flattening" a data structure.

An object can be dumped with the dump method of the pickle module:

 pickle.dump(obj, file[,protocol, *, fix_imports=True])
dump() writes a pickled representation of obj to the open file object file. The optional protocol argument tells the pickler to use the given protocol:

Protocol version 0 is the original (before Python3) human-readable (ascii) protocol and is backwards compatible with previous versions of Python.
Protocol version 1 is the old binary format which is also compatible with previous versions of Python.
Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of new-style classes.
Protocol version 3 was introduced with Python 3.0. It has explicit support for bytes and cannot be unpickled by Python 2.x pickle modules. It's the recommended protocol of Python 3.x.
The default protocol of Python3 is 3.

If fix_imports is True and protocol is less than 3, pickle will try to map the new Python3 names to the old module names used in Python2, so that the pickle data stream is readable with Python 2.

Objects which have been dumped to a file with pickle.dump can be reread into a program by using the method pickle.load(file). pickle.load recognizes automatically, which format had been used for writing the data. A simple example:

import pickle
cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()
The file data.pkl can be read in again by Python in the same or another session or by a different program:

import pickle
f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)
['Paris', 'Dijon', 'Lyon', 'Strasbourg']
Only the objects and not their names are saved. That's why we use the assignment to villes in the previous example, i.e. data = pickle.load(f).

In our previous example, we had pickled only one object, i.e. a list of French cities. But what about pickling multiple objects? The solution is easy: We pack the objects into another object, so we will only have to pickle one object again. We will pack two lists "programming_languages" and "python_dialects" into a list pickle_objects in the following example:

import pickle
fh = open("data.pkl","bw")
programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)
pickle.dump(pickle_object,fh)
fh.close()
The pickled data from the previous example, - i.e. the data which we have written to the file data.pkl, - can be separated into two lists again, when we reread the data:

</pre> import pickle f = open("data.pkl","rb") languages, dialects) = pickle.load(f) print(languages, dialects) ['Python', 'Perl', 'C++', 'Java', 'Lisp'] ['Jython', 'IronPython', 'CPython'] </pre>

shelve Module
One drawback of the pickle module is that it is only capable of pickling one object at the time, which has to be unpickled in one go. Let's imagine this data object is a dictionary. It may be desirable that we don't have to save and load every time the whole dictionary, but save and load just a single value corresponding to just one key. The shelve module is the solution to this request. A "shelf" - as used in the shelve module - is a persistent, dictionary-like object. The difference with dbm databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects -- anything that the "pickle" module can handle. This includes most class instances, recursive data types, and objects containing lots of shared sub-objects. The keys have to be strings.

The shelve module can be easily used. Actually, it is as easy as using a dictionary in Python. Before we can use a shelf object, we have to import the module. After this, we have to open a shelve object with the shelve method open. The open method opens a special shelf file for reading and writing:

</pre> import shelve s = shelve.open("MyShelve")</pre>

If the file "MyShelve" already exists, the open method will try to open it. If it isn't a shelf file, - i.e. a file which has been created with the shelve module, - we will get an error message. If the file doesn't exist, it will be created.

We can use s like an ordinary dictionary, if we use strings as keys:

s["street"] = "Fleet Str"
s["city"] = "London"
for key in s:
    print(key)
A shelf object has to be closed with the close method:

 s.close()
We can use the previously created shelf file in another program or in an interactive Python session:

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