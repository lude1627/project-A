from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Modulos.categoria.logica.auth_consultC import create_cat, all_categories, delete_cat

router = APIRouter()


class CategoryCreate(BaseModel):
    id: int
    name: str


@router.post("/category")
def create_category(data: CategoryCreate):
    if create_cat(data.id, data.name):
        return JSONResponse(content={
            "success": True,
            "message": "Categoría creada exitosamente"
        }, status_code=201)
    else:
        return JSONResponse(content={
            "success": False,
            "message": "Error al crear categoría"
        }, status_code=500)


@router.get("/view_category/data")
def get_category():
    categoria = all_categories()
    if not categoria:  
        return JSONResponse(content=[])
    category_json = [
        {
            "Cat_id": cat[0],
            "Cat_name": cat[1]
        }
        for cat in categoria
    ]
    return JSONResponse(content=category_json)


@router.delete("/category/{id}")
def delete_category(id: int):
    if delete_cat(id):
        return JSONResponse(content={
            "success": True,
            "message": "Categoría eliminada exitosamente"
        })
    else:
        return JSONResponse(content={
            "success": False,
            "message": "Error al eliminar categoría"
        }, status_code=500)
