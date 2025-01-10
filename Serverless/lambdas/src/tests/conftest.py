import pytest
from dataclasses import dataclass
import os

# os.environ["DDB_TABLE_NAME"] = "table-1"

# @pytest.fixture(scope="session", autouse=True)
# def set_env():
#     mp = pytest.MonkeyPatch()
#     print("Setting monkeypatch globally..")
#     mp.setenv("DDB_TABLE_NAME", "table-1")
#     yield
#     mp.undo()  # Clean up after all tests are done
