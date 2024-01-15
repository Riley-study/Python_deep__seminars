import sys
from typing import Hashable
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

abc = 25*5
data = ['hello', 12345, 1.0, abc, True, [4]]
# добавление новых элементов
data.extend(['hello', 12345, 1.0, abc, True, [4]])
n = 0

# while data:
#     n += 1
#     print(f'{n} {data.pop(-1)}')

for n, obj in enumerate(data, 1):
    print(f'{n} {obj} {id(obj)} {sys.getsizeof(obj)}', end=" ")
    print(hash(obj) if isinstance(obj, Hashable) else "no hash", end= "")
    print(f'{" целое положительное число" if isinstance(obj, int) else ""}'
          f'{" строка" if isinstance(obj, str) else ""}')
