# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например, отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)


def division(x, y):
    try:
        res = x / y
        logging.debug(f'деление прошло успешно')
        return res
    except ZeroDivisionError as err:
        logging.error(f"{err} на ноль айайай")


if __name__ == '__main__':
    division(5, 5)
