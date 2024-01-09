#!/usr/bin/python3
"""A square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''a subclass of square'''
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Calculates the area of the square'''
        return self.__size ** 2
