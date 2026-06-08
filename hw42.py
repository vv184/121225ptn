#      Создание базы
# Напишите программу, которая:
#     создаёт базу данных notes_app_<your_group>_<your_full_name>
#     выбирает эту базу через USE notes_app
#     выводит сообщение о результате

import pymysql
from pymysql.cursors import DictCursor

db_name = "notes_app_<your_group>_<your_full_name>"

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    charset="utf8mb4",
    cursorclass=DictCursor
)

try:
    with connection.cursor() as cursor:

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created or already exists.")

        cursor.execute(f"USE {db_name}")

finally:
    connection.close()

#     Добавление заметок
# Продолжите предыдущую программу:
#     создайте таблицу notes с полями: id, title, content
#     вставьте одну заметку в таблицу
#     выполните commit() после вставки
# выведите все заметки используя DictCursor


import pymysql
from pymysql.cursors import DictCursor

db_name = "notes_app_<your_group>_<your_full_name>"

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    charset="utf8mb4",
    cursorclass=DictCursor
)

try:
    with connection.cursor() as cursor:

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                content TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO notes (title, content)
            VALUES (%s, %s)
        """, ("Shopping list", "Milk, Bread, Eggs"))

        connection.commit()

        print("Note added: Shopping list")

        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()

        for note in notes:
            print(note)

finally:
    connection.close()

