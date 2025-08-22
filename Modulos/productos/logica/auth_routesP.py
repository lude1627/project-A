#rutaspara la creacion y para la vista de productos
from fastapi import APIRouter, Form
from Modulos.productos.logica.auth_consultP import create_product,all_categories,all_products, delete_product
 
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()

@router.get("/create_product", response_class=HTMLResponse)
def create():
    with open("Modulos/productos/view/create_product.html", "r", encoding="utf-8") as f:
        html = f.read()

    # obtener categorías desde BD
    categorias = all_categories()

    # construir las opciones <option>
    options = '<option value="">Seleccione una categoria</option>'
    for c in categorias:
        options += f'<option value="{c[0]}">{c[1]}</option>'

    # reemplazar dentro del <select>
    html = html.replace(
        '<option value="">Seleccione una categoria</option>',
        options
    )

    return HTMLResponse(content=html)




@router.post("/create_product", response_class=HTMLResponse)
def create_product_route(
    name: str = Form(...),
    description: str = Form(...),
    cant: int = Form(...),
    price: float = Form(...),
    category_id: int = Form(...)
):
    if create_product(name, description, cant, price, category_id):
        return HTMLResponse(
            content="<script>alert('Producto creado exitosamente');window.location.href='/view_product';</script>",
            status_code=200
        )
    else:
        return HTMLResponse(content="<script>alert('Error al crear el producto');</script>", status_code=500)


@router.get("/view_product", response_class=HTMLResponse)
def view_product():
    with open("Modulos/productos/view/view_product.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@router.get("/view_product/data")
def get_products():
    products = all_products()
    productos_json = [
        {
            "id": p[0],
            "nombre": p[1],
            "descripcion": p[2],
            "cantidad": p[3],
            "precio": p[4],
            "categoria": p[5]
        }
        for p in products
    ]
    return JSONResponse(content=productos_json)

@router.delete("/delete/{id}")
def deleteP(id: int):
    delete_product(id)
  
    return {"message": "Producto eliminado con éxito"}