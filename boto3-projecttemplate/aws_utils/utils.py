import uuid
from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_uuid():
    return str(uuid.uuid4())
