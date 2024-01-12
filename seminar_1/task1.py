# Посчитайте сумму чётных элементов от 1 до n исключая кратные e. Используйте while и if.
# Попробуйте разные значения e и n.

# n = int(input("введите число"))
# e = int(input("введите число"))
# summa = 0
#
# for i in range(0, n + 1, 2):
#     if i % e != 0:
#         summa += i
# print(summa)

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif.
# Откажитесь от магических чисел.
# Обязательно учтите год ввода Григорианского календаря.
# В коде должны быть один input и один print.

year = int(input("Введите год для проверки: "))
MAIN_CONDITION = 4
ADD_CONDITION = 100
EXCEPTION_CONDITION = 400

if year % MAIN_CONDITION == 0 \
        and year % ADD_CONDITION != 0 \
        or year % EXCEPTION_CONDITION == 0:
    res = "високосный"
else:
    res = "не високосный"
print(res)
