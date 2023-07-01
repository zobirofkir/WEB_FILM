from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from data_film import Base, engine

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    Publication_year = Column(String, nullable=False)
    the_quality = Column(String, nullable=False) 
    Country = Column(String, nullable=False)
    the_language = Column(String, nullable=False)
    Type = Column(String, nullable=False)
    Precision = Column(String, nullable=False)
    Release_Date = Column(Integer, nullable=False)
    the_show_length = Column(String, nullable=False)
    comment = Column(String, nullable=False)

    category = relationship('Category', back_populates='films')

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name_publisher = Column(String, nullable=False)
    email = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    country = Column(String, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    Action = Column(String, nullable=False)
    Adventure = Column(String, nullable=False)
    Comedy = Column(String, nullable=False)
    Drama = Column(String, nullable=False)
    Romance = Column(String, nullable=False)
    Thriller = Column(String, nullable=False)
    Horror = Column(String, nullable=False)
    Science = Column(String, nullable=False)
    Fantasy = Column(String, nullable=False)
    Animation = Column(String, nullable=False)
    Documentary = Column(String, nullable=False)
    Mystery = Column(String, nullable=False)
    Historical = Column(String, nullable=False)
    Musical = Column(String, nullable=False)
    Western = Column(String, nullable=False)

    films = relationship('Film', back_populates='category')
 
Base.metadata.create_all(bind=engine)
