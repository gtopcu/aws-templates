
# https://docs.python.org/3/library/io.html

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