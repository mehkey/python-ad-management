
from app.models import AllModels as models
from app.schemas import AllSchemas as schemas
from app.services._base_service import BaseService


class AdCampaignService(BaseService[models.AdCampaign]):
    __entity_type__ = models.AdCampaign

    def _convert_schema_to_db_model(self, ad_campaign: schemas.AdCampaignCreate) -> models.AdCampaign:
        ad_groups = [self._convert_schema_to_db_model_ag(ag) for ag in ad_campaign.ad_groups]
        resp = models.AdCampaign(name=ad_campaign.name, start_date=ad_campaign.start_date, end_date=ad_campaign.end_date, budget=ad_campaign.budget, ad_groups=ad_groups)
        print(resp.start_date)
        print(resp.__dict__)
        return resp

    def _convert_schema_to_db_model_ag(self, ad_group: schemas.AdGroupCreate) -> models.AdGroup:
        ads = [self._convert_schema_to_db_model_ad(a) for a in ad_group.ads]
        return models.AdGroup(name=ad_group.name, targeting_criteria=ad_group.targeting_criteria, ads=ads)

    def _convert_schema_to_db_model_ad(self, ad: schemas.AdCreate) -> models.Ad:
        return models.Ad(title=ad.title, image_url=ad.image_url, destination_url=ad.destination_url)
