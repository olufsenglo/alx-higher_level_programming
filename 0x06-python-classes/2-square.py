#!/usr/bin/python3
"""
The `Square` class represents a square and is initialized with a size.
"""


class Square:
    """
    Represents a square defined by its size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size: int = 0):
        """
        Initializes the square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
