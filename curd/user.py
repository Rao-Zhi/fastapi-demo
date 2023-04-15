from sqlalchemy.orm import Session

from models import user as models
from schemas import user as schemas

def get_users(db: Session, skip: int = 1, limit: int = 10):
    offset = (skip -1) * limit;
    list,total = db.query(models.User).offset(offset).limit(limit).all(),db.query(models.User).count()
    return list,total
        
def add_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, account=user.account, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user