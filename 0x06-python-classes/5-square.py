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

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        """
        type:
            checks type of attribute
        raise:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """

        self.__size = size

        def area(self):
            """area:
                calculates area of square
                """
            return self.__size ** 2

        def my_print(self):

            """my_print:
                Prints the value of self
                """

            for i in range(self.__size):
                print("#" * self.__size)

            if self.__size == 0:
                print()
