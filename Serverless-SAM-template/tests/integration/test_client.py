import pytest


@pytest.fixture
def api_client():
    client = ""
    return client


@pytest.fixture
def mock_response(mocker):
    response = {
        "data": [
            {"code": "CZ", "name": "Czech Republic", "refresh_start_time": 2},
            {"code": "IL", "name": "Israel", "refresh_start_time": 2},
        ]
    }
    mocker.patch(
        "Client._request_api",
        return_value=response,
    )

"""
def test_get_countries(client, mock_country_query):
    countries = mock_response()
    assert len(countries) == 2

    first_country = countries[0]
    assert first_country.code == "CZ"
    assert first_country.name == "Czech Republic"
"""