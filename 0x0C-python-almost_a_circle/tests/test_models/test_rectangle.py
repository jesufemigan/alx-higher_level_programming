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
        cls.fourth_rec = Rectangle(10, 2, 0, 0, 12)
        cls.fifth_rec = Rectangle(10, 2, 1, 3, 90)
        
        cls.update_rec_0 = Rectangle(2, 3, 1, 1, 30)
        cls.update_rec_0.update(22, 3, 5, 2, 2)
        
        cls.update_rec_1 = Rectangle(10, 15, 2, 3, 50)
        cls.update_rec_1.update(x=10, y=2, width=20, height=25, id=99)

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
    
    def test_width_exception(self):
        '''check if the exceptions raised are caught'''
        self.assertRaises(TypeError, Rectangle, "2", 3)
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_correct_height(self):
        '''check if the height is correctly initialized'''
        self.assertEqual(self.first_rec.height, 10)
        self.assertEqual(self.fourth_rec.height, 2)
        self.assertEqual(self.fifth_rec.height, 2)
        
    def test_height_exception(self):
        '''check if the exceptions raised are caught'''
        self.assertRaises(TypeError, Rectangle, 10, "1")
        self.assertRaises(ValueError, Rectangle, 10, -2)

    def test_correct_x(self):
        '''check if x is correctly initialized'''
        self.assertEqual(self.first_rec.x, 0)
        self.assertEqual(self.fourth_rec.x, 0)
        self.assertEqual(self.fifth_rec.x, 1)
        
    def test_x_exception(self):
        '''check if exceptions for x are caught'''
        self.assertRaises(ValueError, Rectangle, 10, 2, -1)

    def test_correct_y(self):
        '''check if y is correctly initialized'''
        self.assertEqual(self.first_rec.y, 0)
        self.assertEqual(self.fourth_rec.y, 0)
        self.assertEqual(self.fifth_rec.y, 3)

    def text_y_exception(self):
        '''check if exceptions for y are caught'''
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -2)
        
    def test_correct_id(self):
        '''check if id is correctly initialized'''
        self.assertEqual(self.first_rec.id, 1)
        self.assertEqual(self.fourth_rec.id, 12)
        self.assertEqual(self.fifth_rec.id, 90)
        
    def test_area(self):
        '''check if area executes correctly'''
        self.assertEqual(self.first_rec.area(), 20)
        self.assertEqual(self.fourth_rec.area(), 20)
        self.assertEqual(self.fifth_rec.area(), 20)
        
    def test_update_0(self):
        '''check if the update method executes correctly'''
        self.assertEqual(self.update_rec_0.id, 22)
        self.assertEqual(self.update_rec_0.width, 3)
        self.assertEqual(self.update_rec_0.height, 5)
        self.assertEqual(self.update_rec_0.x, 2)
        self.assertEqual(self.update_rec_0.y, 2)
        
    def test_update_1(self):
        '''check if update method with explcit 
        argument definition executes correctly'''
        self.assertEqual(self.update_rec_1.x, 10)
        self.assertEqual(self.update_rec_1.y, 2)
        self.assertEqual(self.update_rec_1.width, 20)
        self.assertEqual(self.update_rec_1.height, 25)
        self.assertEqual(self.update_rec_1.id, 99)
