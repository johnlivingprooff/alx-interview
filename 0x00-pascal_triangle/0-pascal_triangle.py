#!/usr/bin/python3
"""returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        row = pascal[-1]
        new = [1]
        for i in range(len(row) - 1):
            new.append(row[i] + row[i + 1])
        new.append(1)
        pascal.append(new)
    return pascal
