from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

from typing import List

class AdCreate(BaseModel):
    title: str
    image_url: str
    destination_url: str

class AdGroupCreate(BaseModel):
    name: str
    targeting_criteria: str
    ads: List[AdCreate]

class AdCampaignCreate(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    budget: float
    ad_groups: List[AdGroupCreate]
    status: str
    
    '''
    @validator("start_date")
    def start_date_validator(cls, value):
        if value < datetime.now():
            raise ValueError("start_date must be greater than current date")
        return value
        
    @validator("end_date")
    def end_date_validator(cls, value):
        if value < cls.start_date:
            raise ValueError("end_date must be greater than start_date")
        return value
    '''

class Ad(BaseModel):
    ad_id: int
    title: str
    image_url: str
    destination_url: str

    class Config:
        orm_mode = True

class AdGroup(BaseModel):
    adgroup_id: int
    name: str
    targeting_criteria: str
    ads: List[Ad]

    class Config:
        orm_mode = True

class AdCampaign(BaseModel):
    campaign_id: int
    name: str
    #start_date: Optional[datetime]
    #end_date: Optional[datetime]
    budget: float
    ad_groups: List[AdGroup]
    advertiser_id: Optional[int]
    status: Optional[str]

    class Config:
        orm_mode = True
