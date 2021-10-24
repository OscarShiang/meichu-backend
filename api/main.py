from os import SEEK_CUR
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc

from .sql import crud, models, schemas
from .sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def hello():
    return {'Hello World'}

@app.get('/shops/', response_model=List[schemas.Shop])
def read_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops

@app.get('/shops/{shop_id}', response_model=schemas.Shop)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.get_shop(db, shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop

@app.post('/shops/', response_model=bool)
def update_shop_info(shop: schemas.ShopUpdate, db: Session = Depends(get_db)):
    return crud.update_shop(db, shop)

@app.post('/track/', response_model=schemas.Node)
def create_track(track: schemas.Track, db: Session = Depends(get_db)):
    return crud.create_track(db, track)

@app.get('/fsm/{hwid}', response_model=List[schemas.FSM])
def get_fsm(hwid: str, db: Session = Depends(get_db)):
    return crud.get_fsm(db, hwid)

@app.post('/fsm/node', response_model=bool)
def update_fsm(fsm: schemas.FSM, db: Session = Depends(get_db)):
    return crud.update_fsm_node(db, fsm)

@app.get('/stat/relation', response_model=List[schemas.VisitRel])
def get_visit_rel(db: Session = Depends(get_db)):
    return crud.get_visit_relation(db)
