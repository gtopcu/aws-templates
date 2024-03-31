
"""
https://docs.python.org/3/library/io.html

There are three main types of I/O: text I/O, binary I/O and raw I/O. A concrete object belonging to 
any of these categories is called a file object. Other common terms are stream and file-like object.

Independent of its category, each concrete stream object will also have various capabilities: 
it can be read-only, write-only, or read-write. It can also allow arbitrary random access  or only 
sequential access (for example in the case of a socket or pipe).

"""


import io
# from io import memoryview
# from io import FileIO, BytesIO, StringIO
# from io import RawIOBase, IOBase, BufferedIOBase, TextIOBase
# from io import BufferedRandom, BufferedReader, BufferedWriter, BufferedRWPair
# from io import TextIOWrapper, LineBuffer, IncrementalNewlineDecoder
# from io import DEFAULT_BUFFER_SIZE, SEEK_SET, SEEK_CUR, SEEK_END, UnsupportedOperation

io_writer = io.BytesIO()
# io_writer.write(b'hello')
# io_writer.seek(100)
# obj: bytes = io_writer.getvalue()
# view: memoryview = io_writer.getbuffer()
# raw: RawIOBase = io_writer.detach()
# io_writer.flush()
# io_writer.close()

buffered_writer = io.BufferedWriter(io_writer, buffer_size=1024)