
# pip install --upgrade sqlite3

import sqlite3
# from sqlite3 import OperationalError
# from sqlite3 import version, version_info, sqlite_version, sqlite_version_info
# from sqlite3 import Connection, Cursor, Row, Error
# from sqlite3 import Blob, Date, Time, Timestamp
from typing import Any
from pathlib import Path

import time
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

FETCH_LIMIT = 10

class DatabaseError(Exception): pass
# class NotConnectedError(Exception): pass
# class InternalError(Exception): pass
class NotAuthorizedError(Exception): pass
class BadRequestError(Exception): pass
class NotFoundError(Exception): pass
# class DuplicateError(Exception): pass
# class InvalidError(Exception): pass
# class NotSupportedError(Exception): pass
# class ProgrammingError(Exception): pass
# class IntegrityError(Exception): pass
# class DataError(Exception): pass

# DB_URL = "sqlite:///" + str(Path(__file__).parent) + "/sqlite.db"
DB_NAME = "sqlite.db"
# DB_PATH = Path(__file__).parent.joinpath(DB_NAME)
# DB_PATH.touch() 
# DB_URI = DB_PATH.as_uri()
DB_URI = DB_NAME

class SQLiteContextManager:
    def __init__(self, db_url:str = DB_URI, timeout:float=60) -> None:
        print("__init__ DB: " + db_url)
        self.db_url = db_url
        self.timeout = timeout
    def __enter__(self):
        print("__enter__ DB")
        self.conn = sqlite3.connect(self.db_url, timeout=self.timeout)
        initDB(self.conn.cursor())
        self.conn.commit()
        print("DB total changes: ", self.conn.total_changes)
        return self.conn
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__ DB")
        self.conn.close()
        return False # do not suppress exceptions

# ************************************************************************************
# conn = sqlite3.connect("test.db") # test.db will be created or opened
# conn = sqlite3.connect(":memory:") # connect to a database in RAM
# cur = con.cursor()
# ************************************************************************************
# cur.execute("create table lang(name, first_appeared)")
# cur.execute("insert into lang values (?, ?)", ("C", 1972))
# for row in cur.execute("select * from lang LIMIT 10"):
#     print(row)
# ************************************************************************************

def initDB(cur: sqlite3.Cursor):
    cur.execute("CREATE TABLE IF NOT EXISTS blogs (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL, date TEXT NOT NULL)")
    cur.execute("INSERT INTO blogs (content, date) VALUES (?, ?)", ("Test content", time.strftime(DATE_FORMAT)))

# cur.execute("SELECT * FROM blogs LIMIT 10")
# result: list[Any] = cur.fetchall()

# id = 1
# cur.execute(f"SELECT * FROM blogs WHERE id='{id}'")
# result: Any = cur.fetchone() 

# ************************************************************************************

def get_blogs(id: int = 0, limit: int = FETCH_LIMIT):
    try: 
        with SQLiteContextManager() as conn:
            cur = conn.cursor()
            if id < 0:
                raise BadRequestError(f"Invalid id: {id}")
            elif id == 0:
                cur.execute(f"SELECT * FROM blogs LIMIT {limit}")
                result: list[Any] = cur.fetchall()
            else:
                cur.execute(f"SELECT * FROM blogs WHERE id='{id}' LIMIT {limit}")
                result: list[Any] = cur.fetchall()
                
            # if result is None:
            #     raise NotFoundError("No data")
            
            # print("DB total changes: ", conn.total_changes)
            # conn.rollback()
            # conn.commit()
            return result
    except sqlite3.OperationalError as e:
        raise DatabaseError(e)

# conn.rollback()
# conn.total_changes
# conn.commit()
# conn.cursor()
# conn.close()
# conn.getlimit(sqlite3.SQLITE_LIMIT_LENGTH)
# conn.blobopen()
# conn.backup()
# conn.create_function
