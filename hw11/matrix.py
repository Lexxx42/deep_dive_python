""" Создайте класс Матрица.

Добавьте методы для:
- вывода на печать;
- сравнения;
- сложения;
- умножения матриц.
"""
import random


class Matrix:
    """ Matrix class. """

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

    def print_matrix(self) -> None:
        """ Print matrix in a terminal. """
        for row in self.data:
            print(" ".join(map(str, row)))

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                'Number of columns in the first matrix must be equal '
                'to the number of rows in the second matrix.'
            )

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.data[i][k] * other.data[k][j]
                result.data[i][j] = dot_product

        return result


matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

print('Matrix 1:')
matrix1.print_matrix()

# Matrix 1:
# 8 9 2
# 6 4 7
# 6 7 3

print('\nMatrix 2:')
matrix2.print_matrix()

# Matrix 2:
# 7 8 7
# 9 7 2
# 0 4 7

result_matrix = matrix1 + matrix2
print('\nMatrix Addition Result:')
result_matrix.print_matrix()

# Matrix Addition Result:
# 15 17 9
# 15 11 9
# 6 11 10

if matrix1 == matrix2:
    print('\nMatrix 1 and Matrix 2 are equal.')
else:
    print('\nMatrix 1 and Matrix 2 are not equal.')

# Matrix 1 and Matrix 2 are not equal.

print('\nMatrix Multiplication Result:')
result_matrix = matrix1 * matrix2
result_matrix.print_matrix()

# Matrix Multiplication Result:
# 137 135 88
# 78 104 99
# 105 109 77
