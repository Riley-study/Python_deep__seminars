class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass(a={self.a}, b={self.b})'

    def __call__(self, *args, **kwargs):
        self.a.append(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
y = x(3.14, 100, 500, start=1) # добавит в х кортеж из трех чисел и пару start=1 в словарь, вернет знач True!
x(y=y) # добавит в х пару ключ значение 'y': True, тк у хранит значение True
print(x)
