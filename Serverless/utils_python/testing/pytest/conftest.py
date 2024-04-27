 
# content of tests/conftest.py
import pytest

def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["info1: did you know that ...", "did you?"]

@pytest.fixture(scope="session")
def db_conn():
    db = " "
    url = " "
    with db.connect(url) as conn: 
        yield conn

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")

