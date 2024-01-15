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

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="uft-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def from_json_string(json_string):
        '''from json string'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create new class'''
        if cls is Rectangle:
            my_class = Rectangle(2, 3)
        elif cls is Square:
            my_class = Square(8)
        else:
            my_class = None
        my_class.update(**dictionary)
        return my_class
