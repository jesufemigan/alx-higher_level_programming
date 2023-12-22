#!/usr/bin/python3
"""A square module"""


class Square:
    """A square with sizes."""
    def __init__(self, size):
        """Constructor.

        Args:
            size: length of a side of a square.
        """
        self.__size = size
