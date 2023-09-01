

#!/usr/bin/python3
"""This module defines a base model class."""


class Base:
    """
    creating private class ettribute
    """
    __nb_objects = 0
def __init__(self, id=None):
    """
    intiating class mrthod
    """ 
    if id is not None:
      self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects