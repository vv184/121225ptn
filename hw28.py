#     План по дням недели
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
# Данные:
# # Расписание дел на неделю
# weekly_schedule = {
#     "Monday": ["Gym", "Work", "Read book"],
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#     "Friday": ["Work", "Dinner with friends"],
#     "Saturday": ["Hiking", "Rest"],
#     "Sunday": ["Family time", "Rest"]
# }
# Пример ввода:
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# ...
# Нажмите 'Enter' для получения плана:
# Sunday: Family time, Rest
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана: q


weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

days = list(weekly_schedule.keys())

i = 0

while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")

    if user_input.lower() == 'q':
        break

    day = days[i % len(days)]
    print(f"{day}: {', '.join(weekly_schedule[day])}")

    i += 1


#     Объединение списков продуктов
# Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все продукты в нижнем регистре.
# Выведите содержимое генератора.
# Данные:
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
# Пример вывода:
# apple
# banana
# orange
# carrot
# tomato
# cucumber
# milk
# cheese
# yogurt


fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

def product_generator(*lists):
    for lst in lists:
        for item in lst:
            yield item.lower()

gen = product_generator(fruits, vegetables, dairy)

for item in gen:
    print(item)


#     Комбинации одежды
# Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".
# Данные:
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
# Пример вывода:
# T-shirt - Red - S
# T-shirt - Red - M
# T-shirt - Red - L
# T-shirt - Blue - S
# ...
# Jacket - Black - L


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def outfit_generator(clothes, colors, sizes):
    for c in clothes:
        for color in colors:
            for size in sizes:
                yield f"{c} - {color} - {size}"

for outfit in outfit_generator(clothes, colors, sizes):
    print(outfit)