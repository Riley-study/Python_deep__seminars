# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]
lst_res = []

for i in set(lst):
    count = lst.count(i)
    if count > 1:
        lst_res.append(i)

print(lst_res)
