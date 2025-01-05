from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import status
from app import schemas, crud
from dependencies import get_db_session

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db_session)]


@router.post("/users/", response_model=schemas.User)
def create_user(db: db_dependency, user: schemas.UserCreate):
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(db: db_dependency, user_id: int):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return db_user


@router.get("/users/", response_model=list[schemas.User])
def read_users(db: db_dependency, skip: int = 0, limit: int = 10):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
