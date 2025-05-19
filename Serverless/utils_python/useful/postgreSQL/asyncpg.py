
# pip install asyncpg logfire

import asyncpg
from asyncpg.connection import Connection
from asyncpg.cursor import CursorFactory
from asyncpg import Record

import logfire

@logfire.instrument()
async def prepare_db(pg_host: str, pg_port: int, database:str, user:str, pw: str, create_database: bool) -> None:  # 1 usage
    if create_database:
        conn = await asyncpg.connect(host=pg_host, port=pg_port, database=database, user=user, password=pw)
        try:
            db_exists = await conn.fetchval('SELECT 1 FROM pg_database WHERE datname = $1', database)
            if not db_exists:
                await conn.execute(f'CREATE DATABASE {database}')
        finally:
            await conn.close()
    
    conn = await asyncpg.connect(host=pg_host, port=pg_port, database=database, user=user, password=pw)
    # try:
    #     async with conn.transaction():
    #         await _create_schema(conn)
    # finally:
    #     await conn.close()

async def do_stuff(conn: Connection, database: str):
    # conn.get_server_version()

    # await conn.execute(f'CREATE DATABASE {database}')
    # await conn.executemany('INSERT INTO mytab (a) VALUES ($1, $2, $3);', [(1, 2, 3), (4, 5, 6)])    

    # db_exists = await conn.fetchval('SELECT 1 FROM pg_database WHERE datname = $1', database)
    # count = await conn.fetchval('SELECT COUNT(1) FROM customers')
    # result:Record = await conn.fetchrow('SELECT * FROM customers')
    # results:list[Record] = await conn.fetchmany('SELECT * FROM customers LIMIT 3 OFFSET 1')
    ids:list[Record] = await conn.fetch('SELECT id FROM customers ORDER BY name DESC LIMIT $1', limit)
    rows = []
    for id in ids:
        row:Record = await conn.fetchrow(f'SELECT * from customers WHERE id={id}')
        rows.append(row)

    # cursor:CursorFactory = conn.cursor('SELECT now()')
    # tc:Transaction = await conn.transaction()
    # conn.close()
    # conn.terminate()