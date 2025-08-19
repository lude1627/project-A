from Modulos.db import conexion
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse

cursor = conexion.cursor()
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def formulario():
    html_content = """
    <html>
    <head>
        <title>Inicio de session</title>
    </head>
    <body>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Username" required><br><br>
            <input type="password" name="password" placeholder="Password" required><br><br>
            <button type="submit">Iniciar session</button>
        </form>
        <button type="button" onclick="location.href='/register'">Registrarse</button>

    </body>
    </html>             
    """
    return HTMLResponse(content=html_content)

@app.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT * FROM usuario WHERE User_name = %s AND User_password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        return HTMLResponse(content=f"<h1>Bienvenido {username}!</h1>")
    else:
        raise HTTPException(status_code=401, detail="Este usuario no existe o la contraseña es incorrecta") 
    

