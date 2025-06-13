

# https://realpython.com/python-mock-library/
# https://docs.pytest.org/en/stable/how-to/monkeypatch.html
# https://www.youtube.com/watch?v=-F6wVOlsEAM
# https://www.youtube.com/watch?v=WFRljVPHrkE

# pip install requests
import requests
import unittest
from unittest.mock import Mock, patch

# You can use patch() as either a decorator or a context manager giving you control over the scope
with patch:
    pass

mock = Mock()
mock.some_attribute
mock.do_something()

# Pass mock as an argument to do_something()
# do_something(mock)

# Patch the json library
json = Mock()
json.dumps() # accepts any argument, returns Mock()

# Assertions
json.loads.assert_called()
json.loads.assert_called_once() 
json.loads.assert_called_with('{"key": "value"}')           # assert_called_with(*args, **kwargs)
json.loads.assert_called_once_with('{"key": "value"}')      # assert_called_once_with(*args, **kwargs): 
json.loads.assert_not_called()

# Number of times you called loads():
json.loads.call_count   

# The last loads() call
json.loads.call_args
# call('{"key": "value"}')

# List of loads() calls:
json.loads.call_args_list
# [call('{"key": "value"}')]

# List of calls to json's methods (recursively):
json.method_calls

# Side-effects
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect

from requests.exceptions import Timeout

requests = Mock()
class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            response = requests.get("http://localhost/api/holidays")




if __name__ == "__main__":
    unittest.main()
