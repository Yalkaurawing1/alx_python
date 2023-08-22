#!/usr/bin/python3
'''Defining a square with size attribute and exceptions'''


class Square:
    '''class square with attributes
    The size attribute must be greater than zero'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)