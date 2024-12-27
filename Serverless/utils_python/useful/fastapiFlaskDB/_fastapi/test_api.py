
import pytest
from fastapi.testclient import TestClient

import app

client = TestClient(app)

API_ENDPOINT = "/api-endpint"

def test_process_array_success():
    request = [
        {"name": "John Doe", "age": 30, "address": "123 Main St"},
        {"name": "Jane Smith", "age": 25, "address": "456 Elm St"}
    ]
    
    response = client.post(API_ENDPOINT, json=request)

    assert response.status_code == 200
    assert response.json() == {"status_code": 200, "status_description": "Success"}

def test_process_array_invalid_json():
    response = client.post(API_ENDPOINT, data="invalid json")
    
    # Check that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422

def test_process_array_missing_field():
    # Define an array with a missing required field (age)
    missing_field_people = [
        {"name": "John Doe", "address": "123 Main St"},
        {"name": "Jane Smith", "age": 25, "address": "456 Elm St"}
    ]
    
    response = client.post("API_ENDPOINT", json=missing_field_people)
    
    # Check that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422

def test_process_array_invalid_type():
    # Define an array with a person having an invalid type for the age field
    invalid_type_people = [
        {"name": "John Doe", "age": "thirty", "address": "123 Main St"},
        {"name": "Jane Smith", "age": 25, "address": "456 Elm St"}
    ]
    
    response = client.post(API_ENDPOINT, json=invalid_type_people)
    
    # Check that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422
