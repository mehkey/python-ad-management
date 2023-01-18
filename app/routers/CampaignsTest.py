import pytest
from .main import app

@pytest.fixture
def client():
    # Start the API server
    app.test_client()
    yield app

def test_create_campaign(client):
    # Send a POST request to the /campaigns endpoint
    response = client.post("/campaigns", json={
        "name": "My Campaign",
        "goal": "conversion",
        "budget": 500.0
    })
    # Check that the response status code is 201 (Created)
    assert response.status_code == 201
    # Check that the response contains the campaign ID
    assert "id" in response.json()
