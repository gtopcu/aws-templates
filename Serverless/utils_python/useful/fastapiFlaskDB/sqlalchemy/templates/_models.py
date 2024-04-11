
from typing import Any, Optional
from datetime import datetime
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Integer, Float, String, CHAR, Text, DateTime, Boolean
from sqlalchemy import func, DATE, TIME, TIMESTAMP, DECIMAL, FLOAT, INTEGER, BIGINT, SMALLINT, VARCHAR, NVARCHAR, ARRAY, JSON, BINARY, CLOB, BLOB, NUMERIC, dialects
from sqlalchemy import select, update, insert, delete, and_, or_, not_, any_, all_, union, union_all, except_, between
from sqlalchemy import distinct, except_, literal_column, text, case, cast, desc, asc, null, true, false, exists, literal

from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship, backref
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.ext.declarative import declarative_base

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('sqlite:///sqlite.db', echo=True)
# SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)
# Base = declarative_base()


class Base(DeclarativeBase):
    pass
    

# import models
# models.Base.metadata.drop_all(bind=engine)
# models. Base.metadata.create_all(bind=engine)