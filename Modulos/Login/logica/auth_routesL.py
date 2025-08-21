from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from Modulos.Login.logica.auth_consultL import login_user, register_user, update_user, view_user

router = APIRouter()


# ---------------- LOGIN ----------------
@router.get("/", response_class=HTMLResponse)
def loger():
    with open("Modulos/Login/vista/login.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@router.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):
    user = login_user(username, password)
    if user:
        user_id = user[0]  # asumimos que User_id es el primer campo
        return HTMLResponse(content=f"<script>alert('Bienvenid@ {username}'); window.location.href='/updateP?id={user_id}';</script>")
    else:
        return HTMLResponse(content="<script>alert('Usuario o contraseña incorrectos'); window.location.href='/';</script>")


# ---------------- REGISTER ----------------
@router.get("/register", response_class=HTMLResponse)
def register():
    with open("Modulos/Login/vista/registro.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@router.post("/register", response_class=HTMLResponse)
def register(id: int = Form(...), username: str = Form(...), phone: int = Form(...), email: str = Form(...), password: str = Form(...)):
    if register_user(id, username, phone, email, password):
        return HTMLResponse(content="<script>alert('Usuario registrado exitosamente'); window.location.href='/';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al registrar usuario'); window.location.href='/register';</script>")    


# ---------------- PERFIL ----------------
@router.get("/updateP", response_class=HTMLResponse)
def get_user(id: int):
    user = view_user(id)  # trae los datos desde la base de datos

    if not user:
        return HTMLResponse(content="<h1>Usuario no encontrado</h1>")

    user_dict = {
        "id": user[0],
        "nombre": user[1],
        "telefono": user[2],
        "correo": user[3],
        "password": user[4]
    }

    with open("Modulos/Login/vista/perfil.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    for key, value in user_dict.items():
        html_content = html_content.replace(f"{{{key}}}", str(value))

    return HTMLResponse(content=html_content)



@router.post("/updateP", response_class=HTMLResponse)
def updateP(id: int = Form(...), username: str = Form(...), phone: int = Form(...), email: str = Form(...), password: str = Form(...)):
    if update_user(id, username, phone, email, password):
        return HTMLResponse(content=f"<script>alert('Usuario actualizado exitosamente'); window.location.href='/updateP?id={id}';</script>")
    else:
        return HTMLResponse(content=f"<script>alert('Error al actualizar usuario'); window.location.href='/updateP?id={id}';</script>")
