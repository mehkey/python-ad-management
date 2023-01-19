#import sqlalchemy as sa
#from sqlalchemy import func
#from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Date, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#from datetime import datetime, timedelta


from app.database import Base
from sqlalchemy import func


class AdCampaign(Base):
    __tablename__ = 'ad_campaigns'

    campaign_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = Column(Float)
    status = Column( String)

    ad_groups = relationship("AdGroup", back_populates="ad_campaign")


class AdGroup(Base):
    __tablename__ = 'ad_groups'

    adgroup_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    targeting_criteria = Column(String)
    campaign_id = Column(Integer, ForeignKey('ad_campaigns.campaign_id'))
    ad_campaign = relationship("AdCampaign", back_populates="ad_groups")
    ads = relationship("Ad", back_populates="ad_group")

class Ad(Base):
    __tablename__ = 'ads'

    ad_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image_url = Column(String)
    destination_url = Column(String)
    adgroup_id = Column(Integer, ForeignKey('ad_groups.adgroup_id'))
    ad_group = relationship("AdGroup", back_populates="ads")

class Advertiser(Base):
    __tablename__ = 'advertisers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    budget = Column(Float)
    #ad_campaigns = relationship("AdCampaign", back_populates="advertiser")

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    #advertiser = relationship("Advertiser", back_populates="users")