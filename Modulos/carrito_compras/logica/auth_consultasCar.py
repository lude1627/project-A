import sqlite3
from Modulos.db import conexion

def get_items():
    cursor = conexion.cursor()
    query = """ 
        SELECT 
            c.Car_id,
            u.User_id,
            u.User_name,
            p.Product_id,
            p.Product_name,
            c.Car_Cantidad,
            p.Product_price AS precio,
            (c.Car_Cantidad * p.Product_price) AS subtotal
        FROM carrito c
        JOIN productos p ON c.Product_id = p.Product_id
        JOIN usuario u ON c.User_id = u.User_id;
        """
    cursor.execute(query)
    carrito = cursor.fetchall()
    cursor.close()
    return carrito

