#!/usr/bin/python3
'''A test file for the base.py file'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''A test for the base class'''
    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def test_A_nb_objects_private(self):
        '''tests if nb_objects is private class attributes'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialised(self):
        '''tests if nb_objects initializes to zero'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiaition(self):
        '''Tests Base() instantiation'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''tests constructor signature'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''test constructor signature with 2 notself args'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''tests consective ids'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''tests sync between class and instance id'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''tests custom int id'''
        b = Base(98)
        self.assertEqual(b.id, 98)
