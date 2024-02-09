import json
from random import randint as rnd
from typing import Callable
from task_3_deco_json import json_cache
from task_4 import count_decor
from task_1_decorator import value_checker

@json_cache
@count_decor(3)
@value_checker
def task05_run(num: int, count: int):
    for _ in range(count):
        answer = int(input('Угадайте число: '))
        if answer == num:
            return True
    return False


if __name__ == '__main__':
    task05_run(5, 6)
