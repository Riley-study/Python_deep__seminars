# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def my_readline(file):
    line = file.readline()
    if line == '':
        file.seek(0)
        return file.readline()
    return line


def names_and_numbers(names: str, numbers: str, task_res: str) -> None:
    with(open(names, 'r', encoding='utf-8') as name,
         open(numbers, 'r', encoding='utf-8') as numb,
         open(task_res, 'w', encoding='utf-8') as res):
        max_len = max(len(name.read().split('\n')), len(numb.read().split('\n')))
        for i in range(max_len):
            new_name = my_readline(name).replace('\n', '')
            num_to_split = my_readline(numb).replace('\n', '')
            n1, n2 = num_to_split.split(' | ')
            new_n = int(n1) * float(n2)
            if new_n < 0:
                res.write(f'{new_name.lower()} : {abs(new_n)}\n')
            else:
                res.write(f'{new_name.upper()} : {int(new_n)}\n')
        # list_name = name.readlines()
        # numb_list = numb.readlines()


names_and_numbers('task2.txt', '12.txt', 'result_task3.txt')
