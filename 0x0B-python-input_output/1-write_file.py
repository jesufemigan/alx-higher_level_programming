#!/usr/bin/python3
'''A module that writes to a file'''


def write_file(filename="", text=""):
    '''returns the length of text written to file'''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
