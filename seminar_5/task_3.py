# Создайте генератор чётных чисел от нуля до 100. Из последовательности исключите числа,
# сумма цифр которых равна 8. Решение в одну строку.

gen_even_numbers = (number for number in range(0, 101, 2) if sum(map(int, str(number))) != 8)
for i in gen_even_numbers:
    print(i)
