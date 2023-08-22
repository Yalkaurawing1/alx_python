#!/usr/bin/python3
"""module with function to test sameness of two objects"""


def is_same_class(obj, a_class):
    """
    function to test sameness
    of two objects
    """
    if type(obj) == a_class:
        return True
    return False