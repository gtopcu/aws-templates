
# https://sqlmodel.tiangolo.com/
# pip install sqlmodel

from typing import Annotated

# Compatible with FastAPI, Pydantic and SQLAlchemy
from sqlmodel import Field, Session, SQLModel, create_engine, select #, update, insert, delete
from decimal import Decimal

# from sqlalchemy.orm import sessionmaker #, Session
# from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from fastapi import FastAPI, Depends, BackgroundTasks, APIRouter, HTTPException, status, Request, Response

# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all(engine))
#     yield
#     # shutdown tasks
# app = FastAPI(lifespan=lifespan)

sqlite_file_name = "sqlite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# sqlite:///:memory: -> memory DB
# sqlite+aiosqlite:///sqlite.db" -> async DB

engine = create_engine(sqlite_url, echo=True)
# SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)

# engine = create_async_engine(sqlite_url, echo=True) 
# AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)


class Hero(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None, index=True, max_length=50)
    age: int | None = Field(default=0, max_length=20)
    money: Decimal = Field(default=0, max_digits=5, decimal_places=3)
"""
CREATE TABLE hero (
        id INTEGER NOT NULL, 
        name VARCHAR NOT NULL, 
        age INTEGER, 
        money NUMERIC(5, 3) NOT NULL, 
        PRIMARY KEY (id)
)
CREATE INDEX ix_hero_name ON hero (name)
"""

SQLModel.metadata.create_all(engine) # Creates tables for the models if not exists. Needs to run after model definitions

# async get_db() -> AsyncSession:
#     db = AsyncSessionLocal()
#     try:
#         yield db
#     finally
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

# async def async_depends_session(self, hero: Hero, db: Session, background_tasks: BackgroundTasks) -> Hero:
#       async with db.begin() as session:
#           session.add(Hero(name="Deadpond", secret_name="Dive Wilson"))
#           await session.commit()
#           await session.close()
#           await session.execute()
#       background_tasks.add_task(create_heroes)
#       return Hero

def create_heroes():
    hero = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", money=0.001)
    with Session(engine) as session:
        session.add(hero)
        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        # session.exec(statement).first()
        # session.exec(select(Hero)).all()
        results = session.exec(statement)
        hero = results.one()
        print("Hero mondy:", hero.money)

def all_methods():
    
    with Session(engine) as session:
        pass   
        # session.begin() # not necessary
        # session.flush() # not necessary
        # session.commit()
        # session.close()
        # session.close_all()
        # session.refresh()
        # session.reset()
        # session.prepare()
        # session.expire()
        # session.expire_all()
        # session.expunge()
        # session.expunge_all()

        # session.add(hero)
        # session.add_all([hero, hero])
        # session.delete(hero)
        # session.merge()

        # session.scalar(select(Hero).where(Hero.name == "Deadpond"))
        # session.scalars(select(Hero).where(Hero.name == "Deadpond"))

        # SELECT - https://sqlmodel.tiangolo.com/tutorial/where/
        # select(Hero)
        # select(Hero).limit(3)
        # select(Hero).offset(3)
        # select(Hero).where(Hero.name == "Deadpond").where(Hero.age == 48).order_by(Hero.name)
        # results = session.exec(statement)
        # heroes = results.all()
        # hero = results.one()

        # UPDATE - https://sqlmodel.tiangolo.com/tutorial/update/
        # hero.age = 16
        # session.add(hero)
        # session.commit()
        # session.refresh(hero)

        # DELETE - https://sqlmodel.tiangolo.com/tutorial/delete/
        # session.delete(hero)
        # session.commit()



"""
CREATE TABLE hero (id INTEGER NOT NULL, name VARCHAR NOT NULL,)
CREATE INDEX ix_hero_name ON hero (name)

SELECT name FROM hero WHERE name = 'Deadpond'
INSERT INTO hero (id, name) VALUES (1, 'Deadpond')
UPDATE hero SET name = 'Deadpond' WHERE name = 'Deadpond'

DELETE FROM hero WHERE name = 'Deadpond'

TRUNCATE TABLE hero
DROP TABLE hero
"""