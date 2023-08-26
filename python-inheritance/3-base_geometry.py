#!/usr/bin/python3
"""
This contains the class BaseGeometry
"""


class BaseGeometry:
    """I do nothing but pass-by"""
    pass

""" Creating an instance if geometry """
bg = BaseGeometry()

# Print the instance
print(bg)

# Print the list of attributes and methods of the instance
print(dir(bg))

# Print the list of attributes and methods of the class
print(dir(BaseGeometry))