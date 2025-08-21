from Modulos.db import conexion

def create_product(name: str, description: str, cant: int, price: float):
    cursor = conexion.cursor()
    query = "INSERT INTO producto (Product_name, Product_description Product_cant, Product_price) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, description, cant, price))
    conexion.commit()
    cursor.close()
    return True

def view_product(id: int):
    cursor = conexion.cursor()
    query = "SELECT * FROM producto WHERE Product_id = %s"
    cursor.execute(query, (id,))
    product = cursor.fetchone()
    cursor.close()
    return product

def all_products():
    cursor = conexion.cursor()
    query = "SELECT * FROM producto"
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    return products

def update_product(id: int, name: str, description: str, cant: int, price: float):
    cursor = conexion.cursor()
    query = "UPDATE producto SET Product_name = %s, Product_description = %s, Product_cant = %s, Product_price = %s WHERE Product_id = %s"
    cursor.execute(query, (name, description, cant, price, id))
    conexion.commit()
    cursor.close()
    return True

def delete_product(id: int):
    cursor = conexion.cursor()
    query = "DELETE FROM producto WHERE Product_id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    cursor.close()
    return True
