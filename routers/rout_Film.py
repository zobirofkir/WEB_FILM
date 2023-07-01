from repository.repo_Film import create_Film
from fastapi import APIRouter
from schemas.schemas import film
from repository.repo_Film import get_book
from repository.repo_Film import update_book
from repository.repo_Film import delete_book

route = APIRouter(
    prefix='/api/film',
    tags=['Film']
)

@route.post('/')
def created_film(cat:film):
    return create_Film(cat)

@route.get('/get')
def get(id:int):
    return get_book(id)

@route.put('/update')
def updated(id:int, cato:film):
    return update_book(id, cato)

@route.delete('/delete')
def deletef_book(id:int):
    return delete_book(id)