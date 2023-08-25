"""
Напишите функцию для транспонирования матрицы.
"""


def transpose_matrix(matrix_to_transpose: list[list[int | str]]) -> list[tuple[int | str]]:
    """
    Transposes matrix.
    :param matrix_to_transpose: matrix to transpose.
    :return: transposed matrix.
    """
    return list(zip(*matrix_to_transpose))


matrix1: list[list[int]] = [[7, 11], [3, 4], [99, -2]]

for row in transpose_matrix(matrix_to_transpose=matrix1):
    print(row)
