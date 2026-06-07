#     Среднее время выполнения
# Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
# Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.


import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        total_time = 0
        result = None

        for _ in range(5):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()

            total_time += end - start

        average_time = total_time / 5

        print(f"Среднее время выполнения для 5 вызовов: {average_time:.2f} секунд")
        print(f"Результат: {result}")

        return result

    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()


#     Среднее время выполнения с количеством вызовов
# Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
# Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.


import time
from functools import wraps

def measure_time(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None

            for _ in range(repeats):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()

                total_time += end - start

            average_time = total_time / repeats

            print(
                f"Среднее время выполнения для {repeats} вызовов: "
                f"{average_time:.2f} секунд"
            )
            print(f"Результат: {result}")

            return result

        return wrapper

    return decorator


@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()