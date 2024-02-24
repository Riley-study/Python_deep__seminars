class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Rectangle:
    def __init__(self, width, height=None):
        self._height = height if height else width
        self._width = width
        if self._width <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {self._width}")
        if self._height <= 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {self._height}")

    def perimeter(self):
        return self._height * 2 + self._width * 2

    def area(self):
        return self._height * self._width

    def __add__(self, other: 'Rectangle'):
        new_perim = self.perimeter() + other.perimeter()
        new_height = self._height + other._height
        new_width = new_perim / 2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perim = self.perimeter() - other.perimeter()
        new_height = abs(self._height - other._height)
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
        return f'Rectangle with length = {self._width} width = {self._height} '

    def __repr__(self):
        return f'Rectangle({self._width}, {self._height})'

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value


if __name__ == '__main__':
    # r = Rectangle(-2)
    r = Rectangle(5, -3)
    # r = Rectangle(4, 4)
    # r.width = -3  # __main__.NegativeValueError: Ширина должна быть положительной, а не -3
    # r = Rectangle(4, 4)
    # r.height = -3  # __main__.NegativeValueError: Высота должна быть положительной, а не -3
