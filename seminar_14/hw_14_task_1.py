import doctest

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Rectangle:
    """
    >>> r1 = Rectangle(5)
    >>> r1.width
    5
    >>> r4 = Rectangle(-2)
    'NegativeValueError: Ширина должна быть положительной, а не -2'
    >>> r2 = Rectangle(3,4)
    >>> r2.width
    3
    >>> r2.height
    4
    >>> r1 = Rectangle(5)
    >>> r1.perimeter()
    20
    >>> r2 = Rectangle(3,4)
    >>> r2.perimeter()
    14
    >>> r1 = Rectangle(5)
    >>> r1.area()
    25
    >>> r2 = Rectangle(3,4)
    >>> r2.area()
    12
    >>> r3 = r1 + r2
    >>> r3.width
    8
    >>> r3.height
    6.0
    >>> r3 = r1 - r2
    >>> r3.width
    2
    >>> r3.height
    2.0
        """
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
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        new_perim = self.perimeter() - other.perimeter()
        new_height = abs(self._height - other._height)
        new_width = new_perim / 2 - new_height
        if new_height > new_width:
            new_height, new_width = new_width, new_height
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
    doctest.testmod(verbose=True)

