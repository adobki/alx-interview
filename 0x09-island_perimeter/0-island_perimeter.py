#!/usr/bin/python3
"""Island Perimeter algorithm"""


def square_area(grid: list, size: tuple, row: int, col: int) -> int:
    """
    Helper function to count number of exposed borders of a square in a grid.
    :param grid: Rectangular matrix of 0's and 1's. 0 == water, 1 == land.
    :param size: Integer tuple of area/size of grid. size=(height, width).
    :param row: Row of current square in grid.
    :param col: Column of current square in grid.
    :return: area of the square on success, 0 otherwise.
    """
    area = 4
    borders = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    for r, c in borders:
        if 0 <= r < size[0] and 0 <= c < size[1]:
            if grid[r][c] == 1:
                area -= 1
    return area


def island_perimeter(grid: list) -> int:
    """
    Calculates the perimeter of the island represented in grid.
    :param grid: Rectangular matrix of 0's and 1's. 0 == water, 1 == land.
    :return: perimeter of the island on success, 0 otherwise.
    """
    # Data Validation: grid is a list
    if not grid or not isinstance(grid, list) or not isinstance(grid[0], list):
        return 0

    height, width, perimeter = len(grid), len(grid[0]), 0

    # Data Validation 2: grid is rectangular matrix with full/equal columns
    for row in grid:
        if not row or not isinstance(row, list) or len(row) != width:
            return 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                perimeter += square_area(grid, (height, width), row, col)
    return perimeter


if __name__ == '__main__':
    """Tests the code in this module"""
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
