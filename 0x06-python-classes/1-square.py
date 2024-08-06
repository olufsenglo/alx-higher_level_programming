#!/usr/bin/python3
"""
The `Square` class represents a square and is initialized with a size.
"""


class Square:
    """
    Represents a square defined by its size.

    Attributes:
        __size (int): The size of the square
    """
    def __init__(self, size: int):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
