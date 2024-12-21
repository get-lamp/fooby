from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.globals import app
from . import crud, models, schemas
from .database import engine, get_db_session

assert app is not None, 'App is not initialized'

models.Base.metadata.create_all(bind=engine)


@app.get("/healthcheck/")
def healthcheck(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    return 'OK'


@app.post("/users/", response_model=schemas.User)
def create_item(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_item(user_id: int, db: Session = Depends(get_db_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
