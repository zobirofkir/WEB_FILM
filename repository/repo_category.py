from Base_Film.model_film import Category
from schemas.schemas import category
from fastapi import HTTPException, status
from Base_Film.data_film import SessionLocal

def created_category(catg:category):
    db = SessionLocal()
    existing_category = db.query(Category).filter(Category.Action==catg.Action).first()
    if existing_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This category has been already existing in this database !')
    else:
        new_category = Category(
            Action =catg.Action,
            Adventure = catg.Adventure,
            Comedy =catg.Comedy,
            Drama =catg.Drama,
            Romance =catg.Romance,
            Thriller =catg.Thriller,
            Horror =catg.Horror,
            Science =catg.Science,
            Fantasy =catg.Fantasy,
            Animation =catg.Animation,
            Documentary =catg.Documentary,
            Mystery =catg.Mystery,
            Historical =catg.Historical,
            Musical =catg.Musical,
            Western =catg.Western
        )

        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return HTTPException(status_code=status.HTTP_201_CREATED, detail='This category has been created !')
    

def get_category(id: int):
    db = SessionLocal()
    geting_category = db.query(Category).filter(Category.id==id).first()
    if geting_category:
        return {'This is the category':[
            {'Action':geting_category.Action},
            {'Adventure':geting_category.Adventure},
            {'Comedy':geting_category.Comedy},
            {'drama':geting_category.Drama},
            {'romance':geting_category.Romance},
            {'Thriller':geting_category.Thriller},
            {'Horror':geting_category.Horror},
            {'science':geting_category.Science},
            {'Fantasy':geting_category.Fantasy},
            {'Animation':geting_category.Animation},
            {'Documentary':geting_category.Documentary},
            {'Mystery':geting_category.Mystery},
            {'Historical':geting_category.Historical},
            {'Musical':geting_category.Musical},
            {'Western':geting_category.Western}
        ]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not found this category !')

def update_category(id:int, cat:category):
    db = SessionLocal()
    updated_category = db.query(Category).filter(Category.id == id).first()
    if updated_category:
        updated_category.Action=cat.Action
        updated_category.Adventure = cat.Adventure
        updated_category.Comedy = cat.Comedy
        updated_category.Drama = cat.Drama
        updated_category.Romance = cat.Romance
        updated_category.Thriller = cat.Thriller
        updated_category.Horror = cat.Horror
        updated_category.Science = cat.Science
        updated_category.Fantasy = cat.Fantasy
        updated_category.Animation = cat.Animation
        updated_category.Documentary = cat.Documentary
        updated_category.Mystery = cat.Mystery
        updated_category.Historical = cat.Historical
        updated_category.Musical = cat.Musical
        updated_category.Western = cat.Western
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail='This category has been updated')
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not found this category')
    
def delete_categiry(id:int):
    db = SessionLocal()
    deleted_category = db.query(Category).filter(Category.id == id).first()
    if deleted_category:
        db.delete(deleted_category)
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail='This category has been deleted seccess ')
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This category Not found !')