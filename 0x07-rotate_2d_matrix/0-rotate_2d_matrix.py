#!/usr/bin/python3
"""Rotate 2D matrix challenge"""


def print_matrix(matrix: list) -> None:
    """Pretty-prints a matrix"""
    if not matrix or not isinstance(matrix, list):
        return
    for i, row in enumerate(matrix):
        if not i:
            print(f'[{row}')
        elif i == len(matrix) - 1:
            print(f' {row}]\n')
        else:
            print(f' {row}')


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2D matrix 90 degrees clockwise"""
    # Input Validation: Check that matrix is a matrix (a list of lists)
    if not matrix or not isinstance(matrix, list):
        return
    # Input Validation: Check for square matrix (equal number of rows/columns)
    for row in matrix:
        if not row or not isinstance(row, list) or not len(row) == len(matrix):
            return

    # Create empty matrix with same size as given matrix
    size = len(matrix)
    rotated = [[0 for _ in range(size)] for _ in range(size)]
    # Copy contents of original to new matrix with values rotated 90 degrees
    for row in range(size):
        c = size - 1 - row
        for col in range(size):
            rotated[col][c] = matrix[row][col]

    # Copy values from rotated matrix back to original
    for row in range(size):
        for col in range(size):
            matrix[row][col] = rotated[row][col]


if __name__ == '__main__':
    """Tests the code in this module"""
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2],
              [3, 4]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[{1}, {2}, {3}],
              [{4}, {5}, {6}],
              [{7}, {8}, {9}]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)
