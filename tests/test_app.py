import pytest
from app import app
from unittest.mock import patch, MagicMock
from types import SimpleNamespace  # <-- Add this import

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@patch('openai.OpenAI')
def test_generate_test_cases(mock_openai_class, client):
    mock_openai_instance = mock_openai_class.return_value

    # Explicitly mock the chat and completions attributes
    mock_chat = MagicMock()
    mock_completions = MagicMock()
    mock_chat.completions = mock_completions
    mock_openai_instance.chat = mock_chat

    # Use SimpleNamespace to mock the structure expected by your route
    mock_completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(
            message=SimpleNamespace(
                content="Test case 1: User logs in with valid credentials."
            )
        )]
    )

    response = client.post("/generate", json={"feature": "User login"})
    assert response.status_code == 200
    assert "test_cases" in response.get_json()
