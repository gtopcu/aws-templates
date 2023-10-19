import uuid
import requests
import datetime, time

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def sleep(seconds: int):
    time.sleep(seconds)

def generate_uuid():
    return str(uuid.uuid4())

def request(endpoint_url: str, headers: dict, timeout: int = 30) -> requests.Response:
    if endpoint_url is None:
        endpoint_url = "http://httpbin.org/status/200"
    try:
        resp = requests.get(endpoint_url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp
    except requests.HTTPError as e:
        raise RuntimeError(f"Received a HTTP 5xx error: {e}")

def writeFile(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def readFile(filename):
    with open(filename, "r") as file:
        return file.read()