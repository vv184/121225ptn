#     Фигуры и площади
# Создайте абстрактный класс Shape.
#     В классе должен быть метод area(), который возвращает площадь фигуры.
#     Реализуйте два класса:
#         Circle, который принимает радиус.
#         Rectangle, который принимает ширину и высоту.
# # Пример использования
# shapes = [Circle(3), Rectangle(4, 5)]
# for shape in shapes:
#     print(f"Area: {shape.area():.2f}")
#     Проверка размеров фигур
# Доработайте фигуры:
#     Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
#     Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.


from abc import ABC, abstractmethod
import math


class InvalidSizeError(Exception):
    """Исключение для некорректных размеров фигур."""
    pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Возвращает площадь фигуры."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Ширина и высота должны быть положительными числами")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Пример использования

shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:

    print(f"Area: {shape.area():.2f}")