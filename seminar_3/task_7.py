# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
import time

text = "fghjk fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 1111111111 fghjk fghjkkk defrtghj " \
       "sdf ghj 1111111111 fghjk fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 1111111111df gh" \
       "j 1111111111 fghjk fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 111111111df ghj 111111" \
       "1111 fghjk fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 111111111df ghj 1111111111 " \
       "fghjk fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 111111111df ghj 1111111111 fghjk " \
       "fghjkkk defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 111111111df ghj 1111111111 fghjk fghjkkk " \
       "defrtghj sdf ghj 1111111111fghjk fghjkkk defrtghj sdf ghj 111111111df ghj 1111111111 fghjk fghjkkk defrtghj " \
       "k defrtghj sdf ghj 111111111"
text1 = text.replace(" ", "")
new_dict = {}

# 1 var
start1 = time.time()
for i in text1:
    # new_dict.setdefault(i, 0)
    new_dict[i] = new_dict.get(i,0) +1
    # new_dict[i] += 1

print(new_dict)
stop1 = time.time()
print(start1 - stop1)

# 2 var
start2 = time.time()
for i in set(text1):
    count = text1.count(i)
    new_dict.setdefault(i, count)

print(new_dict)
stop2 = time.time()
print(start2 - stop2)

