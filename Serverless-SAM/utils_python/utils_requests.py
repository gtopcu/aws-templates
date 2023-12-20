
# requests/aiohttp/httpx
# https://www.youtube.com/watch?v=OPyoXx0yA0I

from typing import Any
import requests


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