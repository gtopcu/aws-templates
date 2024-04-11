
# https://docs.pydantic.dev/latest/concepts/models/#orm-mode-aka-arbitrary-class-instances

# pip install sqlalchemy

from sqlalchemy import create_engine, ForeignKey, Column, Integer, Float, String, CHAR, Text,  DateTime, Boolean
from sqlalchemy import select, insert, update, delete, and_, or_, not_
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# from sqlalchemy.dialects.sqlite import JSON, JSONB, BLOB, REAL, DATETIME, DATE, TIME, NUMERIC, INTEGER, SMALLINT, BIGINT, 
# BINARY, VARBINARY, BOOLEAN, FLOAT, REAL, DOUBLE_PRECISION, NUMERIC, DECIMAL, INET, MACADDR, UUID, JSON,
from sqlalchemy.dialects.postgresql import ARRAY

from pydantic import BaseModel, ConfigDict, StringConstraints
from typing_extensions import Annotated, Literal, TypedDict, NotRequired, Required

from datetime import datetime

# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")
engine = create_engine("sqlite:///data.sqlite", echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=True, autoflush=True, expire_on_commit=False)

Base = declarative_base()
Base.metadata.create_all(bind=engine) # Create all tables in the engine


"""
There are several python packages that add an ORM layer on top of Pydantic:
Pynocular - supports pgsql only
pydbantic - lightweight ORM on top of pydantic models
SQLModel - from the author of FastAPI. Uses SQLAlchemy under the hood
"""

class CompanyOrm(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))

class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    public_key: Annotated[str, StringConstraints(max_length=20)]
    name: Annotated[str, StringConstraints(max_length=63)]
    domains: list[Annotated[str, StringConstraints(max_length=255)]]

co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)
print(co_orm) # __main__.CompanyOrm object at 0x0123456789ab>
co_model = CompanyModel.model_validate(co_orm)
print(co_model)
"""
id=123 public_key='foobar' name='Testing' domains=['example.com', 'foobar.com']
"""


def get_db():
    db = SessionLocal()
    try:   
        yield db
    finally:
        db.close()

def sql_alchemy():

    # db = SessionLocal()
    # db.expire() - u1.some_attribute  # lazy loads afterwards
    # db.expire_all()
    # db.expunge()
    # db.expunge_all()

    # todo = ToDo(title="test")
    # db.add(todo)
    # db.add_all([item1, item2, item3])
    # db.update(todo)
    # db.merge(obj2)
    # db.delete(todo)
    
    # db.begin(nested=False)
    # db.commit()
    # db.flush()
    # db.rollback()
    
    # Issues a Session.expunge_all() which removes all ORM-mapped objects from the session, releases any 
    # transactional/connection resources from the Engine object(s) to which it is bound. When connections are returned 
    # to the connection pool, transactional state is rolled back as well.
    # db.close()     
    
    # db.reset(todo) # an alias to Session.close(), behaves in the same way
    # db.refresh(todo)  # emits a SQL query
    
    # todos = db.query(ToDo).all()
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

    # verbose version of what a context manager will do
    # with Session(engine) as session:
    #     session.begin()
    #     try:
    #         session.add(some_object)
    #     except:
    #         session.rollback()
    #         raise
    #     else:
    #         session.commit()

    # create session and add objects
    # with Session(engine) as session:
    #     with session.begin():
    #         session.add(some_object)
    #     # inner context calls session.commit(), if there were no exceptions
    # # outer context calls session.close()


    # u1 = db.scalars(select(User).where(User.id == 5)).one()
    # u2 = session.scalars(select(User).where(User.id == 5).execution_options(populate_existing=True)).one()

    # from sqlalchemy import update
    # session.execute(update(FooBar).values(x=5))
    # stmt = (
    #     table.update()
    #     .where(table.c.data == "value")
    #     .values(status="X")
    #     .returning(table.c.server_flag, table.c.updated_timestamp)
    # )
    # print(stmt)

    # from sqlalchemy import insert
    # stmt = (
    #     insert(user_table).
    #     values(name='username', fullname='Full Username')
    # )

    # from sqlalchemy import delete
    # stmt = (
    #     delete(user_table).
    #     where(user_table.c.id == 5)
    # )








