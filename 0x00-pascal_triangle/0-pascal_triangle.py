#!/usr/bin/python3
""" Pascal's Triangle Generator """


def pascal_triangle(n: int = 0):
    """ Returns a list of lists of ints for the Pascal’s triangle of n """
    if not isinstance(n, int) or n <= 0:
        return []

    result = []
    while n:
        if not len(result):
            result.append([1])
            n -= 1
            continue
        last = result[-1]
        row = []
        for i in range(len(last)):
            if i == 0:
                row.append(last[0])
                continue
            row.append(last[i] + last[i - 1])
        row.append(last[-1])
        result.append(row)
        n -= 1
    return result


if __name__ == '__main__':
    num = __name__
    print(pascal_triangle(num), end='\t|\t')
    num = 'Some text'
    print(pascal_triangle(num), end='\t|\t')
    num = {'key': __name__}
    print(pascal_triangle(num))

    print('- ' * 20)
    num = 2
    [print(line) for line in pascal_triangle(num)]

    print('- ' * 20)
    num = 12
    [print(line) for line in pascal_triangle(num)]
