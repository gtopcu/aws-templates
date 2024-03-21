# https://www.youtube.com/watch?v=3vfum74ggHE

# pip install fastapi
# pip install "uvicorn[standard]"
# pip install python-multipart sqlalchemy jinja2

# python3 -m venv venv
# source venv/bin/activate

# uvicorn fastapiSQLAlchemy:app --reload
# http://127.0.0.1:8000/docs

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


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, Text #, func, sum, min, max, or_, not_
# from sqlalchemy.sql.expression import select, update, union, alias, delete, bindparam, outerjoin
# from sqlalchemy.sql.functions import concat, count, current_date, current_timestamp, current_time, sysdate
# from sqlalchemy.sql.schema import Column, ForeignKey, Index, Table, UniqueConstraint

DB_URL = "sqlite:///./db.sqlite"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True, unique=True)
    working = Column(Boolean, default=False)
    updated = Column(DateTime)

Base.metadata.create_all(bind=engine)


app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

def get_db():
    db = SessionLocal()
    try:   
        yield db
    finally:
        db.close()

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
    # deleted_count = db.query(ToDo).delete(synchronize_session='evaluate') # auto

    # db.begin(nested=False)
    # db.commit() -> flush + commit
    # db.flush()
    # db.rollback()
    
    return {"todos": todos}

@app.post("/item")
async def post(request: Request, title:str = Form(...), db: Session = Depends(get_db)):
    todo = ToDo(title=title)
    db.add(todo)
    db.commit()

    url = request.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.put("/item/{todo_id}")
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.working = not todo.working
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

