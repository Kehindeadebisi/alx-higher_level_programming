#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """initializes size.

        Attributes:
        size: size of square

        raise: TypeError and ValueError
        """

        @property
        def size(self):

            return self.__size

        @size.setter
        def size(self, value):
            if type(size) is not int:
                raise TypeError("size must be an integer")

            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size

            def area(self):
                return self.__size ** 2

            def my_print(self):

                """Prints self
                """

                for i in range(self.__size):
                    print("#" * self.__size)

                if self.__size == 0:
                    print()

                if position[1]
