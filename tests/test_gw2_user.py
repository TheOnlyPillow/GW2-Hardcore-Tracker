from unittest.mock import Mock, patch
import pytest


from hardcore_tracker.constants import TEST_API_KEY, TEST_USERNAME
from hardcore_tracker.gw2_user import GW2_User


@pytest.fixture
def fake_user():
    return {"username": TEST_USERNAME,
            "api_key": TEST_API_KEY
            }

@pytest.fixture
def bad_request():
    response = {
        "status_code":400,
        "data":None
    }
    return response

@pytest.fixture
def good_request():
    response = {
        "status_code": 200,
        "data":{
            "username": TEST_USERNAME,
            "api_key": TEST_API_KEY
        }
    }
    return response

@patch("hardcore_tracker.gw2_user.requests")
def test_create_user(mock_requests, good_request, fake_user):
    mock_requests.get.return_value.json.return_value = good_request
    test_user = GW2_User(**fake_user)
    assert isinstance(test_user, GW2_User)
    assert test_user.api_key == TEST_API_KEY
    assert test_user.username == TEST_USERNAME
    assert test_user.characters == []
    assert test_user.any_non_hardcore_characters == False