#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest

# project resource
from config import app, db
from models.user import User

db_file = 'users.db'


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test

    def tearDown(self):
        pass

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
