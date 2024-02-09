"""
1) Создать функцию generate_csv_file, которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

2) вторая функция ищет корни квадратного уравнения, принимает на вход три числа
3) декоратор save_to_json, который меняет работу функции 2, три числа на вход он берет из CSV файла, результаты записывает в json
"""
import csv
from random import randint


def generate_csv_file(file_name: str, rows: int):
    if not 100 <=rows <=1000:
        rows = randint(100, 1001)

    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(rows + 1):
            a = randint(0, 100)
            b = randint(0, 100)
            c = randint(0, 100)
            csv_write = csv.writer(f)
            csv_write.writerow((a, b, c))


def find_roots():
    pass


def save_to_json():
    pass

if __name__ == '__main__':
    generate_csv_file('first.csv',10)