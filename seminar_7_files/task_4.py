# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randint, choice

LAT_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def name_generate(min_len_name=6, max_len_name=30):
    res = ''.join([choice(LAT_ALPHABET)
                   for i in range(randint(min_len_name, max_len_name))])
    return res

def write_file (
        ext='.txt',
        min_len_name=6,
        max_len_name=30,
        min_byte=256,
        max_byte=4096,
        count_file=42
) -> None:
    for i in range(count_file):
        with open(name_generate(min_len_name, max_len_name) + ext, 'wb') as file:
            file.write(bytes([randint(0, 255) for i in range(randint(min_byte, max_byte))]))


write_file(ext='.crv', count_file=3)
