# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего вкл.

str_task = '100 90'

def get_unicode_dict(range_in: str) -> dict[str: int]:
    start, end = map(int, range_in.split())
    res = {}
    for i in range(min(start, end), max(start, end)):
        res[chr(i)] = i
    return res


print(get_unicode_dict(str_task))

