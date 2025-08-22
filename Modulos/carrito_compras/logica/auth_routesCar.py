from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, JSONResponse
from Modulos.carrito_compras.logica.auth_consultasCar import add_item, get_items, delete_item, conexion

router = APIRouter()


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

@router.get("/cart", response_class=HTMLResponse)
def cart():
    with open("Modulos/carrito_compras/vista/carrito.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
    
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

@router.post("/cart/add", response_class=HTMLResponse)
def añadir_articulo(articulo: str = Form(...), precio: float = Form(...), cantidad: int = Form(...)):
    if add_item(articulo, precio, cantidad):
        return HTMLResponse(content="<script>alert(Articulo agregado)</script>")
    else:
        return HTMLResponse(content="<script>alert(Error al agregar)</script>")
        
@router.delete("/delete_item/{id}")
def delete_item(id: int):
    delete_item
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM carrito WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    return {"message": "Producto eliminado"}


