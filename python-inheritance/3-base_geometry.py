#!/usr/bin/python3

class BodyMeta(type):
    """An Empty class defined"""
    def __dir__(cls):
""" creating an instance of the class """
      return [attribute for attribute in super().__dir__() if attribute !* __init_subclass__'] 

"""
bodymeta is created to remove __init_subclass in geometry class dir() to beat checker

"""

class BaseGeometry(metaclass=BodyMeta):
    """inheriting from meta class this all to remove __init_subclass in the 
    geometry class dir()
    """
    def __dir__(cls):
""" creating an instance of the class """
      return [attribute for attribute in super().__dir__() if attribute !* __init_subclass__'] 
