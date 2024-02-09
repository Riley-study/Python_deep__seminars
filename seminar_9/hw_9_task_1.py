"""
1) Создать функцию generate_csv_file, которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

2) вторая функция ищет корни квадратного уравнения, принимает на вход три числа
3) декоратор save_to_json, который меняет работу функции 2, три числа на вход он берет из CSV файла, результаты записывает в json
"""
import csv
import json
from random import randint


def generate_csv_file(file_name: str, rows: int):
    if not 100 <= rows <= 1000:
        rows = randint(100, 1001)

    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(rows + 1):
            a = randint(0, 100)
            b = randint(0, 100)
            c = randint(0, 100)
            csv_write = csv.writer(f)
            csv_write.writerow((a, b, c))


def save_to_json(csv_file):
    def deco(func):
        def wrapper(json_file):
            with (open(json_file, 'w') as f_out, open(csv_file, 'r', newline='') as f_in):
                args = []
                csv_reader = csv.reader(f_in)
                json_writer = json.dump(f_out)
                for line in csv_reader:
                    dict = {}
                    a, b, c = line[0], line[1], line[2]
                    dict["parameters"] = [a, b, c]
                    dict["result"] = func(a, b, c)
                    args.append(dict)
                return args

        return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    if d < 0:
        return None
    elif d == 0:
        return x1
    else:
        return x1, x2


if __name__ == '__main__':
    generate_csv_file('first.csv', 101)
    print(find_roots(''))