
# https://www.youtube.com/watch?v=aAy-B6KPld8

from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Boolean, Integer, String
from sqlalchemy import func

engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
connection = engine.connect()

metadata = MetaData() # database schema

user_table = Table(
        """
            CREATE TABLE user (
            id INTEGER NOT NULL, 
            name VARCHAR(50) NOT NULL, 
            address_id INTEGER, 
            working BOOLEAN, 
            updated DATETIME, 
            PRIMARY KEY (id), 
            UNIQUE (name)
        )
        INSERT INTO user (name, address_id, working, updated) VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        SELECT user.id, user.name, user.address_id, user.working, user.updated FROM user WHERE user.name = ?
        """
        'user', 
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String(50), unique=True, nullable=False),
        Column('address_id', Integer, default=0),
        Column('working', Boolean, default=False),
        Column('updated', DateTime, default=func.now()))
        # sa.ForeignKey('address.id'))

metadata.create_all(engine)
# metadata.drop_all(engine)


def insert_user(name:str, address_id:int):
    query = user_table.insert().values(name=name, address_id=address_id)
    connection.execute(query)
    connection.begin
def query_user(name: str):
    query = user_table.select().where(user_table.c.name == name)
    result = connection.execute(query)
    return result.fetchone()
    # return result.fetchmany(10)
    # return result.fetchall()
    # for row in result:
    #     print(row)

if __name__ == "__main__":
    insert_user("John", 1)
    # 
    insert_user("Jane", 2)
    print(query_user("John"))
    print(query_user("Jane"))
