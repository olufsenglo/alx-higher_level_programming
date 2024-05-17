#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list at a given index, similar to C.
    Args:
        my_list: list of numbers
        idx: index
    Returns:
        Element at index idx or none if negative
    """
    return None if idx < 0 or idx >= len(my_list) else my_list[idx]

my_list = [1,2,3,10]

print(element_at(my_list, 3))
