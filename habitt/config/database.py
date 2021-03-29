import datetime
import os

import databases
from sqlalchemy import Column, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HABITT_DB_NAME = os.getenv("HABITT_DB_NAME", "habitt")
HABITT_DB_USER = os.getenv("HABITT_DB_USER", "habitt")
HABITT_DB_PASSWORD = os.getenv("HABITT_DB_PASSWORD", "habitt")
HABITT_DB_HOST = os.getenv("HABITT_DB_HOST", "localhost")
HABITT_DB_PORT = os.getenv("HABITT_DB_PORT", "5436")

DATABASE_URL = f"postgresql://{HABITT_DB_USER}:{HABITT_DB_PASSWORD}@{HABITT_DB_HOST}:{HABITT_DB_PORT}/{HABITT_DB_NAME}"

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(object):
    created_at = Column(DateTime, default=datetime.datetime.now())


Base = declarative_base(cls=Base)
