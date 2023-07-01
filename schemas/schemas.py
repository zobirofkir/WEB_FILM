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

