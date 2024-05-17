#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for outer in matrix:
        for j in outer:
            print('{:d}'.format(j), end=" ")
        print()
