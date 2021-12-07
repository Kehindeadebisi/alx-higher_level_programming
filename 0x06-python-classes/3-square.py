#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """initializes size.

        Attributes:
        size: size of square

        raise: TypeError and ValueError
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        def area(self):

            """Area:
            returns area of square
            """
            return self._size ** 2
