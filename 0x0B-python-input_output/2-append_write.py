#!/usr/bin/python3
'''A module that appens to file'''


def append_write(filename="", text=""):
    '''function that appends'''
    with open(filename, "a", encoding="utf=8") as f:
        return f.write(text)
