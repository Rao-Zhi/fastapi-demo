from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.sql import crud, models, schemas
from app.sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=["users"],
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
    list, total = crud.get_users(db, skip=skip, limit=limit)
    return {"code":200, "usersList":list, "total":total}

@router.post("/add")
def add_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.add_user(db, user)
    return {"code":200, "user":db_user}

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    return {"code":200, "user":db_user}