#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    Creates an object of class Square
    """
    pass

    def __init__(self, size):
        """__init__

        initializes size

        Attributes:
            size :size of square

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
