from Modulos.db import execute_query,conexion

def create_cat(id: int, name: str):
    query = "INSERT INTO categorias (Cat_id, Cat_name) VALUES (%s, %s)"
    try:
        execute_query(query, (id, name),commit=True)
        return True
    except Exception as e:
        print("Error en create_cat: {e}")
        return False
    
def view_cat():
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM categorias"
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    return categories
def delete_cat(id: int):
    query = "DELETE FROM categorias WHERE Cat_id = %s"
    try:
        execute_query(query, (id), commit=True)
        return True
    except Exception as e:
        print("Error en delete_cat: {e}")
        return False