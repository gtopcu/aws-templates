
# https://sqlmodel.tiangolo.com/
# pip install sqlmodel

from typing import Annotated
from decimal import Decimal

# Compatible with FastAPI, Pydantic and SQLAlchemy
from sqlmodel import Field, Relationship, Session, SQLModel, select #, update, insert, delete


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

# SQLModel.metadata.create_all(db.engine)
# SQLModel.metadata.drop_all(db.engine)