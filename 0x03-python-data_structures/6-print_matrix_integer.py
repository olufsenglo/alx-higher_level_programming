#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for outer in matrix:
        for j in range(len(outer)):
            print('{:d}'.format(outer[j]), end=" " if j != len(outer) - 1 else "")
        print()
