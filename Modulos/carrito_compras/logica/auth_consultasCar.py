import sqlite3
from Modulos.db import conexion

def get_items():
    cursor = conexion.cursor()
    query = "SELECT * FROM carrito"
    cursor.execute(query)
    carrito = cursor.fetchall()
    cursor.close()
    return True

def eliminar_producto_db(id: int) -> bool:
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = %s" 
        cursor.execute
        conexion.commit()
        eliminado = cursor.rowcount > 0  
        conexion.close()
        return eliminado
    except Exception as e:
        print("Error al eliminar:", e)
        return False

