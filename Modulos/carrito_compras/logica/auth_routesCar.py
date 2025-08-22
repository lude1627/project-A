from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from Modulos.carrito_compras.logica.auth_consultasCar import get_items, eliminar_producto_db, conexion

router = APIRouter()

@router.get("/cart", response_class=HTMLResponse)
def cart():
    with open("Modulos/carrito_compras/vista/carrito.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

def fetch_items_from_db():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM carrito")
    items = cursor.fetchall()
    cursor.close()
    return items

@router.get("/cart/list/data")
def get_items():
    carrito = fetch_items_from_db()
    return carrito


    
@router.get("/cart/list/data")
def get_items():
    carrito = get_items()
    carritos_json = [
        {
            "id": c[0],
            "articulo": c[1],
            "precio": c[2],
            "cantidad": c[3],          
        }
        for c in carrito
    ]
    return JSONResponse(content=carritos_json)
     
@router.delete("/productos/eliminar/{id}")
def eliminar_producto(id: int):
    eliminado = eliminar_producto_db(id)
    if eliminado:
        return {"msg": f"Producto {id} eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")


