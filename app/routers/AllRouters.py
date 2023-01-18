from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import AllSchemas as schemas
from app.database import get_session
from app.services import AllServices 
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.responses import ORJSONResponse
import json

router = APIRouter(
    tags=['AdCampaign'],
    responses={404: {'description': 'Not Found'}}
)

@router.post(path='/ad-campaigns', response_model=schemas.AdCampaign) #, response_class=JSONResponse)
async def create_ad_campaign(ad_campaign: schemas.AdCampaignCreate, session: Session = Depends(get_session)):
    ad_campaign.status = 'CREATED'
    resp= AllServices.AdCampaignService(session).add(ad_campaign)
    #print(resp)
    #print(resp.__dict__)
    #return resp
    #return Response(content=resp, media_type='application/json')
    return resp #JSONResponse(json.dumps(resp))#JSONResponse(resp) JSONResponse


@router.get(path='/ad-campaign/{campaign_id}', response_model=schemas.AdCampaign)
async def get_ad_campaign(campaign_id: int, session: Session = Depends(get_session)):
    ad_campaign_service = AllServices.AdCampaignService(session)
    db_ad_campaign = ad_campaign_service.get(campaign_id)
    if db_ad_campaign is None:
        raise HTTPException(status_code=404, detail="Ad Campaign not found")
    return db_ad_campaign
