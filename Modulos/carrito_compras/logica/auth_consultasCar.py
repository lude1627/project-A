from Modulos.db import conexion

def add_item(articulo: str, precio: float, cantidad: int):
    cursor = conexion.cursor()
    query = "INSERT INTO carrito (articulo, precio, cantidad) VALUES (?, ?, ?)"
    cursor.execute(query, (articulo, precio, cantidad))
    conexion.commit()
    cursor.close()
    return True

def get_items():
    cursor = conexion.cursor()
    query = "SELECT * FROM carrito"
    cursor.execute(query)
    compras = cursor.fetchall()
    cursor.close()
    return compras

def delete_item(item_id: int):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM carrito WHERE id = ?", (item_id,))
    conexion.commit()
    cursor.close()

def get_total():
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM(precio * cantidad) AS total FROM carrito")
    row = cursor.fetchone()
    cursor.close()
    if row and row[0] is not None:
        return row[0]
    return 0
