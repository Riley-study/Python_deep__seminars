# Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text_init = 'список с уникальными кодами'


def generate_unicode_list(text: str) -> list[int]:
    res = []
    for char in text:
        res.append(ord(char))

    return res


print(generate_unicode_list(text_init))
