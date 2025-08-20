from fastapi import FastAPI
from Modulos.Login.logica import auth_routesL

app = FastAPI()

app.include_router(auth_routesL.router)