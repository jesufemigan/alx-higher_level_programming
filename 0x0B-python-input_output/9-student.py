#!/usr/bin/python3
'''a module for task 9'''


class Student:
    '''a class of student'''
    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns dictionary representation of student instance'''
        return self.__dict__
