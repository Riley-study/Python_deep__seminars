# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends = {
    "Афанасий": ("аккордеон", "бинокль", "велосипед", "розжиг", "спальник"),
    "Борис": ("аккордеон", "бинокль", "велосипед", "розжиг", "спальник"),
    "Владимир": ("аккордеон", "бинокль", "велосипед", "палатка", "котелок")
}

all_things = []
for thing in friends.values():
    all_things.extend(thing)

uniq_things = set(all_things)
print(all_things)  # список всех-всех вещей
print(uniq_things)  # список вещей без повторений у всех

# составить словарь вещь: количество, те вещи, которые встречаются по одному разу ищем в изначальном словаре
# и выводим имя владельца

dict_all_things_count = {}
for thing in all_things:
    dict_all_things_count[thing] = dict_all_things_count.get(thing, 0) + 1
print(dict_all_things_count)

onely_thin_in_the_list = []

for thing in dict_all_things_count:
    if dict_all_things_count[thing] == 1:
        onely_thin_in_the_list.append(thing)
print(f'вещи, которые есть только у одного: {onely_thin_in_the_list}')

for thing in onely_thin_in_the_list:
    for key, value in friends.items():
        if thing in value:
            print(f'{thing} - есть только у друга с именем {key}')

# те вещи, количество которые содержится по (кол-во друзей - 1) есть у всех кроме одного, по ключу названия вещи
# выводим того, у кого ее нет
dict_all_except_one = {}
list_all_except_one = []

friends_except_one = len(friends) - 1
for thing, count in dict_all_things_count.items():
    if count == friends_except_one:
        list_all_except_one.append(thing)

for thing in list_all_except_one:
    for key, value in friends.items():
        if thing not in value:
            print(f'{thing} - нет только у друга с именем {key}')
