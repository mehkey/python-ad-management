from main import app
#from fastapi.testclient import TestClient

import pytest
from starlette.testclient import TestClient

import asyncio
import pytest

pytest_plugins = ('pytest_asyncio',)

@pytest.fixture
def client():
    client = TestClient(app)
    yield client

import asyncio

#pytest_plugins = ('pytest_asyncio',)

@staticmethod
@pytest.mark.asyncio
async def test_create_campaign(client):
    # Send a POST request to the /campaigns endpoint
    response = client.post("/campaigns", json={
        "name": "My Campaign",
        "goal": "conversion",
        "budget": 500.0
    })
    # Check that the response status code is 201 (Created)
    #print(response.status_code)
    assert response.status_code == 201
    # Check that the response contains the campaign ID
    assert "id" in response.json()
