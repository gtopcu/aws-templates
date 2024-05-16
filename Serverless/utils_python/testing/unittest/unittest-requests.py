
# https://www.youtube.com/watch?v=-F6wVOlsEAM

# pip install requests
import requests
import unittest
from unittest.mock import Mock, patch

def get_userdata(user_id):
    response = requests.get(f"http://api.example.com/{user_id}")
    return response.json()


class TestGetUserData(unittest.TestCase):

    @patch('requests.get')
    def test_get_userdata(self, mock_get):
        mock_response = Mock()
        response_dict = {"name": "John"}
        mock_response.json.return_value = response_dict
        
        mock_get.return_value = mock_response
        userdata = get_userdata(1)
        mock_get.assert_called_with("http://api.example.com/1")
        mock_get.assert_called()
        mock_get.assert_not_called()
        self.assertEqual(userdata["name"], "John")
        self.assertEqual(userdata, response_dict)
        self.assertAlmostEqual
        self.assertTrue
        self.assertFalse
        self.assertGreater
        self.assertRegex
        self.assertRaises
        self.assertIs
        self.assertIsNone
        self.assertCountEqual
        self.assertIn
        self.fail("failed the test!")
    
    if __name__ == "__main__":
        unittest.main()

    # @patch('requests.get')
    # def test_get_userdata(self, mock_get):
    #     mock_get.return_value.json.return_value = {"name": "John"}
    #     userdata = get_userdata(1)
    #     self.assertEqual(userdata["name"], "John")
    #     mock_get.assert_called_with("http://api.example.com/1")

    #     with patch("requests.get") as mock_get:
    #         self.assertEqual(userdata["name"], "John")
    #         mock_get.assert_called()
    #         mock_get.assert_called_with("http://api.example.com/1")
    #         mock_get.assert_called_once()
    #         mock_get.assert_called_once_with("http://api.example.com/1")
    #         mock_get.assert_any_call("http://api.example.com/1")
    #         mock_get.assert_any_call("http://api.example.com/2")
    #         mock_get.assert_has_calls([
    #             call("http://api.example.com/1"),
    #             call("http://api.example.com/2")
    #         ])
    #         mock_get.assert_not_called()







