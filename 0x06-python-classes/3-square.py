#!/usr/bin/python3
"""
calculate the area of the square.
"""


class Square:
    """
    Represents a square defined by its size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area: Returns the area of the square.
    """

    def __init__(self, size: int = 0):
        """
        Initializes the square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
