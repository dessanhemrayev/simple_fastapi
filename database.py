from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

engine = create_engine(
    "postgresql+psycopg2://des:des@localhost/health", 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    nickname = Column(String(200), nullable=False)
    phone = Column(String(100), nullable=False)
    telegram_id = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    hpressure = relationship("Hpressure", backref='user')
    lpressure = relationship("Lpressure", backref='user')
    heatbeatrate = relationship("Heatbeatrate", backref='user')
    
git remote add origin https://github.com/dessanhemrayev/simple_fastapi.git


class Hpressure(Base):
    __tablename__ = 'hpressure'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    created_on = Column(DateTime(), default=datetime.now)
    value = Column(String(50), nullable=False)
    

class Lpressure(Base):
    __tablename__ = 'lpressure'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    created_on = Column(DateTime(), default=datetime.now)
    value = Column(String(50), nullable=False)

class Heatbeatrate(Base):
    __tablename__ = 'heatbeatrate'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    created_on = Column(DateTime(), default=datetime.now)
    value = Column(String(50), nullable=False)

Base.metadata.create_all(engine)


