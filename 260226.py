#     Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

text_list = ["Hello", "Python Programming", "World", "Advances Topics", "Simple"]

list = [text.lower() for text in text_list if len(text.split()) == 1]

print("Обработанный список:", list)

#     Обновление цен товаров
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару
# и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
# Введите скидку (в процентах): 17

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

discount = float(input("Введите скидку (в процентах): "))

print("\nТовар          Старая цена     Новая цена")

for product in products:
    name = product[0]
    old_price = product[1]
    new_price = old_price * (1 - discount / 100)

    print(f"{name:<15} {old_price:>10.2f}$ {new_price:>12.2f}$")