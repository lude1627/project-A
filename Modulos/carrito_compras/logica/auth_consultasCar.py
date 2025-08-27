from Modulos.db import  execute_query

def get_items():
<<<<<<< HEAD
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
=======
    query = "SELECT * FROM carrito"
    try:
        carrito = execute_query(query, fetchall=True)
        return carrito
    except Exception as e:
        print("Error al mostrar compras: {e}")
        return False
    
def eliminar_producto_db(id: int) -> bool:
    try:
        query = "DELETE FROM productos WHERE id = %s" 
        execute_query(query,(id),commit=True)
        return 
    except Exception as e:
        print("Error al eliminar: {e}")
        return False
>>>>>>> 21532cfa27eec29c007212ff73ee79a8f3f007dc

