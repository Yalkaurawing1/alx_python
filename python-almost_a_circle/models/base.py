

#!/usr/bin/python3
"""This module defines a base model class."""
# models/base.py

class Base:
    """A base class for geometric shapes."""

    # A private class attribute to count the number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor for Base.

        Args:
            id (int, optional): The id of the object. Defaults to None.
        """

        # If id is not None, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # Otherwise, increment __nb_objects and assign the new value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
