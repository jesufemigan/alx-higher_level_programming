#!/usr/bin/python3
"""A module that defines a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implements the area of the rectangle"""
        return self.__width * self.__height

    def __print__(self):
        """prints the description of rectangle"""
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        """returns the description of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
