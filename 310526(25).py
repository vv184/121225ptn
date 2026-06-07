#     Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.

#     Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.


import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
)

dividend = input("Введите делимое: ")
divisor = input("Введите делитель: ")

try:
    dividend = int(dividend)
    divisor = int(divisor)
    result = dividend / divisor
except ValueError:
    logging.error("Ошибка: Введено некорректное число.")
    print("Ошибка: Введено некорректное число.")
except ZeroDivisionError:
    logging.error("Ошибка: Деление на ноль.")
    print("Ошибка: Деление на ноль.")
else:
    print(result)




