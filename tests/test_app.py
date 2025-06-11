
import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@patch('openai.ChatCompletion.create')
def test_generate_test_cases(mock_openai, client):
    mock_openai.return_value = {
        "choices": [{
            "message": {
                "content": "Test case 1: User logs in with valid credentials."
            }
        }]
    }

    response = client.post("/generate", json={"feature": "User login"})
    assert response.status_code == 200
    assert "test_cases" in response.get_json()
