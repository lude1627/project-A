from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Modulos.Login.logica import auth_routesL
from Modulos.categoria.logica import auth_routesC
from Modulos.productos.logica import auth_routesP
from Modulos.carrito_compras.logica import auth_routesCar

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["https://project-a-2.pages.dev"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
app.include_router(auth_routesL.router)
app.include_router(auth_routesC.router)
app.include_router(auth_routesP.router)
app.include_router(auth_routesCar.router)
