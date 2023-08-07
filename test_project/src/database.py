from configparser import ConfigParser
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = ConfigParser()
config.read(Path(__file__).parent.parent.joinpath('config.ini'))

username = config.get('DB', 'USERNAME')
password = config.get('DB', 'PASSWORD')
database_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
port = config.get('DB', 'PORT')
url = f'postgresql://{username}:{password}@{domain}:{port}/{database_name}'
# url = f'sqlite3://?{username}:{password}@{domain}:{port}/{database_name}'
Base = declarative_base()
engine = create_engine(url, echo=False)

DBSession = sessionmaker(bind=engine)
session = DBSession()