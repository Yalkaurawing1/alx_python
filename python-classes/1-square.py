#!/usr/bin/python3
# 1-square.py

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is positive
        if size < 0:
            raise ValueError("size must be >= 0")
        # Assign size to a private instance attribute
        self.__size = size