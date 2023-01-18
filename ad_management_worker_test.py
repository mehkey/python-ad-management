
import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock
from your_module import process_ad_campaign, AdCampaign

class TestProcessAdCampaign(unittest.TestCase):
    def setUp(self):
        self.mc = MagicMock()
        self.ad_campaign = AdCampaign(campaign_id=1, name='Test Campaign',
                                      start_date=datetime.now() + timedelta(days=-1),
                                      end_date=datetime.now() + timedelta(days=1))

    def test_process_ad_campaign_created(self):
        self.ad_campaign.start_date = datetime.now() + timedelta(days=1)
        process_ad_campaign(self.ad_campaign, self.mc)
        self.assertEqual(self.ad_campaign.status, 'Created')
        self.mc.set.assert_not_called()
        self.mc.delete.assert_not_called()

    def test_process_ad_campaign_running(self):
        process_ad_campaign(self.ad_campaign, self.mc)
        self.assertEqual(self.ad_campaign.status, 'Running')
        self.mc.set.assert_called_once_with(self.ad_campaign.campaign_id, self.ad_campaign)
        self.mc.delete.assert_not_called()

    def test_process_ad_campaign_finished(self):
        self.ad_campaign.end_date = datetime.now() + timedelta(days=-1)
        process_ad_campaign(self.ad_campaign, self.mc)
        self.assertEqual(self.ad_campaign.status, 'Finished')
        self.mc.set.assert_not_called()
        self.mc.delete.assert_called_once_with(self.ad_campaign.campaign_id)

if __name__ == '__main__':
    unittest.main()