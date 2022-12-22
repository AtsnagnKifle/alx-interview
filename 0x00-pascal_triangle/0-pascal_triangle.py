#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = [[1], [1, 1]]
    if n <= 0:
        return []
    if n <= 2:
        return triangle[:n]
    for i in range(2, n):
        line = [1]
        for j in range(i-1):
            line.append(triangle[i-1][j] + triangle[i - 1][j+1])
        triangle.append(line+[1])
    return triangle
