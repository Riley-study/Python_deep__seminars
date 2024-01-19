# Часто встречающиеся слова
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак
# препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

text = "Python 3.9 is the latest version of Python. It's awesome!"
formated_text = text.lower().replace(".", "").replace(",", "").replace("'", " ").replace("!", "")
words = formated_text.split()
words_without_num = []
for word in words:
   if not word.isdigit():
       words_without_num.append(word)
print(words)
print(words_without_num)

dict_res = {}
list_res = []

for word in words_without_num:
    dict_res[word] = dict_res.get(word, 0) + 1

for item in dict_res.items():
    list_res.append(tuple(item))


print(list_res)

# осталась сортировка по убыванию
# text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"