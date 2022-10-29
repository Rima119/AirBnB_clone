#!/usr/bin/python3
"""Unittest for state Model"""
import unittest
from models.state import State
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Unittests for testing State Class"""
    s = State()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.s)), "<class 'models.state.State'>")

    def test_state_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.s, State)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime)
        self.assertIsInstance(self.s.updated_at, datetime)

    def test_two_states_unique_ids(self):
        """test if two states id are unique"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_save(self):
        """test save"""
        s = State()
        sleep(0.05)
        f_updated_at = s.updated_at
        s.save()
        self.assertLess(f_updated_at, s.updated_at)


if __name__ == "__main__":
    unittest.main()
