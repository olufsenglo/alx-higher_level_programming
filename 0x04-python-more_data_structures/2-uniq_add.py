#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list = [1, 2, 3, 1, 4, 2, 5]
    my_set = set(my_list)
    return(sum(my_set))
