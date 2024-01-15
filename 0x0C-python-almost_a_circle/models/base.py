#!/usr/bin/python3
'''A module for the base class'''


from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation'''
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

