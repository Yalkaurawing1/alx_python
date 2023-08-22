#!/usr/bin/python3
"""module for checking inheritance"""


def is_kind_of_class(obj, a_class):
    """
    function to check if obj is instance
    of class or subclass
    Args:
    Obj: object to check
    a_class: the class to which we want to check
    Return:
    True if object is inherited
    Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False