from random import randint, choice
import pathlib
import os

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def sort_files():
    current_path = pathlib.Path(os.getcwd()) # вернет текущую директорию
    for file in current_path.iterdir(): # итератор для директории в текущей папке
        if file.suffix == '.py':
            continue
        try:
            file.replace(f'{file.suffix}/{file.name}')
        except FileNotFoundError:
            os.mkdir(file.suffix)
            file.replace(f'{file.suffix}/{file.name}')


sort_files()