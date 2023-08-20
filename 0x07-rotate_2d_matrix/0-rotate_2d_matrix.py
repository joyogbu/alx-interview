#!/usr/bin/python3
'''rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''defining the function'''
    for i in range(1, len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
