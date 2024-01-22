# Создайте несколько переменных заканчивающихся и не оканчивающихся на “s”. Напишите функцию,
# которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной
# из одной буквы s на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

number = 1
numbers = [1, 2]
s = 's'


def remove_var_with_s():
    list_of_var_with_s = []
    for var in globals():
        if var.endswith("s") and len(var) > 1:
            list_of_var_with_s.append(var)
    return list_of_var_with_s

list_of_var = remove_var_with_s()
print(list_of_var)

for attr in list_of_var:
    globals()[attr[:-1]] = globals()[attr]
    globals()[attr] = None

print(number, numbers)
