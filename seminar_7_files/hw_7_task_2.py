# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него функцию rename_files
#
# Ожидаемый ответ:
#
# Функция def rename_files найдена в файле __init__.py

import os
import pathlib


def rename_files(desired_name, num_digits, source_ext, target_ext):
    current_path = pathlib.Path(f'{os.getcwd()}/.txt')
    count = 1
    for file in current_path.iterdir():
        if file.suffix == f'.{source_ext}':
            file.rename(f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}')
            count += 1


with open ('__init__.py', 'w', encoding='utf-8') as f_write, \
        open ('hw_7_task1.py', 'r', encoding='utf-8') as f_read:
     for line in f_read:
         f_write.writelines('rename_files()')
