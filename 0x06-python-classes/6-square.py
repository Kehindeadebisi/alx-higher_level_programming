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

        @property
        def position(self):
            """position:
            shows position of attribute
            """
            return self.__position

        @position.setter
        def position(self, value):
            """position:
            shows position of attribute

            """
            if type(value) is not tuple or len(value) != 2 or\
               type(value[0]) is not int or type(value[1]) is not int or\
               value[0] < 0 or value[1] < 0:
                self.__position = value

        def area(self):
            """area:
            calculates area of square
            """
            return self.__size ** 2

        def my_print(self):
            """my_print:
               prints value of self

            """
            if self.__size == 0:
                print()
                return

            print("\n" * self.__position[1], end='')

            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
