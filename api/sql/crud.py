from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_shops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shop).offset(skip).limit(limit).all()

def get_shop(db: Session, shop_id: int):
    return db.query(models.Shop).filter(models.Shop.shop_id == shop_id).first()

def update_shop(db: Session, shop: schemas.Shop):
    db.query(models.Shop).filter(models.Shop.name == shop.name).update({
        'location': shop.location,
        'category': shop.category,
        'opening_hours': shop.opening_hours,
        'description': shop.description,
        'phone_num': shop.phone_num
    })
    db.commit()
    return True

def create_track(db: Session, track: schemas.Track):
    db_track = track
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

def get_fsm(db: Session, hwid: str):
    q = f'SELECT * FROM fsm WHERE fsm.hwid == "{hwid}";'
    return db.execute(q).all()

def update_fsm_node(db: Session, node: schemas.FSM):
    db_node = db.query(models.FSM).filter(and_(models.FSM.hwid == node.hwid, models.FSM.node_id == node.node_id)).first()
    if db_node:
        db.query(models.FSM).filter(and_(models.FSM.hwid == node.hwid, models.FSM.node_id == node.node_id)).update({'data': node.data})
        db.commit()
    else:
        db_node = models.FSM(hwid=node.hwid, node_id=node.node_id, data=node.data)
        db.add(db_node)
        db.commit()
        db.refresh(db_node)
    return True

def get_visit_relation(db: Session):
    q = 'SELECT t2.visit_id as visit_1, t1.visit_id as visit_2 FROM track as t1 INNER JOIN track as t2 ON t1.last_track_id = t2.track_id;'
    return db.execute(q).all()
