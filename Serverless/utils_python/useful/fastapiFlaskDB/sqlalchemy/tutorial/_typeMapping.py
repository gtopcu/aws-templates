
# from typing import Any, Dict, Type
# import datetime, decimal, uuid
# from sqlalchemy import types

# # default type mapping, deriving the type for mapped_column()
# # from a Mapped[] annotation
# type_map: Dict[Type[Any], TypeEngine[Any]] = {
#     bool: types.Boolean(),
#     bytes: types.LargeBinary(),
#     datetime.date: types.Date(),
#     datetime.datetime: types.DateTime(),
#     datetime.time: types.Time(),
#     datetime.timedelta: types.Interval(),
#     decimal.Decimal: types.Numeric(),
#     float: types.Float(),
#     int: types.Integer(),
#     str: types.String(),
#     uuid.UUID: types.Uuid(),
# }

# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#customizing-the-type-map
# from sqlalchemy import BIGINT, Integer, NVARCHAR, String, TIMESTAMP
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped, mapped_column, registry
# class Base(DeclarativeBase):
#     type_annotation_map = {
#         int: BIGINT,
#         datetime.datetime: TIMESTAMP(timezone=True),
#         str: String().with_variant(NVARCHAR, "mssql"),
#     }


# class SomeClass(Base):
#     __tablename__ = "some_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     date: Mapped[datetime.datetime]
#     status: Mapped[str]


# from sqlalchemy.schema import CreateTable
# from sqlalchemy.dialects import mssql, postgresql

# print(CreateTable(SomeClass.__table__).compile(dialect=mssql.dialect()))
# CREATE TABLE some_table (
#   id BIGINT NOT NULL IDENTITY,
#   date TIMESTAMP NOT NULL,
#   status NVARCHAR(max) NOT NULL,
#   PRIMARY KEY (id)
# )

# print(CreateTable(SomeClass.__table__).compile(dialect=postgresql.dialect()))
# CREATE TABLE some_table (
#   id BIGSERIAL NOT NULL,
#   date TIMESTAMP WITH TIME ZONE NOT NULL,
#   status VARCHAR NOT NULL,
#   PRIMARY KEY (id)
# )


# from decimal import Decimal
# from typing_extensions import Annotated

# from sqlalchemy import Numeric
# from sqlalchemy import String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import registry

# str_30 = Annotated[str, 30]
# str_50 = Annotated[str, 50]
# num_12_4 = Annotated[Decimal, 12]
# num_6_2 = Annotated[Decimal, 6]

# class Base(DeclarativeBase):
#     registry = registry(
#         type_annotation_map={
#             str_30: String(30),
#             str_50: String(50),
#             num_12_4: Numeric(12, 4),
#             num_6_2: Numeric(6, 2),
#         }
#     )
# class SomeClass(Base):
#     __tablename__ = "some_table"

#     short_name: Mapped[str_30] = mapped_column(primary_key=True)
#     long_name: Mapped[str_50]
#     num_value: Mapped[num_12_4]
#     short_num_value: Mapped[num_6_2]

# from sqlalchemy.schema import CreateTable
# print(CreateTable(SomeClass.__table__))
# CREATE TABLE some_table (
#   short_name VARCHAR(30) NOT NULL,
#   long_name VARCHAR(50) NOT NULL,
#   num_value NUMERIC(12, 4) NOT NULL,
#   short_num_value NUMERIC(6, 2) NOT NULL,
#   PRIMARY KEY (short_name)
# )


# import datetime
# from typing_extensions import Annotated

# from sqlalchemy import func, String
# from sqlalchemy.orm import mapped_column

# intpk = Annotated[int, mapped_column(primary_key=True)]
# timestamp = Annotated[
#     datetime.datetime,
#     mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
# ]
# required_name = Annotated[str, mapped_column(String(30), nullable=False)]

# class Base(DeclarativeBase):
#     pass

# class SomeClass(Base):
#     __tablename__ = "some_table"
#     id: Mapped[intpk]
#     name: Mapped[required_name]
#     created_at: Mapped[timestamp]

# from sqlalchemy.schema import CreateTable
# print(CreateTable(SomeClass.__table__))
# CREATE TABLE some_table (
#   id INTEGER NOT NULL,
#   name VARCHAR(30) NOT NULL,
#   created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
#   PRIMARY KEY (id)
# )


# ENUMS
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map

# import enum
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# class Base(DeclarativeBase):
#     pass

# class Status(enum.Enum):
#     PENDING = "pending"
#     RECEIVED = "received"
#     COMPLETED = "completed"

# class SomeClass(Base):
#     __tablename__ = "some_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     status: Mapped[Status]

# CREATE TYPE status AS ENUM ('PENDING', 'RECEIVED', 'COMPLETED')
# CREATE TABLE some_table (
#   id SERIAL NOT NULL,
#   status status NOT NULL,
#   PRIMARY KEY (id)
# )

# from typing import Literal
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column

# class Base(DeclarativeBase):
#     pass

# Status = Literal["pending", "received", "completed"]

# class SomeClass(Base):
#     __tablename__ = "some_table"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     status: Mapped[Status]

# import enum
# import typing
# import sqlalchemy
# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#     type_annotation_map = {
#         enum.Enum: sqlalchemy.Enum(enum.Enum),
#         typing.Literal: sqlalchemy.Enum(enum.Enum),
#     }