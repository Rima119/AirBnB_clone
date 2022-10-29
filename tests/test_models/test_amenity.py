#!/usr/bin/python3
"""Unittest for state Model"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Unittests for testing State Class"""
    a = Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.a)), "<class 'models.amenity.Amenity'>")

    def test_state_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime)
        self.assertIsInstance(self.a.updated_at, datetime)

    def test_two_states_unique_ids(self):
        """test if two states id are unique"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_save(self):
        """test save"""
        a = Amenity()
        sleep(0.05)
        f_updated_at = a.updated_at
        a.save()
        self.assertLess(f_updated_at, a.updated_at)


if __name__ == "__main__":
    unittest.main()
