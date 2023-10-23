import uuid
import requests
import json
import datetime, time

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def sleep(seconds: int):
    time.sleep(seconds)

def generate_uuid():
    return str(uuid.uuid4())

def requests_get(endpoint_url: str, headers: dict, timeout: int = 30) -> requests.Response:
    try:
        resp = requests.get(endpoint_url, headers=headers, timeout=timeout)
        httpError = resp.raise_for_status()
        return resp
    except requests.HTTPError as e:
        raise RuntimeError(f"Received a HTTP error: {e}")

def requests_put(endpoint_url: str, payload: str, timeout: int = 30) -> requests.Response:
    # payload = {
    #     "user_id": "1000",
    #     "isActive": True
    # }
    response = requests.put(endpoint_url, json=payload)
    #status_code = response.status_code
    #response_body = response.json()
    return response


def writeFile(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def readFile(filename):
    with open(filename, "r") as file:
        return file.read()