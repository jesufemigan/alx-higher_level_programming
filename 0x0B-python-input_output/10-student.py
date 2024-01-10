#!/usr/bin/python3
'''a module for task 9'''


class Student:
    '''a class of student'''
    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns dictionary representation of student instance'''
        try:
            for attr in atrrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            my_dict[key] = value
        return my_dict
