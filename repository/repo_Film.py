from Base_Film.model_film import Film
from Base_Film.data_film import SessionLocal
from schemas.schemas import film
from fastapi import HTTPException, status


def create_Film(cat:film):
    db = SessionLocal()
    existing_film = db.query(Film).filter(Film.name==cat.name).first()
    if existing_film:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This film has been already existing in this database !')
    else:
        new_film = Film(name=cat.name, Publication_year = cat.Publication_year, the_quality=cat.the_quality, Country=cat.Country, the_language=cat.the_language, Type=cat.Type, Precision=cat.Precision, Release_Date=cat.Release_Date, the_show_length=cat.the_show_length, comment = cat.comment)
        db.add(new_film)
        db.commit()
        db.refresh(new_film)
        return {'created':'this film has been created '}


def get_book(id:int):
    db = SessionLocal()
    geting_film = db.query(Film).filter(Film.id==id).first()
    if geting_film:
        return {'This is all film':[
            {'film name':geting_film.name},
            {'film publication':geting_film.Publication_year},
            {'film quality':geting_film.the_quality},
            {'film contry':geting_film.Country},
            {'film language':geting_film.the_language},
            {'film type':geting_film.Type},
            {'film':geting_film.Precision},
            {'film release_date':geting_film.Release_Date},
            {'film the_show_length':geting_film.the_show_length},
            {'film comment':geting_film.comment}
        ]}
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This film not existing in this database !')
    



def update_book(id:int, cato:film):
    db = SessionLocal()
    updated_film = db.query(Film).filter(Film.id == id).first()
    if updated_film:
        updated_film.name=cato.name
        updated_film.Publication_year = cato.Publication_year
        updated_film.the_quality = cato.the_quality
        updated_film.Country = cato.Country
        updated_film.the_language = cato.the_language
        updated_film.Type = cato.Type
        updated_film.Precision = cato.Precision
        updated_film.Release_Date = cato.Release_Date
        updated_film.the_show_length = cato.the_show_length
        updated_film.comment = cato.comment
        return {'updated':'This film is updated'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This film not fount !')
    

def delete_book(id:int):
    db = SessionLocal()
    deleting_film = db.query(Film).filter(Film.id==id).first()
    if deleting_film:
        db.delete(deleting_film)
        db.commit()
        return {'deleted':'this film has been deleted success'}
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not found this film !')
