#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    A class or blueprint that models a square
    """
    def __init__(self, size):
        """
        instantiate attributes to an object
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        Returns:
            str: String representation of the Square instance.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in
                super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        computes area of the square
        """
        return self.__size ** 2