#!/usr/bin/python3
"""Unittest for user Model"""
import unittest
from models.user import User
from datetime import datetime
from time import sleep


class UserCase(unittest.TestCase):
    """Unittests for testing User Class"""
    u = User()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.u, User)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime)
        self.assertIsInstance(self.u.updated_at, datetime)

    def test_two_users_unique_ids(self):
        """test if two users id are unique"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_save(self):
        """test save"""
        u = User()
        sleep(0.05)
        f_updated_at = u.updated_at
        u.save()
        self.assertLess(f_updated_at, u.updated_at)


if __name__ == "__main__":
    unittest.main()
