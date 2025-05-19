

# https://www.youtube.com/watch?v=gkHSIOxh60s
# https://logfire-eu.pydantic.dev/gtopcu/starter-project/settings/setup

# pip install 'logfire[fastapi]' httpx

import sqlite3

import logfire
import httpx
from fastapi import FastAPI

# create a fastapi app, see https://fastapi.tiangolo.com/reference/fastapi/
app = FastAPI()

# ===========================================================================================================
# https://logfire-eu.pydantic.dev/gtopcu/starter-project/settings/setup 
# pip install 'logfire[fastapi,asyncpg]'
# pip install 'logfire[fastapi,sqlite3,httpx]'
# poetry add 'logfire[fastapi]'

import logfire
# logfire.configure(token='')
# logfire.instrument_system_metrics()
# logfire.instrument_starlette()
# logfire.instrument_fastapi(app, capture_headers=True)
# logfire.instrument_asgi()
# logfire.instrument_wsgi()
# logfire.instrument_sqlalchemy()
# logfire.instrument_sqlite3()
# logfire.instrument_asyncpg()
# logfire.instrument_flask()
# logfire.instrument_openai()
# logfire.instrument_anthropic()
# logfire.instrument_requests()
# logfire.instrument_aiohttp_client()
# logfire.instrument_httpx()
# logfire.instrument_aws_lambda()

# logfire.log_slow_async_callbacks(5)
# logfire.install_auto_tracing("fastapi", 0, "error")

# logfire.info('Hello, {place}!', place='World')
# logfire.debug('debug log')
# with logfire.span('This is a span {a=}', a='data'):
#         logfire.info('new log 1')
# logfire.trace('This is a trace log')
# @logfire.instrument()
# def func(): ...

# uv run logfire projects use
# ===========================================================================================================

# sqlite database URL
db_url = 'https://files.pydantic.run/pydantic_pypi.db'
# db_url = "sqlite:///fastapi_logfire.db"

# download the data and create the database
with logfire.span('preparing database'):
    with logfire.span('downloading data'):
        r = httpx.get(db_url)
        r.raise_for_status()

    with logfire.span('create database'):
        with open('pydantic_pypi.db', 'wb') as f:
            f.write(r.content)
        connection = sqlite3.connect('pydantic_pypi.db')


# create an endpoint for getting the number of power plants in a country
@app.get('/country/{country}/')
async def read_item(country: str):
    cursor = connection.cursor()
    cursor.execute(
        'select count(*) from pydantic_pypi where country_code = ?',
        (country,)
    )
    row = cursor.fetchone()
    return {'count': row[0]}


# this endpoint just raise an exception, so you can see how errors
# are displayed in Logfire
@app.post('/error/')
async def error():
    raise RuntimeError('This is what an error looks like')

# to make requests to the fastapi appl, we use a custom transport
# with httpx, see https://www.python-httpx.org/advanced/transports/
# t = httpx.ASGITransport(app=app)
# async with httpx.AsyncClient(transport=t, base_url='http://test') as client:
#     logfire.instrument_httpx(client, capture_headers=True)
#     # make a request to the country endpoint
#     r = await client.get('/country/GB/')
#     assert r.status_code == 200, r.status_code
#     print('response:', r.json())

#     try:
#         r = await client.post('/error/')
#     except RuntimeError as e:
#         print('/error/ raised', e)

def main(): 
    import uvicorn 
    uvicorn.run(app, port=8000, log_level="debug", reload=False, access_log=False, use_colors=True) 

if __name__ == "__main__":
    main()


