# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    first_fib_num = 0
    second_fib_num = 1
    while True:
        yield first_fib_num
        first_fib_num, second_fib_num = second_fib_num, first_fib_num + second_fib_num


f = fibonacci()
for i in range(50):
    print(next(f), end=', ')
