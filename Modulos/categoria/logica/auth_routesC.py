from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, JSONResponse
from Modulos.categoria.logica.auth_consultC import create_cat,all_categories , delete_cat

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

    
@router.get("/view_category/data")
def get_category():
    categoria = all_categories()
    if not categoria:  # si no hay categorías
        return JSONResponse(content=[{
            "Cat_id": 0,
            "Cat_name": "Sin categorías disponibles"
        }])
    category_json = [
        {
            "Cat_id": cat[0],
            "Cat_name": cat[1]
        }
        for cat in categoria
    ]
    return JSONResponse(content=category_json)


    


@router.get("/category/delete", response_class=HTMLResponse)
def delete_category(id: int):
    if delete_cat(id):
        return HTMLResponse(content="<script>alert('Categoría eliminada exitosamente'); window.location.href='/category/view';</script>")
    else:
        return HTMLResponse(content="<script>alert('Error al eliminar categoría'); window.location.href='/category/view';</script>")