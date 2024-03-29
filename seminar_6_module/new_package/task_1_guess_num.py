from random import randint as rnd
from sys import argv
__all__ = ['guessing_game']

# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу
# и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен
# угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

def guessing_game(min_num=1, max_num=10, count=5):
    num_to_guess = rnd(min_num, max_num)
    for i in range(count):
        num_from_user = int(input("Enter number: "))
        if num_to_guess == num_from_user:
            return True
        elif num_to_guess > num_from_user:
            print("загаданное число больше")
        else:
            print("загаданное число меньше")
    return False


# if __name__ == '__main__':
#     print(guessing_game(1, 10, 5))


# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


if __name__ == '__main__':
    print(guessing_game(*list(map(int, argv[1:]))))
