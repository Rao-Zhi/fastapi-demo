from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/wind"
#连接本地mysql数据库
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False
)
#创建一个sessionmaker对象
SessionLocal = sessionmaker(bind=engine)

#创建一个基类
Base = declarative_base()