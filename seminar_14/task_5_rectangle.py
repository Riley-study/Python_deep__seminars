import doctest


class Rectangle:
    """
    >>> Rectangle(4,8).area()
    32
    >>> Rectangle(4, 8) + Rectangle(2, 4)
    Rectangle(12, 6.0)
    >>> Rectangle(4, 8) - Rectangle(2, 2)
    Rectangle(2.0, 6)
    """

    def __init__(self, width, height=None):
        self._height = height if height else width
        self._width = width

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


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    help(Rectangle)
