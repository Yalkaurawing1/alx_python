#!/usr/bin/python3
"""module for object inheritance from superclass"""


def inherits_from(obj, a_class):
    """
    function to check whether
    object instance inherits from class
    directly or indirectly
    Args:
    obj: the object
    a_class: the class
    Return:
    Either True if it does inherit from class
    Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False