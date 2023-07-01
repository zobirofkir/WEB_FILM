from fastapi import FastAPI
from Authentication.Authentication import rour
from routers.rout_Film import route
from routers.route_publisher import routr
from routers.rout_category import rout

app = FastAPI()


app.include_router(rour)
app.include_router(route)
app.include_router(routr)
app.include_router(rout)