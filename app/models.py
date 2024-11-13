from main import db  # Import db from the main app

from sqlalchemy import Column, String, Integer, DateTime, Text, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Passwords should be hashed in production

class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String, unique=True, nullable=False)

class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    api_key = Column(String, nullable=True)
    description = Column(Text, nullable=True)

class CrawlerLog(Base):
    __tablename__ = 'crawler_logs'
    id = Column(Integer, primary_key=True)
    source = Column(String)  # "darknet" or "clearweb"
    url = Column(String)
    title = Column(String)
    description = Column(Text)
    date_time = Column(DateTime, default=datetime.now)
    context = Column(Text)
    snapshot = Column(Text)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    person_name = Column(String)
    wallet_addresses = Column(Text)  # JSON format for multiple addresses

engine = create_engine('postgresql://admin:vP0wcNFIG4jo@ep-bold-snow-a64ztnv3-pooler.us-west-2.aws.neon.tech/finalengine?sslmode=require')
Base.metadata.create_all(engine)

# db.create_all()
