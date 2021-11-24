#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    length = len(new_matrix)
    for x in range(length):
        new_matrix[x] = list(map(lambda y: y**2, new_matrix[x]))
    return new_matrix
