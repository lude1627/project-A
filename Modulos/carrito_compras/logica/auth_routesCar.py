from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from Modulos.carrito_compras.logica.auth_consultasCar import add_item, get_items, delete_item, get_total

router = APIRouter()

@router.get("/cart", response_class=HTMLResponse)
def cart():
    with open("Modulos/carrito_compras/vista/carrito.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Endpoint JSON con lista del carrito
@router.get("/cart/list")
def listar_carrito():
    prod_cart = get_items()
    return JSONResponse(content= prod_cart)

@router.post("/cart/add", response_class=HTMLResponse)
def añadir_articulo(articulo: str = Form(...), precio: float = Form(...), cantidad: int = Form(...)):
    if add_item(articulo, precio, cantidad):
        return HTMLResponse(content="<script>alert(Articulo agregado)</script>")
    else:
        return HTMLResponse(content="<script>alert(Error al agregar)</script>")
        
@router.get("/cart/delete/", response_class=HTMLResponse)
def eliminar_articulo(item_id: int):
    if delete_item(item_id):
        return HTMLResponse(content="<script>alert(articulo eliminado correctamente)</script>")
    else:
        return HTMLResponse(content="<script>alert(Error no se elimino)</script>")

