# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def is_simple(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# def how_many_simple(num: int):
#     i = 2
#     yield i
#     i += 1
#     while i <= num:
#         if is_simple(i):
#             yield i
#         i += 2


def how_many_simple(num: int):
    for i in range(2, num):
        if is_simple(i):
            yield i
        i += 1


print(*how_many_simple(33))

# a = how_many_simple(33)
# for _ in range(33 + 1):
#     print(next(a))
