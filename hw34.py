# Создайте класс Rectangle, который описывает прямоугольник.
#     У каждого объекта должны быть два поля: width и height.
#     Добавьте метод get_area(), который возвращает площадь прямоугольника.
#     Создайте объект прямоугольника с произвольными значениями.
#     Выведите его площадь.
#     Измените ширину и высоту.
#     Выведите новую площадь.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rect = Rectangle(4, 5)

print("Площадь:", rect.get_area())

rect.width = 5
rect.height = 7

print("Новая площадь:", rect.get_area())


# class Counter:
#     def __init__(self):
#         self.value = 0  # счётчик начинается с нуля
#     def increase(self):
#         self.value += 1
#         print(f"Значение увеличено, текущее: {self.value}")
#     def decrease(self):
#         self.value -= 1
#         print(f"Значение уменьшено, текущее: {self.value}")
#     def get_value(self):
#         return self.value
# # Проверка работы счётчика
# counter = Counter()
# counter.increase()  # 1
# counter.increase()  # 2
# counter.increase()  # 3
# counter.decrease()  # 2
# print("Текущее значение:", counter.get_value())


class Counter:
    def __init__(self):
        self.value = 0  # счётчик начинается с нуля

    def increase(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrease(self):
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self):
        return self.value


# Проверка работы счётчика
counter = Counter()

counter.increase()  # 1
counter.increase()  # 2
counter.increase()  # 3
counter.decrease()  # 2

print("Текущее значение:", counter.get_value())