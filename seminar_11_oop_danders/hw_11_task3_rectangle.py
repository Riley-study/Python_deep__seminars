class Rectangle:
    def __init__(self, width, height=None):
        self.height = height if height else width
        self.width = width

    def perimeter(self):
        return self.height * 2 + self.width * 2

    def area(self):
        return self.height * self.width

    def __add__(self, other: 'Rectangle'):
        new_perim = self.perimeter() + other.perimeter()
        new_height = self.height + other.height
        new_width = new_perim / 2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perim = self.perimeter() - other.perimeter()
        new_height = abs(self.height - other.height)
        new_width = new_perim / 2 - new_height
        if new_height > new_width:
            new_height, new_width = new_width, new_height
        # if new_height < 0:
        #     raise ValueError("Размеры вычитаемого прямоугольника превышают размеры уменьшаемого прямоугольника")
        return Rectangle(new_height, new_width)

    def __eq__(self, other: 'Rectangle'):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other: 'Rectangle'):
        return self.area() > other.area()

    def __ge__(self, other: 'Rectangle'):
        return self.area() >= other.area()

    def __str__(self):
        return f'Rectangle with length = {self.width} width = {self.height} '

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    # Rectangle(3, 3)


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
    print(f"высота rect4: {rect4.height}")
