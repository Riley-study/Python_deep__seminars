# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 16
num1 = num
# print(hex(num))
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
res = ""

while num > 0:
    res = str(index[num % 16]) + res
    num //= 16

print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {hex(num1)}')
