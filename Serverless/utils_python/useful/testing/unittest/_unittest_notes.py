

# https://realpython.com/python-mock-library/
# https://docs.pytest.org/en/stable/how-to/monkeypatch.html
# https://www.youtube.com/watch?v=-F6wVOlsEAM
# https://www.youtube.com/watch?v=WFRljVPHrkE

import unittest
from unittest.mock import Mock, MagicMock, patch, ANY, AsyncMock, 

if __name__ == "__main__":
    val = ANY
    unittest.main()

# class TestHolidays(unittest.TestCase):
#     def test_lambda_requests_timeout(self):
#         with patch("lambda_handler.requests") as mock_requests:
#             mock_requests.get.side_effect = Timeout
#             with self.assertRaises(Timeout):
#                 get_holidays()
#                 mock_requests.get.assert_called_once()


###########################################################################################################################
# PATCH
# You can use patch() as either a decorator or a context manager giving you control over the scope

# @patch("requests.get", return_value=Mock(status_code=200, json=lambda: {"name": "John"}))
# @patch("lambda_handler.requests.get", return_value=Mock(status_code=200, json=lambda: {"name": "John"})) # patch requests in lambda_handler.py
# @patch.object(requests, "get", side_effect=requests.exceptions.Timeout) # partial patching
# def test_api(self, mock_requests):
#   response = requests.get("http://localhost/api")

# Patching requests in lambda_handler.file with Timeout 
# from requests import Timeout
# with patch("lambda_handler.requests") as mock_requests: # mock_request -> MagicMock
#     mock_requests.post.side_effect = Timeout
#     mock_requests.post.json.return_value = "{ 'response': 'success' }"

# @patch("lambda_module.handler")
# def test_func(mock_handler): # mock_handler -> MagicMock
#     mock_handler.side_effect = KeyError
#     mock_handler.return_value = "{ "response": "success" }"

# with patch("lambda_module.logger") as logger:
#     yield logger

# Patch only in __main__ local scope
# with patch("__main__.is_weekday"):
#     is_weekday()


###########################################################################################################################
# Mock

# Can assign attributes/methods during creation or anytime after
# mock = Mock()
# mock.some_attribute
# mock.do_something()
# # do_something(mock) # Pass mock as an argument

# mock = Mock(side_effect=Exception) -> mock()
# mock = Mock(return_value=True)     -> mock()
# mock = Mock(name="Python Mock")    -> mock
# mock = Mock(spec=["is_weekday", "get_holidays"])

# mock.configure_mock(return_value=3, side_effect=KeyError}
# mock.reset_mock(visited=None, return_value=True, side_effect=False)
# # Concise initialization using a configuration dict
# holidays = {"12/25": "Christmas", "7/4": "Independence Day"}
# response_mock = Mock(**{"json.return_value": holidays})

# # Patch the json library
# json = Mock()
# json.dumps() # accepts any argument, returns Mock()

# # Assertions
# json.loads.assert_called()
# json.loads.assert_called_once() 
# json.loads.assert_called_with("{"key": "value"}")           # assert_called_with(*args, **kwargs)
# json.loads.assert_called_once_with("{"key": "value"}"")      # assert_called_once_with(*args, **kwargs): 
# json.loads.assert_not_called()

# self.assertEqual(userdata["name"], "John")
# self.assertEqual(userdata, response_dict)
# self.assertAlmostEqual
# self.assertTrue
# self.assertFalse
# self.assertGreater
# self.assertRegex
# self.assertRaises
# self.assertIs
# self.assertIsNone
# self.assertCountEqual
# self.assertIn
# self.fail("failed the test!")

# # Number of times you called loads():
# json.loads.call_count   

# # The last loads() call
# json.loads.call_args
# # call('{"key": "value"}')

# # List of loads() calls:
# json.loads.call_args_list
# # [call('{"key": "value"}')]

# # List of calls to json's methods (recursively):
# json.method_calls

# # Side-effects
# # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
#
# from requests.exceptions import Timeout
# requests = Mock()
# class TestHolidays(unittest.TestCase):
#     def test_get_holidays_timeout(self):
#         requests.get.side_effect = Timeout
#         with self.assertRaises(Timeout):
#             response = requests.get("http://localhost/api/holidays")


###########################################################################################################################
# MagicMock

# magic_mock = MagicMock()
# magic_mock.configure_mock(return_value=3, side_effect=KeyError)
# magic_mock.reset_mock(visited=None, return_value=True, side_effect=False)
# holidays = {"12/25": "Christmas", "7/4": "Independence Day"}
# response_mock = MagicMock(**{"json.return_value": holidays})

# magic_mock.call_count
# magic_mock.call_args
# magic_mock.call_args_list
# magic_mock.called
# magic_mock.return_value
# magic_mock.side_effect

# magic_mock.assert_called()
# magic_mock.assert_not_called()
# magic_mock.assert_called_once()
# magic_mock.assert_any_call
# magic_mock.assert_has_calls
# magic_mock.assert_called_with       # (*args, **kwargs)
# magic_mock.assert_called_once_with  # (*args, **kwargs)

# self.assertEqual(userdata["name"], "John")
# self.assertEqual(userdata, response_dict)
# self.assertAlmostEqual
# self.assertTrue
# self.assertFalse
# self.assertGreater
# self.assertRegex
# self.assertRaises
# self.assertIs
# self.assertIsNone
# self.assertCountEqual
# self.assertIn
# self.fail("failed the test!")



