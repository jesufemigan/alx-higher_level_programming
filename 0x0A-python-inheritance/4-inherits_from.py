#!/usr/bin/python3
"""Module that ckecks subclass"""


def inherits_from(obj, a_class):
    '''function that checks subclass'''
    return isinstance(obj, a_class) and type(obj) != a_class
