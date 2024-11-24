
# pip install pytest requests
# pytest -v test_rest.py

import json
import os
import pytest
import requests

def load_json_file(filename):
    """Helper function to load JSON from a file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    with open(file_path, 'r') as file:
        return json.load(file)

class TestAPIEndpoint:
    
    @pytest.fixture
    def api_url(self):
        """Fixture for API URL - can be configured based on environment"""
        return "https://api.example.com/endpoint"  # Replace with your API endpoint
    
    @pytest.fixture
    def request_data(self):
        """Fixture to load request data from JSON file"""
        return load_json_file('request.json')
    
    @pytest.fixture
    def expected_response(self):
        """Fixture to load expected response from JSON file"""
        return load_json_file('response.json')
    
    def test_post_endpoint(self, api_url, request_data, expected_response):
        """Test POST request to API endpoint"""
        # Set up headers
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Send POST request
        response = requests.post(
            api_url,
            json=request_data,
            headers=headers
        )
        
        # Assert status code is successful
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        
        # Parse response JSON
        actual_response = response.json()
        
        # Compare actual response with expected response
        assert actual_response == expected_response, \
            f"Response mismatch.\nExpected: {expected_response}\nActual: {actual_response}"

    @pytest.mark.parametrize("missing_field", ["required_field1", "required_field2"])
    def test_post_endpoint_missing_required_fields(self, api_url, request_data, missing_field):
        """Test POST request with missing required fields"""
        # Create a copy of request data and remove a required field
        modified_data = request_data.copy()
        modified_data.pop(missing_field, None)
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Send POST request
        response = requests.post(
            api_url,
            json=modified_data,
            headers=headers
        )
        
        # Assert that the request fails with a 400 status code
        assert response.status_code == 400, \
            f"Expected status code 400 for missing {missing_field}, but got {response.status_code}"