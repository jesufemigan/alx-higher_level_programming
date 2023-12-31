#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
        A rectangle of width and height
    """
    def __init__(self, width=0, height=0):
        """Constructor
            Args:
                width
                height
        """

        self.width = width
        self.height = height

    def __str__(self):
        """
        Prints the shaped form of the rectangle using #
        """
        shaped_rectangle = ''
        if self.__width != 0 and self.__height != 0:
            shaped_rectangle += '\n'.join('#' * self.__width for j in
                                          range(self.__height))
        return shaped_rectangle

    @property
    def width(self):
        """
            Width of the rectangle

            Raises:
                TypeError if width is not an integer
                ValueError if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
            Height of the rectangle

            Raises:
                TypeError if height is not an integer
                ValueError if height is less than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
