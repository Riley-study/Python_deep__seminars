# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений. Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.


import json
from collections import defaultdict


class Factorial:
    def __init__(self, size, file_name: str='json_file.json'):
        self.storage = defaultdict(int)
        self.size = size
        self.file_name = file_name

    def __str__(self):
        txt = '\n'.join(f'{k}: {v}' for k, v in self.storage.items())
        return f'Объекты хранилища:\n{txt}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.storage, file, indent=4)
            self.storage.clear()


    def __call__(self, k):
        f = 1
        for i in range(2, k+1):
            f *= i
        if len(self.storage) == self.size:
            self.storage.pop(list(self.storage)[0])
        self.storage[k] = f
        return f


if __name__ == '__main__':
    ex1 = Factorial(6)
    with ex1:
        for i in range(1, 11):
            ex1(i)
        print(f'{ex1}')




