#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    This function finds the biggest integer in a list.

    Args:
        my_list: The list of integers

    Returns:
        The biggest integer in the list
    """
    if not my_list:
        return None
    largest = my_list[0]
    for i in my_list:
        if i > largest:
            largest = i
    return largest
