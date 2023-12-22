#!/usr/bin/python3
"""A square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: a side of the square
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square

        Returns:
            the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
