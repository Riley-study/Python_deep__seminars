"""
доработать задание 1 до декоратора
"""
from functools import wraps
from random import randint as rnd
from typing import Callable


def value_checker(func):
    @wraps(func)
    def wrapper(num, count):
        if not 1 <= num <= 100:
            num = rnd(1, 100)
        if not 1 <= count <= 10:
            num = rnd(1, 10)
        return func(num, count)
    print("start_game")
    return wrapper


@value_checker
def run(num: int, count: int):
    for _ in range(count):
        answer = int(input('Угадайте число: '))
        if answer == num:
            return True
    return False


if __name__ == '__main__':
    run(6, 6)
