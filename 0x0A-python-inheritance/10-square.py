#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""A square module"""


class Square(Rectangle):
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculates the area of the square'''
        return size ** 2
