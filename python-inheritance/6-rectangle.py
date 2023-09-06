#!/usr/bin/python3


"""Importing from 5's BaseGeometry"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherit from Base Geometry"""

    def __init__(self, width, height):
        """Initializing Rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height