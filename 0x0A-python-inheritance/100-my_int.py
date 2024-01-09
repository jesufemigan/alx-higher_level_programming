#!/usr/bin/python3
'''A module that uses int'''


class MyInt(int):
    '''a class that uses the int'''
    def __new__(cls, *args, **kwargs):
        '''create a new instance of class'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''what was != is now =='''
        return int(self) != other

    def __ne__(self, other):
        '''what was == is now !='''
        return int(self) == other
