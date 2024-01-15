#!/usr/bin/python3
'''A module to test the class Square'''

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    '''a class to test square for various scenarios'''
    @classmethod
    def setUpClass(cls):
        cls.first_sqr = Square(2)
        cls.second_sqr = Square(2, 1, 1, 10)
        cls.my_update_sqr_1 = Square(5)
        cls.my_update_sqr_2 = Square(10)
        cls.my_update_sqr_1.update(89, 10, 4, 8)
        cls.my_update_sqr_2.update(size=20, id=99, y=4, x=8)

    def test_square_init(self):
        '''check if square intializes correctly'''
        self.assertEqual(self.first_sqr.width, 2)
        self.assertEqual(self.first_sqr.height, 2)
        self.assertEqual(self.first_sqr.width, self.first_sqr.height)
        self.assertEqual(self.first_sqr.id, 1)
        self.assertEqual(self.first_sqr.x, 0)
        self.assertEqual(self.first_sqr.y, 0)

    def test_square_methods(self):
        '''check if the methods of rectangle works for square'''
        self.assertEqual(self.first_sqr.area(), 4)

    def setUp(self):
        '''set up for getter and setter'''
        self.squ = Square(2)
        self.squ.size = 10

    def test_getter_setter_methods(self):
        '''test the setter and getter methods'''
        self.assertEqual(self.squ.width, 10)
        self.assertEqual(self.squ.height, 10)

    def test_square_update_method(self):
        '''test the update method for square'''
        self.assertEqual(self.my_update_sqr_1.size, 10)
        self.assertEqual(self.my_update_sqr_1.x, 4)
        self.assertEqual(self.my_update_sqr_1.y, 8)
        self.assertEqual(self.my_update_sqr_1.id, 89)

        self.assertEqual(self.my_update_sqr_2.size, 20)
        self.assertEqual(self.my_update_sqr_2.x, 8)
        self.assertEqual(self.my_update_sqr_2.y, 4)
        self.assertEqual(self.my_update_sqr_2.id, 99)
