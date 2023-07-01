from .database import Base, engine
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__='Authentication'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)