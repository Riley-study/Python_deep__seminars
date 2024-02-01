# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей
# на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами,
# ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
# Пример использования На входе:
from random import randint as rnd


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


def generate_boards() -> list[list[tuple]]:
    chess_board = list()
    res_list = []
    while len(res_list) < 4:
        for i in range(9):
            coordinate1 = rnd(1, 9)
            coordinate2 = rnd(1, 9)
            chess_board.append((coordinate1, coordinate2))
        # if check_queens(chess_board):
        res_list.append(chess_board)
    return res_list


print(generate_boards())
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4),
# (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
# [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
