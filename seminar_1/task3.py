# Нарисовать в консоли ёлку спросив у пользователя количество рядов. Пример результата:
# Сколько рядов у ёлки? 5

tree = int(input("Введите число уровней елки: "))
count = 1
while count <= tree:
    print(" " * (tree - count) + "*" * (count * 2 - 1))
    count += 1
