from fastapi import FastAPI
from Modulos.Login.logica import auth_routes

app = FastAPI()

app.include_router(auth_routes.router)