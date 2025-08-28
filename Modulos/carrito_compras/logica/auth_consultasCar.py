from Modulos.db import  execute_query
#uno mas
#mostrar datos en tabla
def get_items():
    query = """ 
        SELECT c.Car_id, p.Product_name, c.Car_Cantidad, p.Product_price AS precio, (c.Car_Cantidad * p.Product_price) AS subtotal
        FROM carrito c JOIN productos p ON c.Product_id = p.Product_id;
        """
    try:
            carrito = execute_query(query, fetchall=True)
            return carrito
    except Exception as e:
            print("Error al mostrar compras: {e}")
            return False
    
#eliminar

def eliminar_producto_db(id: int) -> bool:
    try:
        query = "DELETE FROM productos WHERE id = %s" 
        execute_query(query,(id),commit=True)
        return 
    except Exception as e:
        print("Error al eliminar: {e}")
        return False

