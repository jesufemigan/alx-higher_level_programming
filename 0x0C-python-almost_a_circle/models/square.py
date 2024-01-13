#!/usr/bin/python3
'''a module for the square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class for sqaure'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''the string to return when we print the square class'''
        return f"[Square] ({str(self.id)}) {str(self.x)}/{str(self.y)} \
- {str(self.width)}"

    @property
    def size(self):
        '''one side of the square'''
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
