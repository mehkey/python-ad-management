import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext import declarative



import configparser
import os

ENV = os.environ.get('ENV', 'DEV')
if ENV not in ('DEV', 'STAGING', 'PROD'):
    raise RuntimeError(
        f'Environment "{ENV}" is not recognized. Check your environment variable to make'
        'sure that the environment variable ENV is set to one of "DEV", "STAGING" or "PROD".'
    )

config = configparser.ConfigParser()
print(f"./configs/{ENV.lower()}.ini")
file = config.read(f"./configs/{ENV.lower()}.ini")
if not file:
    raise RuntimeError('Unable to read config file.')

db_config = config['Database']
POSTGRES_USER = db_config.get('postgres_user')
POSTGRES_PASSWORD = db_config.get('postgres_password')
POSTGRES_HOST = db_config.get('postgres_host')
POSTGRES_PORT = db_config.get('postgres_port', '5431')
POSTGRES_DB = db_config.get('postgres_db', 'admanagement')
POSTGRES_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'



engine = sa.create_engine(POSTGRES_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()