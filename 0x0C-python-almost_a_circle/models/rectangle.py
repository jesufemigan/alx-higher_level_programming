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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''The height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''position on x axis'''
        return self.__x

    @x.setter
    def x(self, value):
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''position on y axis'''
        return self.__y

    @y.setter
    def y(self, value):
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints the rectangle to stdout with the character #'''
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''writes [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return f"[Rectangle] ({str(self.id)}) {str(self.__x)}/{str(self.__y)} \
- {str(self.__width)}/{str(self.__height)}"

    def update(self, *args, **kwargs):
        '''update the class rectangle'''
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'width':
                    self.__width = kwargs[key]
                elif key == 'height':
                    self.__height = kwargs[key]
                elif key == 'x':
                    self.__x = kwargs[key]
                elif key == 'y':
                    self.__y = kwargs[key]
