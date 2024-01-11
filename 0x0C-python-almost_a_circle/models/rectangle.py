#!/usr/bin/python3
'''A module for the rectangle class'''


from models.base import Base


class Rectangle(Base):
    '''A class rectangle that inherits from the Base Class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''The width of the rectangle'''
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def height(self):
        '''The height of the rectangle'''
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self._height = value

    @property
    def x(self):
        '''position on x axis'''
        return self._x

    @x.setter
    def x(self, value):
        if x < 0:
            raise ValueError('x must be >= 0')
        self._x = value

    @property
    def y(self):
        '''position on y axis'''
        return self._y

    @y.setter
    def y(self, value):
        if y < 0:
            raise ValueError('y must be >= 0')
        self._y = value

    def area(self):
        '''calculates the area of the rectangle'''
        return self.__width * self.__height
