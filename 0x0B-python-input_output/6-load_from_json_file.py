#!/usr/bin/python3
'''module that loads into JSON'''


import json


def load_from_json_file(filename):
    '''function that loads from JSON'''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
