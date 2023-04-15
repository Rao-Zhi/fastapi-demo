from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.mysql import SessionLocal, engine

# from fastapi.models.user import user as models
from models import user as models
from schemas import user as schemas
from curd import user as curd

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
def read_users(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    list, total = curd.get_users(db, skip=skip, limit=limit)
    return {"code":200, "usersList":list, "total":total}

@router.post("/add")
def add_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = curd.add_user(db, user)
    return {"code":200, "user":db_user}

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = curd.delete_user(db, user_id)
    return {"code":200, "user":db_user}