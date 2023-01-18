import json
from fastapi.testclient import TestClient
import unittest
from app.main import app
from fastapi import FastAPI

class TestCreateAdCampaign(unittest.TestCase):
    def setUp(self):
        self.api_client = TestClient(app)

    def test_create_ad_campaign(self):
        data = {
            "name": "Test Ad Campaign",
            "start_date": "2022-01-01T00:00:00",
            "end_date": "2022-12-31T23:59:59",
            "budget": 1000.0,
            "status": "CREATED",
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

        response = self.api_client.post('/ad-campaigns', json=data)

        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.content_type, 'application/json')

        json_response = json.loads(response.text)
        print('RESPONS',json_response)
        self.assertEqual(json_response['name'], data['name'])
        #self.assertEqual(json_response['start_date'], data['start_date'])
        #self.assertEqual(json_response['end_date'], data['end_date'])
        self.assertEqual(json_response['budget'], data['budget'])
        self.assertEqual(json_response['ad_groups'][0]['name'], data['ad_groups'][0]['name'])
        self.assertEqual(json_response['ad_groups'][0]['targeting_criteria'], data['ad_groups'][0]['targeting_criteria'])
        self.assertEqual(json_response['ad_groups'][0]['ads'][0]['title'], data['ad_groups'][0]['ads'][0]['title'])
        self.assertEqual(json_response['ad_groups'][0]['ads'][0]['image_url'], data['ad_groups'][0]['ads'][0]['image_url'])
        self.assertEqual(json_response['ad_groups'][0]['ads'][0]['destination_url'], data['ad_groups'][0]['ads'][0]['destination_url'])

if __name__ == '__main__':
    unittest.main()