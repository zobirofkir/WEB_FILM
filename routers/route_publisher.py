from repository.repo_publisher import create_publisher, get_publisher, update_publisher, deletd_publidher
from fastapi import APIRouter
from schemas.schemas import publisher

routr = APIRouter(
    prefix='/api/publosher',
    tags=['Publisher']
)

@routr.post('/')
def creating_publisher(cate:publisher):
    return create_publisher(cate)

@routr.get('/get')
def gete_publisher(id:int):
    return get_publisher(id)

@routr.put('/update')
def updated_publidher(id:int, cat:publisher):
    return update_publisher(id, cat)

@routr.delete('/delete')
def deleted_publisher(id:int):
    return deletd_publidher(id)