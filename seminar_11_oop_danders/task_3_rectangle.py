# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, length, width=None):
        self.lenght = length
        self.width = width if width else length

    def len(self):
        return self.lenght * 2 + self.width * 2

    def area(self):
        return self.lenght * self.width

    def __add__(self, other: 'Rectangle'):
        new_perim = self.len() + other.len()
        new_length = self.lenght + other.lenght
        new_width = new_perim / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perim = self.len() - other.perimeter()
        # print(new_perim)
        new_width = abs(self.width - other.width)
        # print(new_width)
        new_length = new_perim / 2 - new_width
        # print(new_length)
        if new_length < 0:
            raise ValueError("Размеры вычитаемого прямоугольника превышают размеры уменьшаемого прямоугольника")

        return Rectangle(new_length, new_width)

    def __eq__(self, other: 'Rectangle'):
        return self.area() == other.area

    def __gt__(self, other: 'Rectangle'):
        return self.area() > other.area()

    def __ge__(self, other: 'Rectangle'):
        return self.area() >= other.area()

    def __str__(self):
        return f'Rectangle with length = {self.lenght} width = {self.width} '


if __name__ == '__main__':
    a = Rectangle(4, 10)
    b = Rectangle(3, 10)
    print(a + b)
    print(a - b)
    print(a == b)
    print(a >= b)
    print(a <= b)
    print(a < b)
    print(a > b)
