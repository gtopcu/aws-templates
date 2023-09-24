import pytest

@pytest.fixture(scope="module", autouse=True)
def testfix():
    return 123
