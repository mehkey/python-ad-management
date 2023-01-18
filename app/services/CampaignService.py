from app import models
from app import schemas
from app.services._base_service import BaseService


class AdCampaignService(BaseService[models.AdCampaign]):
    __entity_type__ = models.AdCampaign

    def _convert_schema_to_db_model(self, player: schemas.PlayerCreate) -> models.AdCampaign:
        return models.AdCampaign(
            name=player.name,
            queue_id=player.queue_id,
            status='WAITING',
            attributes=player.attributes
        )