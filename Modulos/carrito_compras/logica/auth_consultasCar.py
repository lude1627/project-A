from Modulos.db import  execute_query

def get_items():
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

