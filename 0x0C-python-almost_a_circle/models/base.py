#!/usr/bin/python3
'''A module for the base class'''


class Base:
    '''A class Base which is the base for all other classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
