
# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

matrix = [[1, 2, 3, 4],
          [4, 5, 6, 7],
          [7, 8, 9, 10]]


def transpose(matrix_in: list[list[int]]) -> list[list[int]]:
    rows = len(matrix_in)
    col = len(matrix_in[0])
    result = [[0 for _ in range(rows)] for _ in range(col)]
    for i in range(rows):
        for j in range(col):
            result[j][i] = matrix_in[i][j]
    return result


def transpose2(matrix_in: list[list[int]]) -> list[list[int]]:
    temp = []
    for i in range(len(matrix_in[0])):
        temp.append([])
        for j in range(len(matrix_in)):
            temp[i].append(matrix_in[j][i])
    return temp


def transpose_zip(matrix_in: list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix_in))


transposed_matrix = transpose(matrix)
transposed_matrix2 = transpose2(matrix)
transposed_matrix3 = transpose_zip(matrix)
print(transposed_matrix)
print(transposed_matrix2)
print(transposed_matrix3)

