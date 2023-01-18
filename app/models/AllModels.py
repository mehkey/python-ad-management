#import sqlalchemy as sa
#from sqlalchemy import func
#from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Date, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#from datetime import datetime, timedelta


from app.database import Base
from sqlalchemy import func


'''
class Player(Base):
    __tablename__ = 'player'

    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(100), nullable=False)
    queue_id = sa.Column('queue_id', sa.Integer, sa.ForeignKey('queue.id'), nullable=False)
    status = sa.Column('status', sa.String(50), nullable=False)
    match_id = sa.Column('match_id', sa.Integer, sa.ForeignKey('match.id'))
    join_time = sa.Column('join_time', sa.DateTime, server_default=func.now())
    attributes = sa.Column('attributes', sa.JSON)

    queue = relationship('Queue', back_populates='players')
    match = relationship('Match', back_populates='players')
'''

class AdCampaign(Base):
    __tablename__ = 'ad_campaigns'

    campaign_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = Column(Float)
    status = Column( String)

    ad_groups = relationship("AdGroup", back_populates="ad_campaign")

    '''
    def __init__(self, name:str, start_date:datetime, end_date:datetime, budget:float):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = 'CREATED'
    '''
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