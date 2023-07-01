from pydantic import BaseModel

class Users(BaseModel):
    username:str
    email:str
    password:str

class Afficher_Users(BaseModel):
    username:str
    email:str
    password:str

    class config():
        orm_mode=True


class film(BaseModel):
    name :str
    Publication_year :str
    the_quality :str 
    Country :str
    the_language :str
    Type :str
    Precision :str
    Release_Date :int
    the_show_length :str
    comment :str

class publisher(BaseModel):
    name_publisher : str
    email : str
    bio : str
    country : str



class category(BaseModel):
    Action :str
    Adventure :str
    Comedy :str
    Drama :str
    Romance :str
    Thriller :str
    Horror :str
    Science :str
    Fantasy :str
    Animation :str
    Documentary :str
    Mystery :str
    Historical :str
    Musical :str
    Western :str
