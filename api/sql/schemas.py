from typing import List, Optional

from pydantic import BaseModel

class Track(BaseModel):
    track_id: int
    user_id: int
    visit_id: int
    last_track_id: int
    user_gender: str
    user_age: int
    user_occupation: str
    class Config:
        orm_mode = True

class ShopUpdate(BaseModel):
    name: str
    location: str
    category: str
    opening_hours: str
    description: str
    phone_num: str
    class Config:
        orm_mode = True

class Shop(BaseModel):
    shop_id: int
    name: str
    location: str
    category: str
    luxury: int
    people_in_shop: int
    opening_hours: str
    description: str
    commodity: str
    phone_num: str
    icon: str
    class Config:
        orm_mode = True

class NodeCreate(BaseModel):
    hwid: str
    action: str
    trigger: str
    parent_id: int
    # class Config:
    #     orm_mode = True

class Node(BaseModel):
    node_id: int
    hwid: str
    action: str
    trigger: str
    parent_id: int
    class Config:
        orm_mode = True

class FSM(BaseModel):
    hwid: str
    node_id: str
    data: str
    class Config:
        orm_mode = True

class VisitRel(BaseModel):
    visit_1: int
    visit_2: int
