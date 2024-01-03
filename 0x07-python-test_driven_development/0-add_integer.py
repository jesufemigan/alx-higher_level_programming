#!/usr/bin/python3
"""
A module that adds two numbers
numbers must be either float or integer
"""


def add_integer(a, b=98):
    """
        adds two numbers
        the two numbers must be either float or integer
        the two numbers will be converted to int before adding
        Returns: a + b
    """
    if not type(a) in [int, float]:
        raise TypeError('a must be an integer')
    if not type(b) in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
