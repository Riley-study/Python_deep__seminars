# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

text_init = "Слова выводятся отсортированными согласно кодировки"


def string_parse(text: str) -> str:
    """
    Обрабатывает строку
    :param text:
    :return: str
    """
    list_of_words = text.split(" ")
    list_of_words.sort()
    max_length = len(max(list_of_words, key=len))

    res = ''
    for i, word in enumerate(list_of_words, 1):
        res += f'{i} {word:>{max_length + 1}}\n'
    return res


print(string_parse(text_init))
help(string_parse)
