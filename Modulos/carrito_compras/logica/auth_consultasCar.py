from Modulos.db import  execute_query

#guardar datos
def add_to_cart(product_id: int, user_id: int, cantidad: int):
    query = """
        INSERT INTO carrito (User_id, Product_id, Car_Cantidad)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE Car_Cantidad = Car_Cantidad + VALUES(Car_Cantidad);
    """
    cursor = conexion.cursor()
    cursor.execute(query, (user_id, product_id, cantidad))
    conexion.commit()
    return JSONResponse(content={"message": "Producto agregado al carrito"})

#uno mas
#mostrar datos en tabla
def get_items():
    query = """ 
        SELECT c.Car_id, u.User_id, u.User_name, p.Product_id, p.Product_name, c.Car_Cantidad, p.Product_price AS precio, (c.Car_Cantidad * p.Product_price) AS subtotal
        FROM carrito c JOIN productos p ON c.Product_id = p.Product_id JOIN usuario u ON c.User_id = u.User_id;
        """
    try:
            carrito = execute_query(query, fetchall=True)
            return carrito
    except Exception as e:
            print("Error al mostrar compras: {e}")
            return False
    
<<<<<<< HEAD
=======
#eliminar
>>>>>>> 5567bcd4542a5bc9e7277d16b0e0775832030d44
def eliminar_producto_db(id: int) -> bool:
    try:
        query = "DELETE FROM productos WHERE id = %s" 
        execute_query(query,(id),commit=True)
        return 
    except Exception as e:
        print("Error al eliminar: {e}")
        return False

