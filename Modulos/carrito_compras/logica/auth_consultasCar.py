from Modulos.db import  execute_query
#uno mas
#mostrar datos en tabla
def get_items():
    query = """ 
        SELECT c.Car_id, c.Car_Cantidad, p.Product_name, p.Product_price, (c.Car_Cantidad * p.Product_price)
        FROM carrito c JOIN productos p ON c.Product_id = p.Product_id;
        """
    try:
            carrito = execute_query(query, fetchall=True)
            return carrito
    except Exception as e:
            print("Error al mostrar compras: {e}")
            return False
    
#eliminar
def deleteProduct_carrito(Car_id: int):
   
    query = "DELETE FROM carrito WHERE Car_id = %s"

    try:
        execute_query(query,(Car_id),commit=True)
        return True
    except Exception as e:
        print("Error al eliminar el producto: {e}")
        return 

