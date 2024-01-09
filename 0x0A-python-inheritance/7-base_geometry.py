#!/usr/bin/python3
"""A module for base geometry"""


class BaseGeometry:
    """A custom class basegeometry"""
    def area(self):
        """area method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
