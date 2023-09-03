#!/usr/bin/python3
"""This module defines a base model class."""
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

        Raises:
            TypeError: If any of the arguments are not integers.
            ValueError: If width or height are less than or equal to 0, or x or y are less than 0.
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

        # Assign value to the private attribute
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

          Raises:
              TypeError: If value is not an integer.
              ValueError: If value is less than or equal to 0.
         """

          # Check if value is an integer
        if not isinstance(value, int):
           raise TypeError("height must be an integer")

          # Check if value is positive
        if value <= 0:
            raise ValueError("height must be > 0")

          # Assign value to the private attribute
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

          Raises:
              TypeError: If value is not an integer.
              ValueError: If value is less than 0.
          """

          # Check if value is an integer
         if not isinstance(value, int):
            raise TypeError("x must be an integer")

          # Check if value is non-negative
         if value < 0:
              raise ValueError("x must be >= 0")

          # Assign value to the private attribute
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

          Raises:
              TypeError: If value is not an integer.
              ValueError: If value is less than 0.
          """

          # Check if value is an integer
         if not isinstance(value, int):
              raise TypeError("y must be an integer")

          # Check if value is non-negative
         if value < 0:
              raise ValueError("y must be >= 0")

          # Assign value to the private attribute
         self.__y = value

    def area(self):
         """A public method that returns the area of the rectangle.

         Returns:
             int: The area of the rectangle.
         """

         # Calculate and return the area as width times height
         return self.__width * self.__height

    def display(self):
         """A public method that prints the rectangle with the character #.

         Prints in stdout the Rectangle instance with the character # by taking care of x and y.
         """

         # Print y number of newlines before the rectangle
         print("\n" * self.__y, end="")

         # Loop through the height of the rectangle
         for i in range(self.__height):
             # Print x number of spaces before the rectangle
             print(" " * self.__x, end="")
             # Print a row of # characters with the width of the rectangle
             print("#" * self.__width)

    def __str__(self):
        """A magic method that returns a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """

        # Return a formatted string with the attributes of the rectangle
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """A public method that assigns an argument to each attribute.

        Args:
            args (tuple): A variable-length tuple of arguments.

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        
        **kwargs can be thought of as a double pointer to a dictionary: key/value
        As Python doesn't have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        # A list of attributes to update in order
        attributes = ["id", "width", "height", "x", "y"]

        # Loop through the arguments and assign them to the corresponding attributes
        for i, arg in enumerate(args):
            # Check if the index is within the range of attributes
            if i < len(attributes):
                # Set the attribute with the argument value using setattr
                setattr(self, attributes[i], arg)
        else:
            # Loop through the key/value pairs in kwars
            for key, value in kwargs.items():
                # Check if the key is valid atterabute name
                if key in attributes:
                    setattr(self, key, value)
           