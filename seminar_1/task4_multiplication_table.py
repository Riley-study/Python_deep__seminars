# Выведите в консоль таблицу умножения 2х2 до 9х9 как в школьной тетради

for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i+4):
            print(f" {k:>2} X {j:>2} = {k * j:>2}", end='\t')
        print()
    print()


#  Второй вариант решения на семинаре
# FORMAT = 15
#
# def print_mult(n, m):
#     for i in range(2, 11):
#         st = ''
#         for j in range(n, m + 1):
#             st0 = f'{j} X {i} = {j * i}'
#             st += st0 + ' ' * (FORMAT - len(st0))
#         print(st)
#
#
# print_mult(2, 5)
# print()
# print_mult(6, 9)
