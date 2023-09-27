from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Companion(Base):
    __tablename__ = 'companions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String, unique=True, index=True)
    level = Column(Integer, default=1)
    strength = Column(Integer, default=5)
    defense = Column(Integer, default=5)
    speed = Column(Integer, default=5)
    HP = Column(Integer, default=10)
    image = Column(String)
    type = Column(String)
    training_end_time = Column(DateTime, default=None)
    chosen_stat = Column(String, default=None)