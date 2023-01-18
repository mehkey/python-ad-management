import uvicorn
from fastapi import FastAPI, Depends

from app.routers import Campaigns

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext import declarative

#from app import configs

def get_session():
    session = database.SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI() #FastAPI(dependencies=[Depends(get_session)])

app.include_router(Campaigns.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)