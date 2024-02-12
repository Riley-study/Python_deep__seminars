# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return 2 * math.pi * self.radius

    def circle_area(self):
        return math.pi * self.radius ** 2


circle = Circle(4)
print(circle.circle_length())
print(circle.circle_area())
