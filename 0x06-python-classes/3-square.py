#!/usr/bin/python3
"""A square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor


        Args:
            size: a side of the square

        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            rasie ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
            Method that calculates the area of the square
        """
        return self.__size ** 2
