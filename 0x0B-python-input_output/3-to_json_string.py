#!/usr/bin/python3
'''a module that returns JSON representation'''


import json


def to_json_string(my_obj):
    '''function to return JSON'''
    return json.dumps(my_obj)
