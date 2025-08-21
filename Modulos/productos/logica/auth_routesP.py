#rutaspara la creacion y para la vista de productos
from fastapi import APIRouter, Form
from Modulos.productos.logica.auth_consultP import create_product, view_product, all_products, update_product, delete_product  
from fastapi.responses import HTMLResponse

router = APIRouter()


