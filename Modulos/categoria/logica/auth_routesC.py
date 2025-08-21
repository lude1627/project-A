from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from Modulos.categoria.logica.auth_consultC import create_cat, view_cat, delete_cat

router = APIRouter()

@router.get("/category", response_class=HTMLResponse)
def categories():
    with open("Modulos/categoria/vista/categorias.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
    
@router.post("/category", response_class=HTMLResponse)
def create_category(id: int = Form(...), name: str = Form(...)):
    if create_cat(id, name):
        return HTMLResponse(content="<script>alert('Categoría creada exitosamente'); window.location.href='/category';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al crear categoría'); window.location.href='/category';</script>")    

#buscando opcion de llamar los datos de la tabla categorias
@router.get("/category", response_class=HTMLResponse)
def mostrar_categorias():
    categorias = view_cat()

    if not categorias:
        return "<h2>No hay categorías registradas</h2>"

    # Construimos la lista HTML
    content = "<h2>Lista de Categorías</h2><ul>"
    for cat in categorias:
        content += f"<li>ID: {cat['Cat_id']} | Nombre: {cat['Cat_name']}</li>"
    content += "</ul>"

    return content

@router.get("/category/delete", response_class=HTMLResponse)
def delete_category(id: int):
    if delete_cat(id):
        return HTMLResponse(content="<script>alert('Categoría eliminada exitosamente'); window.location.href='/category/view';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al eliminar categoría'); window.location.href='/category/view';</script>")