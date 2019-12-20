#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[f[i]**2 for i in range(len(f))] for f in matrix]
