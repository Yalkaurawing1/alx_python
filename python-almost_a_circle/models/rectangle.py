#!/usr/bin/python3
"""CLass Rectangle"""
# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    """A class that represents a rectangle shape."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A class constructor for Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The horizontal position of the rectangle. Defaults to 0.
            y (int, optional): The vertical position of the rectangle. Defaults to 0.
            id (int, optional): The id of the object. Defaults to None.
        """

        # Call the super class with id
        super().__init__(id)

        # Assign each argument to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width attribute.

        Args:
            value (int): The new value for the width attribute.
        """

        self.__width = value

    @property
    def height(self):
        """A getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height attribute.

        Args:
            value (int): The new value for the height attribute.
        """

        self.__height = value

    @property
    def x(self):
        """A getter for the x attribute.

        Returns:
            int: The horizontal position of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """A setter for the x attribute.

        Args:
            value (int): The new value for the x attribute.
        """

        self.__x = value

    @property
    def y(self):
        """A getter for the y attribute.

        Returns:
            int: The vertical position of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """A setter for the y attribute.

        Args:
            value (int): The new value for the y attribute.
        """

        self.__y = value
