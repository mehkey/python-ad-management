import asyncio
from typing import Iterable

import asyncpg
import itertools
import networkx as nx
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.models import AllModels as models

from sqlalchemy.sql import text
from asyncio import sleep
import memcache


CONN_POOL: asyncpg.Pool

#connect to the Postgres DB
ENGINE = create_async_engine('postgresql+asyncpg://app:app@localhost:5431/admanagement')
ASYNC_SESSION: sessionmaker = sessionmaker(ENGINE, expire_on_commit=False, class_=AsyncSession)

#connect to the cache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

#start a main thread that loops every 5 seconds
async def main():
    while True:
        async with ASYNC_SESSION() as session:
            ad_campaign = await session.execute(select(models.AdCampaign))

        for a in ad_campaign.scalars():
            
            await process_ad_campaign(a)

        await sleep(5)

#Update the Status from RUNNING to FINISHED if end_date expired
#Update the Status from CREATED to RUNNING we reached the start_date 
async def process_ad_campaign(ad_campaign):
    current_time = datetime.now()
    if ad_campaign.start_date <= current_time < ad_campaign.end_date:
        ad_campaign.status = 'RUNNING'
        mc.set(ad_campaign.campaign_id, ad_campaign)
        await process_ad_groups(ad_campaign.ad_groups)
    elif current_time > ad_campaign.end_date:
        ad_campaign.status = 'FINISHED'
        mc.delete(ad_campaign.campaign_id)
        await process_ad_groups(ad_campaign.ad_groups)
    else:
        ad_campaign.status = 'CREATED'

async def process_ad_groups(ad_groups):
    for ad_group in ad_groups:
        await process_ads(ad_group)

#Update the Memcache if the status is RUNNING or FINISHED
async def process_ads(ad_group):
    ads = ad_group.ads
    for ad in ads:
        if ad_group.status == 'RUNNING':
            mc.set(ad.ad_id, ad)
        elif ad_group.status == 'FINISHED':
            mc.delete(ad.ad_id)


if __name__ == '__main__':
    asyncio.run(main())