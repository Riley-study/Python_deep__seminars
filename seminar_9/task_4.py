"""
Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
"""
from functools import wraps
from typing import Callable


def count_decor(count: int):
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return deco


@count_decor(4)
def my_func(*args):
    return sum(args)


if __name__ == '__main__':
    print(my_func(1, 2, 3, 4, 5))
