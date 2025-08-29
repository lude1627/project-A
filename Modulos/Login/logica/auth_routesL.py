from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Modulos.Login.logica.auth_consultL import login_user, register_user, update_user, view_user

router = APIRouter()


class LoginModel(BaseModel):
    username: str
    password: str

class RegisterModel(BaseModel):
    id: int
    username: str
    phone: int
    email: str
    password: str

class UpdateUserModel(BaseModel):
    id: int
    username: str
    phone: int
    email: str
    password: str



@router.post("/login")
def login(data: LoginModel):
    user = login_user(data.username, data.password)
    if user:
        user_id = user[0]
        return JSONResponse(content={
            "success": True,
            "message": f"Bienvenid@ {data.username}",
            "user_id": user_id
        })
    else:
        return JSONResponse(content={
            "success": False,
            "message": "Usuario o contraseña incorrectos"
        })


@router.post("/register")
def register(data: RegisterModel):
    if register_user(data.id, data.username, data.phone, data.email, data.password):
        return JSONResponse(content={
            "success": True,
            "message": "Usuario registrado exitosamente"
        })
    else:
        return JSONResponse(content={
            "success": False,
            "message": "Error al registrar usuario"
        })


@router.get("/get_user/{id}")
def get_user_json(id: int):
    user = view_user(id)
    if not user:
        return JSONResponse(content={"error": "Usuario no encontrado"}, status_code=404)
    return JSONResponse(content={
        "id": user[0],
        "username": user[1],
        "phone": user[2],
        "email": user[3],
        "password": user[4]
    })


@router.post("/updateP")
def updateP(data: UpdateUserModel):
    if update_user(data.id, data.username, data.phone, data.email, data.password):
        return JSONResponse(content={
            "success": True,
            "message": "Usuario actualizado exitosamente"
        })
    else:
        return JSONResponse(content={
            "success": False,
            "message": "Error al actualizar usuario"
        })
