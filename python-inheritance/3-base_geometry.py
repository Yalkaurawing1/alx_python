#!/usr/bin/python3

"""
This module is an empty class 
"""
class BodyMetaClass(type):
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


class BaseGeometry(metaclass=BodyMetaClass):
    """
    This class models an empty class
    """
    def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']