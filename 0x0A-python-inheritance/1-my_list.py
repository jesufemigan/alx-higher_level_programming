#!/usr/bin/python3
"""
Module with a class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list class"""
    def print_sorted(self):
        """A function that prints a sorted list"""
        print(sorted(self))
