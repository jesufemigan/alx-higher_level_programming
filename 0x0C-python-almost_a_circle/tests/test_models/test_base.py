#!/usr/bin/python3
'''A test file for the base.py file'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''A test for the base class'''
    @classmethod
    def setUpClass(cls):
        '''Function to initialise the class of Base'''
        cls.a = Base()
        cls.b = Base(90)
        cls.c = Base()

    def test_base_class(self):
        '''Check if base class initialises correctly'''
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 90)
        self.assertEqual(self.c.id, 2)
