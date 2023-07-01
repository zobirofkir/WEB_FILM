from Base_Film.data_film import SessionLocal
from Base_Film.model_film import Publisher
from schemas.schemas import publisher
from fastapi import HTTPException, status

def create_publisher(cate:publisher):
    db = SessionLocal()
    existing_publisher = db.query(Publisher).filter(Publisher.name_publisher==cate.name_publisher).first()
    if existing_publisher:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This publisher has been already existing in this database !')
    else:
        new_publisher = Publisher(name_publisher=cate.name_publisher, email=cate.email, bio=cate.bio, country=cate.country)
        db.add(new_publisher)
        db.commit()
        db.refresh(new_publisher)
        return HTTPException(status_code=status.HTTP_201_CREATED, detail='This publisher has ben created success ')
    
def get_publisher(id:int):
    db = SessionLocal()
    geting_publisher = db.query(Publisher).filter(Publisher.id == id).first()
    if geting_publisher:
        return {'this is all publisher':[
            {'name_publisher':geting_publisher.name_publisher},
            {'email':geting_publisher.email},
            {'bio':geting_publisher.bio},
            {'country':geting_publisher.country}
        ]}
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not found this publisher !')


def update_publisher(id:int, cat:publisher):
    db = SessionLocal()
    updated_publisher = db.query(Publisher).filter(Publisher.id==id).first()
    if updated_publisher:
        updated_publisher.name_publisher=cat.name_publisher
        updated_publisher.email = cat.email
        updated_publisher.bio = cat.bio
        updated_publisher.country = cat.country
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail='This publisher has been updated')
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This publisher not found !')
    
def deletd_publidher(id:int):
    db = SessionLocal()
    deleting_publisher = db.query(Publisher).filter(Publisher.id==id).first()
    if deleting_publisher:
        db.delete(deleting_publisher)
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail='This publisher has been deleted ')
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This publisher not found !')
