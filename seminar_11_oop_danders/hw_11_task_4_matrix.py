class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join(''.join(f'{x:^3}' for x in row) for row in self.data)

    def __repr__(self):
        return f'Matrix({self.rows},{self.cols})'

    def __eq__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            # return all([all([self.data[r][c] == other.data[r][c] for c in range(self.cols)] for r in range(self.rows))])
            return all(
                map(lambda x: x[0] == x[1], zip([y for x in self.data for y in x], [y for x in other.data for y in x])))
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            # for i in range(self.rows):
            #     for j in range(self.cols):
            #         new_matrix.data = self.data[i][j] + other.data[i][j]
            # return new_matrix
            new_matrix.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return new_matrix
        else:
            raise ValueError("размер матриц не совпадает")

    def __mul__(self, other):
        if isinstance(other, Matrix) and other.cols == self.rows:
            new_matrix = Matrix(other.cols, self.rows)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        new_matrix.data[i][j] += self.data[i][k] * other.data[k][j]
            return new_matrix
        else:
            raise ValueError("размер матриц не подходит для умножения")


if __name__ == '__main__':
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    print(matrix1)

    matrix2 = Matrix(3, 2)
    matrix2.data = [[1, 2], [4, 5], [4, 5]]
    print(matrix2)
    print(matrix2 == matrix1)
    print(matrix2 is matrix1)
    # print(matrix2 + matrix1)
    print(matrix2 * matrix1)
