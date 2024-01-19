# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков


my_list = [1, 40, 55, 2, 5, 5, 7, 7, 8, 8, 9, 9, 10]
unic_list = set(my_list)
print(unic_list)

unic_list2 = []

for num in my_list:
    if num not in unic_list2:
        unic_list2.append(num)
print(unic_list2)