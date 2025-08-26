from Modulos.db import execute_query

def login_user(username: str, password: str):
    query = "SELECT * FROM usuario WHERE User_name = %s AND User_password = %s"
    try:
        result = execute_query(query, (username, password), fetchone=True)
        return result
    except Exception as e:
        print(f"Error en login_user: {e}")
        return None


def register_user(id: int, username: str, phone: int, email: str, password: str):
    query = """
        INSERT INTO usuario (User_id, User_name, User_phone, User_mail, User_password) 
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        execute_query(query, (id, username, phone, email, password), commit=True)
        return True
    except Exception as e:
        print(f"Error en register_user: {e}")
        return False


def update_user(id: int, username: str, phone: int, email: str, password: str):
    query = """
        UPDATE usuario 
        SET User_name = %s, User_phone = %s, User_mail = %s, User_password = %s 
        WHERE User_id = %s
    """
    try:
        execute_query(query, (username, phone, email, password, id), commit=True)
        return True
    except Exception as e:
        print(f"Error en update_user: {e}")
        return False


def view_user(id: int):
    query = "SELECT * FROM usuario WHERE User_id = %s"
    try:
        result = execute_query(query, (id,), fetchone=True)
        return result
    except Exception as e:
        print(f"Error en view_user: {e}")
        return None
