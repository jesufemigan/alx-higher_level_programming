#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
        A rectangle of width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor
            Args:
                width
                height
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
        Prints the shaped form of the rectangle using #
        """
        if self.__width == 0 and self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """Gets the code to instantiate the class"""
        return f'Rectangle({self.__width}, {self.__height})'

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

    def __del__(self):
        """Delete the rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A static method to check which rectangle is bigger

        Args:
            rect_1: An instance of Rectangle
            rect_2: An instance of Rectangle

        Returns:
            The bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        A class method that returns a new instance of Rectangle
        where size = width = height
        """
        return cls(size, size)
