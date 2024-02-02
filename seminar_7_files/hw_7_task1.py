import os
import pathlib


# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании
# в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать
# только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")


def rename_files(desired_name, num_digits, source_ext, target_ext):
    current_path = pathlib.Path(f'{os.getcwd()}/.txt')
    count = 1
    for file in current_path.iterdir():
        if file.suffix == f'.{source_ext}':
            file.rename(f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}')
            count += 1


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
