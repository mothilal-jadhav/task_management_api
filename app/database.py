from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


database_url = "mysql+pymysql://root:mothilal%4012@127.0.0.1:3306/Task_management_system"

engine = create_engine(database_url)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        