#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for row_list in matrix:
        temp_list = list(map(lambda x: x**2, row_list))
        new_list.append(temp_list)
    return new_list
