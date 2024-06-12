#!/usr/bin/python3
"""Rotate a 2D matrix 90 degrees in-place"""


def rotate_2d_matrix(matrix):
    """function to rotate a matrix in place"""
    # to get the size of the 2d matrix
    N = len(matrix)

    # to rotate the matrix 90 degrees
    for x in range(N // 2):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N - 1 - y][x]
            matrix[N - 1 - y][x] = matrix[N - 1 - x][N - 1 - y]
            matrix[N - 1 - x][N - 1 - y] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = temp

    # # print the matrix
    # for i in range(N):
    #     for j in range(N):
    #         print(matrix[i][j], end=" ")
    #     print()
