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
from typing import Callable


def generate_csv_file(file_name, rows):
    # if not 100 <= rows <= 1000:
    #     rows = randint(100, 1001)

    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(rows):
            a = randint(0, 100)
            b = randint(0, 100)
            c = randint(0, 100)
            csv_write = csv.writer(f)
            csv_write.writerow((a, b, c))


def save_to_json(json_file):
    def deco(func):
        def wrapper(csv_file):
            with open(csv_file, 'r', encoding='utf-8') as f_in:
                args = []
                csv_reader = csv.reader(f_in, dialect='excel')
                for line in csv_reader:
                    if line:
                        dict = {}
                        a, b, c = line[0], line[1], line[2]
                        dict["parameters"] = [a, b, c]
                        dict["result"] = func(a, b, c)
                        args.append(dict)
            with open(json_file, 'w', encoding='utf-8') as f_out:
                json_writer = json.dump(args, f_out, indent=1)
            return dict

        return wrapper

    return deco


@save_to_json('results.json')
def find_roots(a, b, c):
    if int(a) == 0:
        return None
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        d = b ** 2 - 4 * a * c
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if d < 0:
            return None
        elif d == 0:
            return x1
        else:
            return x1, x2


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

# with open("results.json", 'r') as f:
#     data = json.load(f)

# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

# print(len(data))

generate_csv_file("input_data.csv", 2)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

# if 100 <= len(data) <= 1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data))
