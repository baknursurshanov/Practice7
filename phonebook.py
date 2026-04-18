import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "", 
    "host": "127.0.0.1"
}

def start_app():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        print("Подключено")

        
        cur.execute("CREATE TABLE IF NOT EXISTS phonebook (id SERIAL PRIMARY KEY, name TEXT, phone TEXT);")
        conn.commit()

        
        print("Ввод данных")
        user_name = input("Введите ИМЯ: ")
        user_phone = input("Введите НОМЕР: ")

        print(f"Отправка {user_name} в базу")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (user_name, user_phone))

        conn.commit() 
        print("Данные сохранены")

        cur.execute("SELECT * FROM phonebook;")
        print("Что сейчас в базе:")
        for row in cur.fetchall():
            print(row)

        cur.close()
        conn.close()

    except Exception as e:
        print(f"\n!!! ОШИБКА: {e}")

if __name__ == "__main__":
    start_app()
