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


def rotate_idx(row: int = 0, col: int = 0, __factor: int = 1, __limit: int = 2,
               size: int = 2) -> tuple:
    """Get next index of 2D matrix in clockwise direction"""
    col += __factor
    if col == __limit + __factor:
        col, row = __limit, row + __factor
    if row == __limit + __factor:
        __factor *= -1
        col, row = col + __factor, __limit
        __limit = 0 if __factor < 0 else size
    return row, col, __factor, __limit


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2D matrix 90 degrees clockwise"""
    # Input Validation: Check that matrix is a matrix (a list of lists)
    if not matrix or not isinstance(matrix, list):
        return
    for row in matrix:
        if not row or not isinstance(row, list):
            return

    # Define parameter defaults for rotate_idx function
    row, col, operand, limit = 0, 0, 1, len(matrix) - 1

    # Rotate matrix values 90 degrees in clockwise direction
    for _ in range(len(matrix) - 1):
        # Shift matrix values backward one cell in counter-clockwise direction
        for _ in range(len(matrix) * len(matrix) - 2):
            # Set current index before shifting
            idx = col, row
            # Get row and column indexes of next cell
            row, col, operand, limit = rotate_idx(row, col, operand, limit)
            # Replace value in cell with previous value and backup current
            matrix[col][row], matrix[idx[0]][idx[1]] = \
                matrix[idx[0]][idx[1]], matrix[col][row]


if __name__ == '__main__':
    """Tests the code in this module"""
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [['one  ', 'two  ', 'three'],
              ['four ', 'five ', 'six  '],
              ['seven', 'eight', 'nine ']]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[{1}, {2}, {3}],
              [{4}, {5}, {6}],
              [{7}, {8}, {9}]]

    print_matrix(matrix)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)
