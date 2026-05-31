#    Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# num = 43197
# Пример вывода:
# 24



num = 43197

def sum_digits(num):
    if num < 10:
        return num

    return sum_digits(num // 10) + num % 10

print(sum_digits(num))

#     Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:
# 28

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def sum_nested(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

print(sum_nested(nested_numbers))
