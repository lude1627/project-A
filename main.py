from fastapi import FastAPI
from Modulos.Login.logica import auth_routesL
from Modulos.productos.logica import auth_routesP

app = FastAPI()

app.include_router(auth_routesL.router)
app.include_router(auth_routesP.router)
