#!/usr/bin/python3
"""A square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: a side of square
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
