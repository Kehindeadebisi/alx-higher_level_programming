#!/usr/bin/python3
"""
Module: 0-rectangle.py
creation of class Rectangle
"""


class Rectangle:
    """Class Rectanglle:
    an empty class
    """

    def __init__(self, width=0, height=0):
        """initializing
        """
        self.__width

        @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an >= 0")

        self.__height = value
