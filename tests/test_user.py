#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest


# project resource
from models.user import User


class TestUser(unittest.TestCase):
    """This class contains several methods to test the
    user.py file.
    """
    def setUp(self):
        pass

    def test(self):        
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
