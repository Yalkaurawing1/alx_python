#!/usr/bin/python3
"""
This module contains the class BaseGeometry
"""


class BaseGeometry():
    """A class with method area"""
    def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    
    
    
    def area(self):
       
        """raises an exception when called"""
        raise Exception("area() is not implemented")