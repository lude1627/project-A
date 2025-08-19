from fastapi import FastAPI
from session import router as session_router
from register import router as register_router

app = FastAPI()

# Incluye los routers de los otros archivos para que todas las rutas sean accesibles
app.include_router(session_router)
app.include_router(register_router)