#rutaspara la creacion y para la vista de productos
from fastapi import APIRouter, Form
from Modulos.productos.logica.auth_consultP import create_product, view_product, all_products, update_product, delete_product  
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/create_product",response_class= HTMLResponse)
def create():
    with open("Modulos/productos/view/create_product.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@router.post("/create_product", response_class=HTMLResponse)
def create_product_route(name: str = Form(...), description: str = Form(...), cant: int = Form(...), price: float = Form(...)):
    
    if create_product(name, description, cant, price):
        return HTMLResponse(content="<script>alert('Producto creado exitosamente');</script>", status_code=200)
    else:
        return HTMLResponse(content="<script>alert('Error al crear el prducto');</script> ", status_code=500)



 