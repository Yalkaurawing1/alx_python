#!/usr/bin/python3
"""A Base Geometry Class that raise an exception"""


class BaseGeometry:
    """BaseGeometry class defined"""

    def __init__(BaseGeometry):
        pass

    def area(self):
        """function to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Type Validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))