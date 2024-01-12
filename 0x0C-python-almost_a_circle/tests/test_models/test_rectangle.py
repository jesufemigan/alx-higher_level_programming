#!/usr/bin/python3
'''A module that tests for the Rectangle Class'''


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''A class to test the rectangle class'''
    @classmethod
    def setUpClass(cls):
        '''set up a rectangle with empty or incomplete arguments'''
        cls.first_rec = Rectangle(2, 10)
        cls.second_rec = Rectangle(-2, -3)
        cls.third_rec = Rectangle("2", "4")
        cls.fourth_rec = Rectangle(10, 2, 0, 0, 12)
        cls.fifth_rec = Rectangle(10, 2, 1, 3, 90)

    def test_empty_arguments(self):
        '''raises TypeError when Rectangel is initialized
        with no argument'''
        self.assertRaises(TypeError, Rectangle)
    
    def test_incomplete_argument(self):
        '''raises TypeError when Rectangle is initialized with
        1 argument'''
        self.assertRaises(TypeError, Rectangle, 1)

    def test_correct_width(self):
        '''check if the width is correctly initialized'''
        self.assertEqual(self.first_rec.width, 2)
        self.assertEqual(self.fourth_rec.width, 10)
        self.assertEqual(self.fourth_rec.width, 10)

    def test_correct_height(self):
        '''check if the height is correctly initialized'''
        self.assertEqual(self.first_rec.height, 10)
        self.assertEqual(self.fourth_rec.height, 2)
        self.assertEqual(self.fifth_rec.height, 2)

    def test_correct_x(self):
        '''check if x is correctly initialized'''
        self.assertEqual(self.first_rec.x, 0)
        self.assertEqual(self.second_rec.x, 0)
        self.assertEqual(self.third_rec.x, 0)
        self.assertEqual(self.fourth_rec.x, 0)
        self.assertEqual(self.fifth_rec.x, 1)

    def test_correct_y(self):
        '''check if y is correctly initialized'''
        self.assertEqual(self.first_rec.y, 0)
        self.assertEqual(self.second_rec.y, 0)
        self.assertEqual(self.third_rec.y, 0)
        self.assertEqual(self.fourth_rec.y, 0)
        self.assertEqual(self.fifth_rec.y, 3)

    def test_correct_id(self):
        '''check if id is correctly initialized'''
        self.assertEqual(self.first_rec.id, 1)
        self.assertEqual(self.second_rec.id, 2)
        self.assertEqual(self.third_rec.id, 3)
        self.assertEqual(self.fourth_rec.id, 12)
        self.assertEqual(self.fifth_rec.id, 90)
