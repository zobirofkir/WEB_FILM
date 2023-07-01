from repository.repo_category import created_category, get_category, update_category, delete_categiry
from fastapi import APIRouter
from schemas.schemas import category

rout = APIRouter(
    prefix='/api/category',
    tags=['Category']
)

@rout.post('/')
def create_category(catg:category):
    return created_category(catg)

@rout.get('/get')
def geting(id:int):
    return get_category(id)

@rout.put('/update')
def updated(id:int, cat:category):
    return update_category(id, cat)

@rout.delete('/deleted')
def deleted_cat(id:int):
    return delete_categiry(id)