from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Shop(Base):
    # TABLE shop (shop_id INT PRIMARY KEY,              name TEXT, location TEXT, category TEXT, luxury INT, people_in_shop INT,            opening_hours TEXT, description TEXT, commodity TEXT);

    __tablename__ = 'shop'

    shop_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    category = Column(String)
    luxury = Column(Integer, default=0)
    people_in_shop = Column(Integer, default=0)
    opening_hours = Column(String)
    description = Column(String, default='')
    commodity = Column(String, default='')
    phone_num = Column(String, default='')
    icon = Column(String, default='')

class Track(Base):
    # track (track_id INT PRIMARY KEY,             user_id INT, visit_id INT, last_track_id INT, user_gender TEXT,            user_age INT, user_occupation TEXT);

    __tablename__ = 'track'

    track_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    visit_id = Column(Integer)
    last_track_id = Column(Integer)
    user_gender = Column(String)
    user_age = Column(Integer)
    user_occupation = Column(String)
    timestamp = Column(DateTime)

class Node(Base):
    __tablename__ = 'node'

    node_id = Column(Integer, primary_key=True, index=True)
    hwid = Column(String, index=True)
    action = Column(String, default='')
    trigger = Column(String, default='')
    parent_id = Column(Integer)

class FSM(Base):
    __tablename__ = 'fsm'

    hwid = Column(String, primary_key=True)
    node_id = Column(String)
    data = Column(String)
