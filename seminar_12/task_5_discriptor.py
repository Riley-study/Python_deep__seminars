class Side:
    def __init__(self, min_val: int = 1, max_val: int = 100):
        self._min_val = min_val
        self._max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        if not self._min_val <= value <= self._max_val:
            raise ValueError("error")


class Rectangle:
    length = Side(3, 5)
    wight = Side(3, 5)

    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) > 1 else self.length

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, value):
        self.length = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.width = value

    def area(self):
        return self.length * self.width

    def perim(self):
        return 2 * (self.length + self.width)

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perim() + other.perim()
        new_length = self.length + other.length
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perim() - other.perim())
        new_length = abs(self.length - other.length)
        new_width = new_perimetr / 2 - new_length
        if new_width < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f'Rectangle({self.length=}, {self.width=})'


if __name__ == '__main__':
    P1 = Rectangle(4, 8)
    P2 = Rectangle(6, 11)
    print(P1.length)
    print(P2.width)
