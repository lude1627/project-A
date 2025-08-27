from fastapi import APIRouter, Form, HTTPException
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
            "id": c[0],
            "nombre": c[1],
            "descripcion": c[2],
            "cantidad": c[3],
            "precio": c[4],
            "categoria": c[5]
        }
        for c in carrito
    ]
    return JSONResponse(content=carrito_json)