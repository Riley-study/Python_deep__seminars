# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя функцию is_attacking(q1,q2),
# проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def is_attacking(q1: tuple, q2: tuple) -> bool:
    first_queen = [*q1]
    second_queen = [*q2]
    if first_queen[0] - second_queen[0] == first_queen[1] - second_queen[1]:
        return True
    if first_queen[0] == second_queen[0] or first_queen[1] == second_queen[1]:
        return True
    return False


def check_queens(queens: list[tuple]) -> bool:
    for first_queen in queens:
        for second_queen in queens:
            if first_queen == second_queen:
                continue
            if is_attacking(first_queen, second_queen):
                return False
    return True

print(check_queens(queens))
# print(is_attacking((1, 1), (2, 3)))