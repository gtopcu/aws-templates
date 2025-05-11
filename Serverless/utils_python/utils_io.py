"""
https://docs.python.org/3/library/io.html

io — Core tools for working with streams
https://github.com/python/cpython/blob/3.12/Lib/io.py

There are three main types of I/O: text I/O, binary I/O and raw I/O. A concrete object belonging to 
any of these categories is called a file object. Other common terms are stream and file-like object

Independent of its category, each concrete stream object will also have various capabilities: 
it can be read-only, write-only, or read-write. It can also allow arbitrary random access or only 
sequential access (for example in the case of a socket or pipe)

"""
import io
# from io import memoryview
# from io import FileIO, BytesIO, StringIO
# from io import RawIOBase, IOBase, BufferedIOBase, TextIOBase
# from io import BufferedRandom, BufferedReader, BufferedWriter, BufferedRWPair
# from io import TextIOWrapper, LineBuffer, IncrementalNewlineDecoder
# from io import DEFAULT_BUFFER_SIZE, SEEK_SET, SEEK_CUR, SEEK_END, UnsupportedOperation

# IOBase
# The abstract base class for all I/O classes
# f: io.IOBase = open("myfile.jpg", "rb")

# BytesIO - extends IOBase/BufferedIOBase, in-memory byte streams
# io_bytes = io.BytesIO(b"some initial binary data: \x00\x01")
# io_bytes = io.BytesIO()
# io_bytes.write(b'hello')
# io_bytes.seek(100)
# view = bytes.getbuffer()
# view[2:4] = b"56"
# io_bytes.getvalue()
# io_bytes.getbuffer()
# io_bytes.detach()
# io_bytes.flush()
# io_bytes.close()

# TextIO - extends IOBase
# io_text: io.TextIOBase = open("myfile.txt", "r", encoding="utf-8")

# StringIO - extends TextIO, in-memory text streams
# https://docs.python.org/3/library/io.html#io.StringIO
# message = "sample text"
# io_str = io.StringIO(message) # file-like String
# io_str.write('More text\n')
# data = io_str.read(10)
# pos = io_str.seek(0, io.SEEK_END) 
# value = io_str.getvalue()
# io_str.flush()
# io_str.close()

# Raw IO - extends IOBase
# Unbuffered, generally used as a low-level building-block for binary and text streams
# io_raw: io.RawIOBase = open("myfile.jpg", "rb", buffering=0)

# FileIO - subclasses RawIOBase
# io_file = io.FileIO("test.txt", "w") # r, w, a, r+, w+, a+
# io_file.writelines(["line1", "line2"])
# io_file.flush()
# io_file.close()

# BufferedIOBase - extends IOBase
# Handles buffering on a raw binary stream(RawIOBase). Its subclasses BufferedWriter, BufferedReader, 
# and BufferedRWPair buffer raw binary streams that are writable, readable, and both readable and writable respectively.
# BufferedRandom provides a buffered interface to seekable streams

# buffered_writer = io.BufferedWriter(io_writer, buffer_size=1024)
