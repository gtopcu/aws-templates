
# https://www.youtube.com/watch?v=3vfum74ggHE
# https://www.youtube.com/watch?v=AKQ3XEDI9Mw

# pip install fastapi
# pip install "uvicorn[standard]"
# pip install python-multipart sqlalchemy jinja2

# python3 -m venv venv
# source venv/bin/activate

# uvicorn fastapiSQLAlchemy:app --reload
# http://127.0.0.1:8000/docs

from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Depends, Request, Form, File, status
# from fastapi import File, UploadFile, Body, Path, Query, Cookie, Header
# from fastapi.responses import Response, HTMLResponse, JSONResponse
# FileResponse, PlainTextResponse, RedirectResponse,  StreamingResponse
# from fastjsonschema import validate, exceptions

# FastAPI is built on starlette ASGI FW
from starlette.responses import RedirectResponse, HTMLResponse, JSONResponse, PlainTextResponse, Response
# from starlette.templating import Jinja2Templates
# from starlette.staticfiles import StaticFiles
# templates = Jinja2Templates(directory="templates")


from sqlalchemy import create_engine, ForeignKey, Column, Integer, Float, String, CHAR, Text, DateTime, Boolean
# from sqlalchemy import func, sum, min, max, or_, not_
from sqlalchemy.orm import sessionmaker, Session, declarative_base, Mapped, mapped_column
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import relationship, backref, joinedload, subqueryload, selectinload, lazyload
# from sqlalchemy.sql.expression import select, update, union, alias, delete, bindparam, outerjoin
# from sqlalchemy.sql.functions import concat, count, current_date, current_timestamp, current_time, sysdate
# from sqlalchemy.sql.schema import Column, ForeignKey, Index, Table, UniqueConstraint

DB_URL = "sqlite:///sqlite.db"
engine = create_engine(DB_URL, echo=True) # connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)
Base = declarative_base()

class ToDo(Base):
    """
    CREATE TABLE todo (
        _id_ INTEGER NOT NULL, 
        title VARCHAR NOT NULL, 
        working BOOLEAN, 
        updated DATETIME, 
        PRIMARY KEY (_id_)
    )
    CREATE UNIQUE INDEX ix_todo_title ON todo (title)
    SELECT * FROM todo LIMIT 100
    """
    __tablename__ = "todos"
    id = Column("_id_", Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), index=True, unique=True, nullable=False)
    working = Column(Boolean, default=False)
    updated = Column(DateTime)

    def __init__(self, title: str, working: bool = False):
        self.title = title
        self.working = working
        self.updated = datetime.now() # default=sa.func.now()
    def  __repr__(self):
        return f"<ToDo {self.title}>"

class ToDoNotes(Base):
    """
    CREATE TABLE notes (
        _id_ INTEGER NOT NULL, 
        todo_id INTEGER NOT NULL, 
        note VARCHAR NOT NULL, 
        PRIMARY KEY (_id_), 
        FOREIGN KEY(todo_id) REFERENCES todos (_id_)
    )
    INSERT INTO "notes"("_id_", "todo_id", "note") VALUES(1, 1, 'note');
    """
    __tablename__ = "notes"
    id = Column("_id_", Integer, primary_key=True, autoincrement=True)
    todo_id = Column(Integer, ForeignKey("todos._id_"), nullable=False)
    note = Column(String, nullable=False)

    def __init__(self, todo_id: int, note: str):
        self.todo_id = todo_id
        self.note = note


# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:   
        yield db
    finally:
        db.close()

# async def get_db() -> AsyncSession:
#     db = AsyncSessionLocal()
#     try:
#         yield db
#     finally
#         db.close()

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    
    # request.base_url
    # request.path_params
    # request.method
    # request.headers
    # request.auth
    # request.query_params
    
    todos = db.query(ToDo).all()
    # db.query(ToDo).filter(ToDo.name == "G").count(10)
    # results = db.query(ToDo).filter(ToDo.id > 3).filter(ToDo.title.like("%An%"))
    # results = db.query(ToDo).filter(ToDo.title.in_(["gt1", "gt2"]))
    # for item in results:
    #     print(item)
    # deleted_count = db.query(ToDo).delete(synchronize_session='evaluate') # auto

    # List[Row[Tuple[ToDo, ToDoNotes]]] 
    # results = db.query(ToDo, ToDoNotes).filter(ToDo.id == ToDoNotes.todo_id).filter(ToDo.name == "G").all()
    # for result in results:
    #     print(result)

    # db.begin(nested=False)
    # db.commit() -> flush + commit
    # db.flush()
    # db.rollback()
    
    return {"todos": todos}

@app.post("/item", status_code=status.HTTP_201_CREATED)
async def post(request: Request, title:str = Form(...), db: Session = Depends(get_db)):
    todo = ToDo(title=title)
    db.add(todo)
    db.commit()

    url = request.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_201_CREATED)

@app.put("/item/{todo_id}")
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.working = not todo.working
    todo.updated = datetime.now()
    db.commit()

    url = request.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.delete("/item/{todo_id}")
async def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = request.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

# def main():
#     import uvicorn