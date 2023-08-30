#!/usr/bin/python3
"""
This module contains the class BaseGeometry
"""
class BaseGeometry:
    """A class with method area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
""" Create an instance of BaseGeometry """
bg = BaseGeometry()

""" Try to call the area method """
try:
    print(bg.area())        
except Exception as e:
    """ Print the exception message """
    print("[{}] {}".format(e.self.area, e))
