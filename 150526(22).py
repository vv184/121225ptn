# Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
#     Отбирает заказы дороже 500.
#     Создаёт список названий отобранных продуктов в алфавитном порядке.
#     Возвращает итоговый список названий.
# Данные:
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
# Пример вывода:
# ['Chair', 'Laptop']

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400},
]

def select_expensive_products(orders):
    return sorted(
        map(
            lambda order: order["product"],
            filter(lambda order: order["price"] > 500, orders)
        )
    )

print(select_expensive_products(orders))

# Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
#     Вычисляет общую выручку для каждого товара.
#     Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800),
]

def sales_statistics(sales):
    revenue = dict(
        map(
            lambda item: (item[0], item[1] * item[2]),
            sales
        )
    )

    return dict(
        sorted(
            revenue.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

print(sales_statistics(sales))