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
        <title>Formulario de categoria</title>
    </head>
    <body>
        <form action="/register" method="post">
            <input type="text" name="username" placeholder="Categoria" required><br><br>
            <button type="submit">Crear</button>
            <button type="submit">Editar</button>
        </form>
    </body>
    </html>             
    """
    return HTMLResponse(content=html_content)