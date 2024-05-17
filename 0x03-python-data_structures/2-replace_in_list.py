#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: The list to access.
        idx: The index of the element to retrieve.
        element: value to replace with.

    Returns:
        The new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
