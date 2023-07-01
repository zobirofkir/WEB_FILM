from fastapi import FastAPI
from Authentication.Authentication import rour
app = FastAPI()


app.include_router(rour)