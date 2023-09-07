#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

class OverrideMetaClass(type):
    """def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)"""

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in
                super().__dir__() if attribute != '__init_subclass__']
    

class BaseGeometry(metaclass=OverrideMetaClass):
    """
    This class models an empty class
    """
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
        """a method to raise an exception with a message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        A method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry, metaclass=OverrideMetaClass):
    """
    Models a rectangle. A derived class of BaseGeometgry
    """
    def __dir__(cls) -> None:
        """
        Removes __init_subclass__ from list of class attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    def __init__(self, width, height):
        """
        Call attriutes of parent.
        validates attributes for positive integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
            """
            Returns the string representation"""
            return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
            """
            This method computes the area of the triangle
            """
            return self.__width * self.__height
