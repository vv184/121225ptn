# Объединение данных в строку
# Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари)
# и возвращает их строковое представление, объединённое через " | ". Добавьте документацию
# и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
# data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
# Пример вывода:
# 42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}

from typing import Any

def  join_data(data: list[Any]) -> str:
    return ' | '.join(map(str, data))

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

print(join_data(data))

# Сумма вложенных чисел
# Напишите функцию, которая принимает список словарей, где каждый словарь содержит
# имя пользователя и список баллов. Функция должна вернуть сумму всех чисел.
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
# data = [
#     {"name": "Alice", "scores": [10, 20, 30]},
#     {"name": "Bob", "scores": [5, 15, 25]},
#     {"name": "Charlie", "scores": [7, 17, 27]}
# ]
# Пример вывода:
# Итоговый балл: 156

from typing import TypedDict

class UserData(TypedDict):
    name: str
    scores: list[int]

def sum_scores(data: list[UserData]) -> int:
    return sum(
        sum(user["scores"])
        for user in data
    )

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

print(f"Итоговый балл: {sum_scores(data)}")