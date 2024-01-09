#!/usr/bin/python3
'''a module that returns JSON representation'''


def to_json_string(my_obj):
    '''function to return JSON'''
    return json.dump(my_obj)
