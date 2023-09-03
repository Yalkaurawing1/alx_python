#!/usr/bin/python3


# models/square.py
"""This module inherite from  rectangle model class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class that represents a square shape."""

    def __init__(self, size, x=0, y=0, id=None):
        """A class constructor for Square.

        Args:
            size (int): The size of the square.
            x (int, optional): The horizontal position of the square. Defaults to 0.
            y (int, optional): The vertical position of the square. Defaults to 0.
            id (int, optional): The id of the object. Defaults to None.

        Raises:
            TypeError: If any of the arguments are not integers.
            ValueError: If size is less than or equal to 0, or x or y are less than 0.
        """

        # Call the super class with id, x, y, width and height
        # The width and height must be assigned to the value of size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A getter for the size attribute.

        Returns:
            int: The size of the square.
        """

        # Return the width or height attribute as the size of the square
        return self.width

    @size.setter
    def size(self, value):
        """A setter for the size attribute.

        Args:
            value (int): The new value for the size attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Check if value is positive
        if value <= 0:
            raise ValueError("width must be > 0")

        # Assign value to the width and height attributes as the size of the square
        self.width = value
        self.height = value

    def __str__(self):
        """A magic method that returns a string representation of the square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """

        # Return a formatted string with the attributes of the square
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
