from Modulos.db import conexion
from fastapi import FastAPI,Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse 

cursor = conexion.cursor()
app = FastAPI()

@app.get("/" , response_class=HTMLResponse)
def formulario():

    html_conntent = """
    <html>
    <head>
        <title>Register</title>
        </head>
        <body>
            <form action="/register" method="post">
                Cedula: <input type="number" name="id" placeholder="Cedula" required><br><br>
                Nombre: <input type="text" name="username" placeholder="Nombre completo" required><br><br>
                Telefono: <input type="number" name=phone placeholder="Celular" required><br><br>
                Correo: <input type="email" name="email" placeholder="Correo electronico" required><br><br>
                Contraseña: <input type="password" name="password" placeholder="Contraseña" required><br><br>
                <button type="submit">Register</button>
            </form>
        </body>
    </html>             
            """
    return HTMLResponse(content=html_conntent)

@app.post("/register", response_class=HTMLResponse)
def register(id: int = Form(...),username: str = Form(...), phone: int = Form(...), email: str = Form(...), password: str = Form(...)):
    try:
        # verificar que el id existe
        cursor.execute("SELECT * FROM usuario WHERE User_Id = %s", (id,))
        existe= cursor.fetchone()

        if existe: 
            return HTMLResponse(content="<script>alert('El ID ya existe.'); window.location.href='/';</script>")

        cursor.execute("INSERT INTO usuario (User_Id, User_name, User_phone, User_mail, User_password) VALUES (%s,%s, %s, %s, %s)", (id,username, phone, email, password))
        conexion.commit()
        return HTMLResponse(content="<script>alert('Registro exitoso!'); window.location.href='/';</script>")
       # return HTMLResponse(content="<h1>Registro exitoso!</h1>")
    except Exception as e:
        conexion.rollback()
        raise HTTPException(status_code=500, detail=str(e))
