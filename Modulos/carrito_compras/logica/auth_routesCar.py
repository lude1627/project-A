from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from Modulos.carrito_compras.logica.auth_consultasCar import add_item, get_items, delete_item, get_total

router = APIRouter()

# Endpoint JSON con lista del carrito
@router.get("/cart/list", response_class=JSONResponse)
def lista_carrito():
    items = get_items()
    total = get_total()
    return JSONResponse(content={"Info": f"✅  {items}"})

@router.post("/cart/add")
def añadir_articulo(articulo: str = Form(...), precio: float = Form(...), cantidad: int = Form(...)):
    add_item(articulo, precio, cantidad)
    #return RedirectResponse(url="/cart", status_code=303)
    return JSONResponse(content={"message": f"✅ Artículo  {articulo} agregado correctamente"})

@router.get("/cart/delete/{item_id}")
def eliminar_articulo(item_id: int):
    delete_item(item_id)  # Aquí borras el item
    return JSONResponse(content={"message": f"✅ Artículo con ID {item_id} eliminado correctamente"})

