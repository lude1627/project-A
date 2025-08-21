from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from Modulos.categoria.logica.auth_consultC import create_cat, view_cat, delete_cat

router = APIRouter()

@router.get("/category", response_class=HTMLResponse)
def categories():
    with open("Modulos/categoria/vista/categorias.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
    
@router.post("/category/create", response_class=HTMLResponse)
def create_category(id: int = Form(...), name: str = Form(...)):
    if create_cat(id, name):
        return HTMLResponse(content="<script>alert('Categoría creada exitosamente'); window.location.href='/category';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al crear categoría'); window.location.href='/category';</script>")    

@router.get("/category/view", response_class=HTMLResponse)
def view_categories():
    categories = view_cat()
    rows = ""
    if categories:
        for cat in categories:
            rows += f"""
            <tr>
                <td>{cat['Cat_id']}</td>
                <td>{cat['Cat_name']}</td>
                <td><a href='/category/delete?id={cat['Cat_id']}'>Eliminar</a></td>
            </tr>
            """
    else:
        rows = "<tr><td colspan='3'>No hay categorías disponibles</td></tr>"

    with open("Modulos/categoria/vista/categorias.html", "r", encoding="utf-8") as f:
        html_content = f.read().replace("{{categorias}}", rows)

    return HTMLResponse(content=html_content)

@router.get("/category/delete", response_class=HTMLResponse)
def delete_category(id: int):
    if delete_cat(id):
        return HTMLResponse(content="<script>alert('Categoría eliminada exitosamente'); window.location.href='/category/view';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al eliminar categoría'); window.location.href='/category/view';</script>")