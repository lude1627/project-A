from Modulos.db import conexion

def login_user(username: str, password: str):
    cursor = conexion.cursor()
    query = "SELECT * FROM usuario WHERE User_name = %s AND User_password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def register_user(id: int, username: str,phone: int, email: str, password: str):
    cursor = conexion.cursor()
    query = "INSERT INTO usuario (User_id, User_name, User_phone, User_mail, User_password) VALUES (%s, %s, %s,%s, %s)"
    cursor.execute(query, (id,username, phone, email, password))
    conexion.commit()
    cursor.close()
    return True

