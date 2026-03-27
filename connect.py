import psycopg2
from config import host, user, password, db_name, port

def get_connection():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
        )
        connection.autocommit = True 
        return connection
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

if name == "main":
    test_conn = get_connection()
    if test_conn:
        print("Связь установлена")
        test_conn.close()
