#!/usr/bin/python3
"""Unittest for city Model"""
import unittest
from models.city import City
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """Unittests for testing City Class"""
    c = City()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_city_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.c, City)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime)
        self.assertIsInstance(self.c.updated_at, datetime)

    def test_two_city_unique_ids(self):
        """test if two cities id are unique"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_save(self):
        """test save"""
        c = City()
        sleep(0.05)
        f_updated_at = c.updated_at
        c.save()
        self.assertLess(f_updated_at, c.updated_at)


if __name__ == "__main__":
    unittest.main()
