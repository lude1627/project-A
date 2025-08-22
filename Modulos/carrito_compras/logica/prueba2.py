from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Producto(BaseModel):
    id: int
    articulo: str
    precio: float
    cantidad: int

# Agregar al carrito
@app.post("/add_to_cart")
def add_to_cart(producto: Producto):
    conexion = sqlite3.connect("carrito.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO carrito (articulo, precio, cantidad) VALUES (?, ?, ?)",
                   (producto.articulo, producto.precio, producto.cantidad))
    conexion.commit()
    conexion.close()
    return {"message": f"{producto.articulo} agregado al carrito"}

# Ver carrito
@app.get("/cart")
def ver_carrito():
    conexion = sqlite3.connect("carrito.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT articulo, precio, cantidad FROM carrito")
    items = cursor.fetchall()
    conexion.close()
    return [{"articulo": i[0], "precio": i[1], "cantidad": i[2]} for i in items]
