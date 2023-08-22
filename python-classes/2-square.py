#!/usr/bin/python3
'''Defining a square with size attribute'''


class Square:
    '''class square with area'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)

    def area(self):
        ''' returning the area of a square'''
        return self.__size ** 2