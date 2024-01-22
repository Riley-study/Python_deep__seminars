# Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text_init = 'список с уникальными кодами'


def generate_unicode_list(text: str) -> list[int]:
    res = set()
    for char in text:
        res.add(ord(char))
    return sorted(list(res), reverse=True)


print(generate_unicode_list(text_init))
