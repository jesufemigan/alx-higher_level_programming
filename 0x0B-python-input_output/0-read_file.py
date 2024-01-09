#!/usr/bin/python3
'''A module that reads file'''


def read_file(filename=""):
    '''reads a file'''
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
