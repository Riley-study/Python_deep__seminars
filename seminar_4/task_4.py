# Функция получает на вход список чисел. Отсортируйте его элементы in place без
# использования встроенных в язык сортировок. Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


num = [1, 5, 7, 3, 99, 23, 11]

print(num)
bubble_sort(num)
print(num)
