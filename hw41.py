#     Список всех стран
# Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой строки и иметь номер.


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="world"
)

cur = conn.cursor()
cur.execute("SELECT Name FROM country ORDER BY Name")

i = 1
for (name,) in cur:
    print(i, name)
    i += 1

conn.close()


#     Города выбранной страны
# Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка. Далее выведите все города этой страны и их численность населения, также с нумерацией.



cur = conn.cursor()

cur.execute("SELECT Code, Name FROM country ORDER BY Name")

countries = cur.fetchall()

i = 1
for code, name in countries:
    print(i, name)
    i += 1

choice = input("Введите номер или название страны: ")

country_code = None

try:
    choice_num = int(choice)
    country_code = countries[choice_num - 1][0]
except:
    for code, name in countries:
        if name.lower() == choice.lower():
            country_code = code
            break

cur.execute(
    "SELECT Name, Population FROM city WHERE CountryCode = %s ORDER BY Population DESC",
    (country_code,)
)

print("\nГорода:")
i = 1
for name, pop in cur:
    print(i, name, pop)
    i += 1

conn.close()