from Modulos.db import conexion

def create_cat(id: int, name: str):
    cursor = conexion.cursor()
    query = "INSERT INTO categorias (Cat_id, Cat_name) VALUES (%s, %s)"
    cursor.execute(query, (id, name))
    conexion.commit()
    cursor.close()
    return True

def view_cat():
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM categorias"
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    return categories

def delete_cat(id: int):
    cursor = conexion.cursor()
    query = "DELETE FROM categorias WHERE Cat_id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    cursor.close()
    return True