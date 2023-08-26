#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """ Define a public instance method area """
    def area(self):
        """ Raise an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

""" Create an instance of BaseGeometry """
bg = BaseGeometry()

""" Try to call the area method """
try:
    bg.area()
except Exception as e:
    """ Print the exception message """
    print("[{}] {}".format(e.self.area, e))
