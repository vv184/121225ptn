#     Добавление товаров
# Создайте программу, которая подключается к MongoDB и:
#     выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
#     очищает коллекцию перед началом
#     добавляет 3 товара с полями: name, price, stock
#     выводит сообщение о количестве добавленных товаров


from pymongo import MongoClient

client = MongoClient("")

db = client["ich_edit"]

collection_name = "products_<your_group>_<your_full_name>"
collection = db[collection_name]

collection.delete_many({})

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Phone", "price": 800, "stock": 10},
    {"name": "Headphones", "price": 150, "stock": 20}
]

result = collection.insert_many(products)

print(f"{len(result.inserted_ids)} products inserted.")


#     Увеличение цен
# Продолжите предыдущую задачу. Теперь программа должна:
#     увеличить цену всех товаров на 20%
#     вывести количество обновлённых записей
#     затем вывести список всех товаров с новыми ценами


from pymongo import MongoClient

client = MongoClient("")
db = client["shop"]
products = db["products"]

result = products.update_many(
    {},
    [{"$set": {"price": {"$multiply": ["$price", 1.2]}}}]
)

print(f"Prices updated for {result.modified_count} products.\n")

print("Updated products:")
for product in products.find():
    print(f"- {product['name']} — ${product['price']:.2f}")