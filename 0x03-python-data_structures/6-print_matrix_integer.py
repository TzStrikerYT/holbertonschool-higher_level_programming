#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        a = ' '
        for j in i:
            print("{:d}".format(j), end='')
            if j != i[-1]:
                print(a, end='')
        print()
