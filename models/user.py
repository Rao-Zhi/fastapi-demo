from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.mysql import Base

# Path: app/sql/models.py
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    account = Column(String(50))
    password = Column(String(50))

    # items = relationship("Item", back_populates="owner")