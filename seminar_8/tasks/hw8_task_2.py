# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
# и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах:
# JSON, CSV и Pickle (на выбор). Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории.
# Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
import csv
import json
import os
import pickle
from pprint import pprint


# def get_dir_size(path_dir: str) -> int:
#     size_res = 0
#     for path_, _, files in os.walk(path_dir):
#         for file in files:
#             size_res += os.path.getsize(os.path.join(path_, file))
#     return size_res


def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def save_results_to_json(data: [{str: str | int}], file_name) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_results_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        csv_write = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        csv_write.writeheader()
        csv_write.writerows(data)


def save_results_to_pickle(data: [{str: str | int}], file_name) -> None:
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)


def traverse_directory(full_path=os.getcwd()) -> [{str: str}]:
    result = []
    for path_, dir_list, file_list in os.walk(full_path):
        for cur_file in file_list:
            result.append({'Path': os.path.join(path_, cur_file), 'Type': 'File',
                           'Size': os.path.getsize(os.path.join(path_, cur_file))})
        for cur_dir in dir_list:
            result.append({'Path': os.path.join(path_, cur_dir), 'Type': 'Directory',
                           'Size': get_dir_size(os.path.join(path_, cur_dir))})
    return result


pprint(traverse_directory(r'/seminar_6_module/seminar_8'))
save_results_to_json(
    traverse_directory(r'/seminar_6_module/seminar_8'),
    'res.json')
save_results_to_csv(
    traverse_directory(r'/seminar_6_module/seminar_8'),
    'res.csv')
save_results_to_pickle(
    traverse_directory(r'/seminar_6_module/seminar_8'),
    'res.bin')
