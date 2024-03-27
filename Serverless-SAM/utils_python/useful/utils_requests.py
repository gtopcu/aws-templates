
# requests does not support concurrency!
# requests/aiohttp/httpx:
# https://www.youtube.com/watch?v=OPyoXx0yA0I

from typing import Any
import requests
import httpx
import aiohttp
import asyncio
import time

# requests-cache:
# https://www.youtube.com/watch?v=cJBYGSXcCgQ
# https://pypi.org/project/requests-cache/
# pip install requests-cache
from typing import Final
from dataclasses import dataclass
from requests_cache import CachedSession
from datetime import timedelta


def requests_get(endpoint_url, headers=None, auth=None, timeout: int = 30) -> requests.Response:
    response = requests.get(endpoint_url, headers=headers, timeout=timeout)
    # data:list[str] = requests.get("http://data.csv").content.decode().split("\n")
    httpError = response.raise_for_status()
    # status_code = response.status_code
    # response_body = response.json()
    # content = response.content
    return response
    # try:
    #     ...
    # except requests.HTTPError as e:
    #     raise RuntimeError(f"HTTP error: {e}") from e
    # except requests.exceptions.ConnectionError as e:
    #     raise RuntimeError(f"Connection error: {e}") from e

def requests_put(endpoint_url, payload, headers=None, auth=None, timeout: int = 30) -> Any:
    # payload = {
    #     "user_id": "1000",
    #     "isActive": True
    # }
    response = requests.post(endpoint_url, headers=headers, auth=auth, timeout=timeout, json=payload)
    httpError = response.raise_for_status()
    #status_code = response.status_code
    #response_body = response.json()
    return response.json()     

def requests_put(endpoint_url, payload, headers=None, auth=None, timeout: int = 30) -> Any:
    response = requests.put(endpoint_url, headers=headers, auth=auth, timeout=timeout, json=payload)
    httpError = response.raise_for_status()
    return response.json()

# # Session reuses the same connection, much faster
# def requests_get_with_session(session: requests.Session) ->:
#     response = session.get("XXXXXXXXXXXXXXXXXXXXXXX")
#     return response.json()

# def main() -> None:
#     start = time.perf_counter()
#     with requests.Session() as session:
#         response = requests_get_with_session(session)
#     end = time.perf_counter()
#     print(f"Time elapsed: {end - start:.2f}")

# ---------------------------------------------------------------------------------------------------------------------

# # aiohttp - supports concurrency
# async def async_aiohttp_get(session: aiohttp.ClientSession, url: str) -> Any:
#     async with session.get(url) as response:
#         return await response.json()

# async def async_main() -> None:
#     async with aiohttp.ClientSession() as session:
#         response = async_aiohttp_get(session, "XXXXXXXXXXXXXXXXXXXXXXX")

# ---------------------------------------------------------------------------------------------------------------------

# # httpx - supports concurrency
# async def httpxget(client: httpx.AsyncClient, url: str) -> Any:
#     response = await client.get(url)
#     return response.json()

# async def httpx_get() -> None:
#     async with httpx.AsyncClient() as client:
#         tasks = [ httpxget(client, "XXXXXXXXXXXXXXXXXXXXXXX") for _ in range(10) ]
#         #tasks = [ httpxget(client, "http://url1.com"), httpxget(client, "http://url2.com") ]
#         results = await asyncio.gather(*tasks)
#     for result in results:
#         print(result)

# ---------------------------------------------------------------------------------------------------------------------

# URL: Final = "https://animechan.vercel.app/api/random"
# session = CachedSession(cache_name="cache/default_cache", expire_after=10, # expire_after=timedelta(days=1)
#                         # cache_control=False, stale_if_error=False, allowable_codes= [200, 202],
#                         # allowable_methods=["GET", "OPTIONS"], always_revalidate=False, serializer=
#                         # ignored_parameters=["api-key"], match_headers=["Accept-Language"]
#                         # backend="sqlite" - DEFAULT
#                         # backend="memory", 
#                     )

# @dataclass
# class Quote:
#     anime: str = None
#     character: str = None
#     quote: str = None

# def get_quote() -> Quote:
#     response = session.get(URL)
#     # response.raise_for_status()
#     # return Quote(**response.json())
#     try:
#         json:dict = response.json()
#         quote = Quote(**json)
#         print(f"{quote.anime} - {quote.character} - {quote.quote}")
#     except Exception as e:
#         print(f"{response.status_code} - {e}")

# print("done")