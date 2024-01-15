#!/usr/bin/python3
'''a module for the square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class for square that inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''the string to return when we print the square class'''
        return f"[{type(self).__name__}] ({str(self.id)}) {str(self.x)}/\
{str(self.y)} - {str(self.width)}"

    @property
    def size(self):
        '''one side of the square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update method for the Square class'''
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
