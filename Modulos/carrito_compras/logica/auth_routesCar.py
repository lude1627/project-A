from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from Modulos.carrito_compras.logica.auth_consultasCar import get_items

router = APIRouter()

@router.get("/view_carrito", response_class=HTMLResponse)
def view_product_page():
    with open("Modulos/carrito_compras/vista/carrito.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@router.get("/view_carrito/data")
def get_carricto():
    carrito = get_items()
    carrito_json = [
        {
            "Car_id": c[0],
            "User_id": c[1],
            "User_name": c[2],
            "Product_id": c[3],
            "Product_name": c[4],
            "Car_cantidad": c[5],
            "Product_price": c[6],
            "Car_subTotal": c[7],
        }
        for c in carrito
    ]
    return JSONResponse(content=carrito_json)