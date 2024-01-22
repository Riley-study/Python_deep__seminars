# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала.
# Если верхняя граница больше длины списка, до конца.

def sum_numbers_between_two_index(in_list: list[int | float], start_index: int, end_index: int) -> int | float:
    """ returns sum of numbers"""
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    if end_index > len(in_list):
        end_index = len(in_list)
    if start_index < 0:
        start_index = 0
    return sum(in_list[start_index:end_index])


list_init = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 45, 67, 8, 99]

print(sum_numbers_between_two_index(list_init, -6, 25))
