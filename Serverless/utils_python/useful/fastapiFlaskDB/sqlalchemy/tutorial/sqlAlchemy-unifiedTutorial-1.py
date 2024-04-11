
# https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial
# https://alembic.sqlalchemy.org/en/latest/

from sqlalchemy import __version__

from sqlalchemy import create_engine
from sqlalchemy import text, Result
from sqlalchemy.orm import Session, declarative_base, DeclarativeBase
from sqlalchemy import MetaData, Table, Column, ForeignKey, Integer, String
from sqlalchemy import select, insert, update, delete, func, desc, asc, or_, and_

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata = MetaData()

class Base(DeclarativeBase):
    pass

# Base = declarative_base()
# Base.metadata.create_all(engine)
# Base.registry

if __name__ == "__main__":
    print(__version__) #2.0.29
    # print(metadata)

    # SELECT name, age FROM users
    # INSERT INTO users (name, age) VALUES (:name, :age)
    # UPDATE users SET age = :age WHERE name = :name
    # DELETE FROM users WHERE name = :name

    # with engine.connect() as conn: # tx not auto-committed. use conn only inside with block

        # conn.begin()
        # conn.commit()
        # conn.rollback
        # conn.close()
        
        # result = conn.execute(text("select 'hello world'"))
        # if row := result.first():
        #     print(row)
        # print(result.all())

        # t = text("SELECT * FROM users")
        # conn.execute(text("INSERT INTO users (name, fullname) VALUES (:name, :fullname)"),)
        # result = conn.execute(t)
        
    # with engine.connect() as conn:
    #     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    #     conn.execute(
    #         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
    #         [{"x": 1, "y": 1}, {"x": 2, "y": 2}],
    #     )
    #     conn.commit()
    #     result = conn.execute(text("SELECT * FROM some_table"))
    #     print(result.all())

    # https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#fetching-rows
    # with engine.begin() as conn: # starts tx, commits/rollbacks at the end
    #     conn.execute(
    #         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
    #         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    #     )
    #     result = conn.execute(text("SELECT x, y FROM some_table"))
    #     for row in result:
        #         print(row)
        # for row in result:
        #     print(f"x: {row.x}  y: {row.y}")
        # for x, y in result:
        #     print(x, y)
        # for row in result:
        #     print(row[0], row[1]) # x,y
        # for dict_row in result.mappings():
        #     print(dict_row["x"], dict_row["y"])
    
    
    # SESSION XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX# 

    # with Session(engine) as session:
    #     stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
    #     result = session.execute(stmt, {"y": 1})
    #     for row in result:
    #         print(f"x: {row.x}  y: {row.y}")
        
    # with Session(engine) as session:
    #     stmt = text("UPDATE some_table SET y=:y WHERE x=:x")
    #     result = session.execute(stmt, [{"x": 1, "y": 11}, {"x": 2, "y": 22}])
    #     session.commit()

    #     stmt = text("SELECT x, y FROM some_table")
    #     result = session.execute(stmt)
    #     for x, y in result:
    #         print(x, y)
        # print(result.first())
        # print(result.all())
        
        # session.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 3, "y": 33}])
        # session.execute(text("DELETE FROM some_table WHERE x=:x"), [{"x": 1}])
    

    # Table XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # user_table = Table(
    #     "users",
    #     metadata,
    #     Column("id", Integer, primary_key=True),
    #     Column("name", String(30), index=True),
    #     Column("fullname", String),
    # )
    # address_table = Table(
    #     "addresses",
    #     metadata,
    #     Column("id", Integer, primary_key=True),
    #     Column("user_id", ForeignKey("users.id"), nullable=False),
    #     Column("email_address", String, nullable=False),
    # )
    # metadata.create_all(engine)

    # print(user_table.primary_key)
    # print(user_table.indexes)
    # print(user_table.c.keys())
    # print(user_table.c.name)
    
    # Loading existing data:
    # some_table = Table("some_table", metadata, autoload_with=engine)


    # INSERT XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html
    # from sqlalchemy import insert
    
    # stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
    # print(stmt)
    # compiled = stmt.compile()
    # compiled.params

    # with engine.connect() as conn:
    #     result = conn.execute(stmt)
    #     conn.commit()
    #     result.inserted_primary_key # (1,) ->  CursorResult.inserted_primary_key

    #     user_table.insert().values(id=1, name="john", fullname="John Doe")
    #     result = user_table.select().where(user_table.c.id == 1)

    # All columns: insert(user_table)
    # INSERT INTO user_account (id, name, fullname) VALUES (:id, :name, :fullname)

    # with engine.connect() as conn:
    #     result = conn.execute(
    #         insert(user_table),
    #         [
    #             {"name": "sandy", "fullname": "Sandy Cheeks"},
    #             {"name": "patrick", "fullname": "Patrick Star"},
    #         ],
    #     )
    #     conn.commit()
    #     INSERT INTO user_account (name, fullname) VALUES (?, ?)
    #     [...] [('sandy', 'Sandy Cheeks'), ('patrick', 'Patrick Star')]

    #     session.execute(
    #         insert(User),
    #         [
    #             {"name": "spongebob", "fullname": "Spongebob Squarepants"},
    #             {"name": "sandy", "fullname": "Sandy Cheeks"},
    #             {"name": "patrick", "fullname": "Patrick Star"},
    #             {"name": "squidward", "fullname": "Squidward Tentacles"},
    #             {"name": "ehkrabs", "fullname": "Eugene H. Krabs"},
    #         ],
    #     )
         
    #     print(insert(user_table).values().compile(engine))
    #     INSERT INTO user_account DEFAULT VALUES
    
    #     Insert Returning PK and other attributes
    #     insert_stmt = insert(address_table).returning(
    #         address_table.c.id, address_table.c.email_address
    #     )
    #     print(insert_stmt)
    #     INSERT INTO address (id, user_id, email_address)
    #     VALUES (:id, :user_id, :email_address)
    #     RETURNING address.id, address.email_address

    #     Insert From Select     
    #     select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
    #     insert_stmt = insert(address_table).from_select(
    #         ["user_id", "email_address"], select_stmt
    #     )
    #     print(insert_stmt.returning(address_table.c.id, address_table.c.email_address))
    #     INSERT INTO address (user_id, email_address)
    #     SELECT user_account.id, user_account.name || :name_1 AS anon_1
    #     FROM user_account RETURNING address.id, address.email_address

    #     Insert From Select
    #     select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
    #     insert_stmt = insert(address_table).from_select(
    #         ["user_id", "email_address"], select_stmt
    #     )
    #     print(insert_stmt)
    #     INSERT INTO address (user_id, email_address)
    #     SELECT user_account.id, user_account.name || :name_1 AS anon_1
    #     FROM user_account


    # SELECT XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
    # from sqlalchemy import select
    
    #with engine.connect() as conn:
    with Session(engine) as session: # returns ORM object as row
        stmt = select(user_table).where(user_table.c.name == "spongebob")
        print(stmt)
        for row in session.execute(stmt):
            print(row)

        # print(select(user_table.c.name, user_table.c.fullname))
        # print(select(user_table.c["name", "fullname"]))
        # print(select(User))
        # row = session.execute(select(User)).first()
        # user = session.scalars(select(User)).first() # returns first “column” of each row at once
        # name, fullname = select(User.name, User.fullname)
        # row = session.execute(select(User.name, User.fullname)).first()
        # session.execute(select(User.name, Address).where(User.id == Address.user_id).order_by(Address.id)).all()
        # session.execute(select(("Username: " + user_table.c.name).label("username"),).order_by(user_table.c.name))
        # select(address_table.c.email_address)
        #     .select_from(user_table)
        #     .join(address_table, user_table.c.id == address_table.c.user_id)
        # )
        # select(user_table).join(address_table, isouter=True)
        # select(user_table).join(address_table, full=True)
        # select(user_table).order_by(user_table.c.name)
        # select(User).order_by(User.fullname.desc())
        # select(User.name, func.count(Address.id).label("count"))
        #     .join(Address)
        #     .group_by(User.name)
        #     .having(func.count(Address.id) > 1)
        # )
        # print(result.all())
        # select(Address.user_id, func.count(Address.id).label("num_addresses"))
        #     .group_by("user_id")
        #     .order_by("user_id", desc("num_addresses"))
        # )
        # subq = (
        #     select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
        #     .group_by(address_table.c.user_id)
        #     .subquery()
        # )
        # print(select(subq.c.user_id, subq.c.count))

        # subq = select(Address).where(~Address.email_address.like("%@aol.com")).subquery()
        # address_subq = aliased(Address, subq)
        # stmt = (
        #     select(User, address_subq)
        #     .join_from(User, address_subq)
        #     .order_by(User.id, address_subq.id)
        # )
        # for user, address in session.execute(stmt):
        #     print(f"{user} {address}")

        # from sqlalchemy import union_all
        # stmt1 = select(user_table).where(user_table.c.name == "sandy")
        # stmt2 = select(user_table).where(user_table.c.name == "spongebob")
        # u = union_all(stmt1, stmt2)
        # with engine.connect() as conn:
        #     result = conn.execute(u)
        #     print(result.all())

        # func.now()  
        # func.count("*")
        # func.cast("1", Integer)
        # func.concat("a", "b")
        # func.aggregate_strings("a", "b")
        # func.length("a")
        # func.max("a")
        # func.min("a")
        # func.sum("a")
        # func.random
        # func.sysdate        

        # print(select(func.count()).select_from(user_table))
        # print(select(func.count()).select_from(user_table).where(user_table.c.name == "sandy"))
        # print(select(func.lower("A String With Much UPPERCASE")))
        # select(func.now())

        # from sqlalchemy.dialects import postgresql
        # print(select(func.now()).compile(dialect=postgresql.dialect()))
        # SELECT now() AS now_1
        # from sqlalchemy.dialects import oracle
        # print(select(func.now()).compile(dialect=oracle.dialect()))
        # SELECT CURRENT_TIMESTAMP AS now_1 FROM DUAL

        # from sqlalchemy import JSON
        # function_expr = func.json_object('{a, 1, b, "def", c, 3.5}', type_=JSON)
        # stmt = select(function_expr["def"])
        # print(stmt)
        # SELECT json_object(:json_object_1)[:json_object_2] AS anon_1

    
    # UPDATE XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # https://docs.sqlalchemy.org/en/20/tutorial/data_update.html
    # from sqlalchemy import update
    
    #with engine.connect() as conn:
    with Session(engine) as session: # returns ORM object as row
        # stmt = (
        #     update(user_table)
        #     .where(user_table.c.name == "patrick")
        #     .values(fullname="Patrick the Star")
        # )
        # stmt = update(user_table).values(fullname="Username: " + user_table.c.name)
        
        # from sqlalchemy import bindparam
        # stmt = (
        #     update(user_table)
        #     .where(user_table.c.name == bindparam("oldname"))
        #     .values(name=bindparam("newname"))
        # )
        # with engine.begin() as conn:
        #     conn.execute(
        #         stmt,
        #         [
        #             {"oldname": "jack", "newname": "ed"},
        #             {"oldname": "wendy", "newname": "mary"},
        #             {"oldname": "jim", "newname": "jake"},
        #         ],
        #     )
        # 
        # scalar_subq = (
        #     select(address_table.c.email_address)
        #     .where(address_table.c.user_id == user_table.c.id)
        #     .order_by(address_table.c.id)
        #     .limit(1)
        #     .scalar_subquery()
        # )
        # update_stmt = update(user_table).values(fullname=scalar_subq)
        # print(update_stmt)    





        

        