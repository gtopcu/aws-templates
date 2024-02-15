
# requests/aiohttp/httpx
# https://www.youtube.com/watch?v=OPyoXx0yA0I
# requests does not support concurrency!

from typing import Any
import requests
import aiohttp
import httpx
import asyncio
import time


def requests_get(endpoint_url: str, headers: dict, timeout: int = 30) -> requests.Response:
    try:
        resp = requests.get(endpoint_url, headers=headers, timeout=timeout)
        httpError = resp.raise_for_status()
        return resp
    except requests.HTTPError as e:
        #logger.exception(e)
        raise RuntimeError(f"HTTP error: {e}") from e
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(f"Connection error: {e}") from e
        #raise SystemExit(e)

def requests_put(endpoint_url: str, payload: str, timeout: int = 30) -> Any:
    # payload = {
    #     "user_id": "1000",
    #     "isActive": True
    # }
    response = requests.put(endpoint_url, json=payload)
    #status_code = response.status_code
    #response_body = response.json()
    return response.json()

# Session reuses the same connection, much faster
def requests_get_with_session(session: requests.Session) ->:
    response = session.get("XXXXXXXXXXXXXXXXXXXXXXX")
    return response.json()

def main() -> None:
    start = time.perf_counter()
    with requests.Session() as session:
        response = requests_get_with_session(session)
    end = time.perf_counter()
    print(f"Time elapsed: {end - start:.2f}")

# aiohttp - supports concurrency
async def async_aiohttp_get(session: aiohttp.ClientSession, url: str) -> Any:
    async with session.get(url) as response:
        return await response.json()

async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        response = async_aiohttp_get(session, "XXXXXXXXXXXXXXXXXXXXXXX")

# httpx - supports concurrency
async def httpxget(client: httpx.AsyncClient, url: str) -> Any:
    response = await client.get(url)
    return response.json()

async def httpx_get() -> None:
    async with httpx.AsyncClient() as client:
        tasks = [ httpxget(client, "XXXXXXXXXXXXXXXXXXXXXXX") for _ in range(10) ]
        #tasks = [ httpxget(client, "http://url1.com"), httpxget(client, "http://url2.com") ]
        results = await asyncio.gather(*tasks)
    for result in results:
        print(result)