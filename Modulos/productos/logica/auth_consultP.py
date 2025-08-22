from Modulos.db import conexion


def view_product(id: int):
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE Product_id = %s"
    cursor.execute(query, (id,))
    product = cursor.fetchone()
    cursor.close()
    return product

def all_products():
    cursor = conexion.cursor()
    query = """
        SELECT p.Product_id, p.Product_name, p.Product_description, 
               p.Product_cant, p.Product_price, c.Cat_name
        FROM productos p
        INNER JOIN categorias c ON p.Cat_id = c.Cat_id
        ORDER BY p.Product_name
    """
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    return products

def update_product(id: int, name: str, description: str, cant: int, price: float, cat_id: int) -> bool:
    
    cursor = conexion.sursor()
    query = """
                UPDATE productos 
                SET Product_name = %s, 
                    Product_description = %s, 
                    Product_cant = %s, 
                    Product_price = %s,
                    Cat_id = %s
                WHERE Product_id = %s
            """
    cursor.execute(query, (name, description, cant, price, cat_id, id))
    conexion.commit()

    cursor.close()
    return True

def delete_product(id: int):
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE Product_id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    cursor.close()
    return True

def get_category():
    cursor = conexion.cursor()
    query = "SELECT * FROM categorias"
    cursor.execute(query)


def all_categories():
    cursor = conexion.cursor()
    cursor.execute("SELECT Cat_id, Cat_name FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()
    return categorias

def create_product(name, description, cant, price, category_id):
    cursor = conexion.cursor()
    query = """
        INSERT INTO productos (Product_name, Product_description, Product_cant, Product_price, Cat_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, description, cant, price, category_id))
    conexion.commit()
    cursor.close()
    return True

