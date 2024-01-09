#!/usr/bin/python3
"""
Module with a class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list class"""
    def __init__(self):
        """Constructor for class MyList"""
        super().__init__()

    def print_sorted(self):
        """A function that prints a sorted list"""
        print(sorted(self))
