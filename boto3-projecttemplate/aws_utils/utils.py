import uuid
import requests
import datetime, time

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def sleep(seconds: int):
    time.sleep(seconds)

def generate_uuid():
    return str(uuid.uuid4())

def request(endpoint_url: str):
    if endpoint_url is None:
        endpoint_url = "http://httpbin.org/status/500"
    try:
        resp = requests.get(endpoint_url)
        resp.raise_for_status()
        return resp
    except requests.HTTPError as e:
        raise RuntimeError(f"Received a HTTP 5xx error: {e}") from e
