# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = "ааа ттт ббб опачкиии hhhh 12"
list_of_words = text.split(" ")
list_of_words.sort()
max_length = len(max(list_of_words, key=len))

# for word in list_of_words:
#     if max_length < len(word):
#         max_length = len(word)
print(max_length)

for i, word in enumerate(list_of_words, 1):
    print(f'{i} {word:>{max_length + 1}}')
