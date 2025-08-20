from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from Modulos.Login.logica.auth_consultL import login_user, register_user, update_user, view_user

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def loger():

    with open("Modulos/Login/vista/login.html", "r", encoding= "utf-8") as f:
        return HTMLResponse(content = f.read())

@router.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):
    user = login_user(username, password)
    if user:
        return HTMLResponse(content=f"<script>alert('Bienvenid@ a nuestra tienda {username}'); window.location.href='/updateP';</script>")
    else:
        return HTMLResponse(content="<script>alert('Usuario o contraseña incorrectos'); window.location.href='/';</script>")

@router.get("/register", response_class=HTMLResponse)
def register():
    with open("Modulos/Login/vista/registro.html", "r",  encoding= "utf-8") as f:
        return HTMLResponse(content=f.read())
@router.post("/register", response_class=HTMLResponse)
def register(id: int = Form(...), username: str = Form(...), phone: int = Form(...), email: str = Form(...), password: str = Form(...)):
    if register_user(id, username, phone, email, password):
        return HTMLResponse(content="<script>alert('Usuario registrado exitosamente'); window.location.href='/';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al registrar usuario'); window.location.href='/register';</script>")    
    
@router.get("/updateP/{id}", response_class=HTMLResponse)

def updateP(id:int):
     user = view_user(id)
     if user:
         with open("Modulos/Login/vista/perfil.html", "r", encoding= "utf-8") as f:
             content = f.read()
             content = content.replace("{{username}}", user.username)
             content = content.replace("{{phone}}", str(user.phone))
             content = content.replace("{{email}}", user.email)
             return HTMLResponse(content=content)
     with open("Modulos/Login/vista/perfil.html", "r", encoding= "utf-8") as f:
        return HTMLResponse(content=f.read())
     
@router.post("/updateP", response_class=HTMLResponse)
def updateP(id: int = Form(...), username: str = Form(...), phone: int = Form(...), email: str = Form(...), password: str = Form(...)):
    if update_user(id, username, phone, email, password):
        return HTMLResponse(content="<script>alert('Usuario actualizado exitosamente'); window.location.href='/updateP';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al actualizar usuario'); window.location.href='/updateP';</script>")