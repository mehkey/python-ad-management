import json
import pytest as pytest
from fastapi.testclient import TestClient
#from main import app
from fastapi import FastAPI, Depends

#from . import main.app as a
from app.main import app as a

#import sys
#sys.path.append('../.')
##import os
#os.chdir('..')
'''
@pytest.fixture(scope='module')
def client():
    return TestClient()
'''

client = TestClient(a)

@pytest.fixture
def api_client():
    #app = FastAPI()
    return TestClient(a)

@pytest.mark.asyncio
async def test_create_ad_campaign(api_client):
    data = {
        "name": "Test Ad Campaign",
        "start_date": "2022-01-01T00:00:00",
        "end_date": "2022-12-31T23:59:59",
        "budget": 1000.0,
        "ad_groups": [
            {
                "name": "Test Ad Group",
                "targeting_criteria": "Test targeting criteria",
                "ads": [
                    {
                        "title": "Test Ad",
                        "image_url": "http://test-image-url.com",
                        "destination_url": "http://test-destination-url.com"
                    }
                ]
            }
        ]
    }

    response = await app.post('/ad-campaigns', json=data)

    assert response.status_code == 200
    assert response.content_type == 'application/json'

    json_response = json.loads(await response.text())

    assert json_response['name'] == data['name']
    assert json_response['start_date'] == data['start_date']
    assert json_response['end_date'] == data['end_date']
    assert json_response['budget'] == data['budget']
    assert json_response['ad_groups'][0]['name'] == data['ad_groups'][0]['name']
    assert json_response['ad_groups'][0]['targeting_criteria'] == data['ad_groups'][0]['targeting_criteria']
    assert json_response['ad_groups'][0]['ads'][0]['title'] == data['ad_groups'][0]['ads'][0]['title']
    assert json_response['ad_groups'][0]['ads'][0]['image_url'] == data['ad_groups'][0]['ads'][0]['image_url']
    assert json_response['ad_groups'][0]['ads'][0]['destination_url'] == data['ad_groups'][0]['ads'][0]['destination_url']