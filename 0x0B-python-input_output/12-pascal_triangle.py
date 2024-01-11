#!/usr/bin/python3
'''A python scripts that returns a list of list of pascal triangle'''


def pascal_triangle(n):
    '''returns a list of list of pascal triangle'''

    if n <= 0:
        return []

    pascal_tri = [[1]]
    while len(pascal_tri) != n:
        start_triangle = pascal_tri[-1]
        tmp = [1]
        for i in range(len(start_triangle) - 1):
            tmp.append(start_triangle[i] + start_triangle[i+1])
        tmp.append(1)
        pascal_tri.append(tmp)
    return pascal_tri
