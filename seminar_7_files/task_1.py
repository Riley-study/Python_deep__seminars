# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform, choice
from string import ascii_letters


def rate_number(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines([f'{randint(-1000, 1001)} | {uniform(-1000, 1001)}\n' for _ in range(count_str + 1)])


rate_number(6, '12.txt')

# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

LAT_VOWELS = 'aeiou'
LAT_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LAT_CONR = 'bcdfghjklmnpqrstvwxyz'


def name_gen():
    res = ''.join([choice(LAT_CONR) if i % 2 == 0 else choice(LAT_VOWELS)
                   for i in range(randint(4, 8))]).capitalize()
    return res


def pseudo_names(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines([name_gen() + '\n' for _ in range(count_str + 1)])



pseudo_names(5, 'task2.txt')
