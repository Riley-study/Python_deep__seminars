"""
Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь. Если при создании экземпляра передаётся
только одна сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.lenght = length
        self.width = width if width else length

    def len(self):
        return self.lenght * 2 + self.width * 2

    def area(self):
        return self.lenght * self.width


rect = Rectangle(2, 4)
print(rect.len())
print(rect.area())
