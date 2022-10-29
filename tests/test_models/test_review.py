#!/usr/bin/python3
"""Unittest for state Model"""
import unittest
from models.review import Review
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Unittests for testing State Class"""
    r = Review()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.r)), "<class 'models.review.Review'>")

    def test_state_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.r, Review)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime)
        self.assertIsInstance(self.r.updated_at, datetime)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)

    def test_two_states_unique_ids(self):
        """test if two states id are unique"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_save(self):
        """test save"""
        r = Review()
        sleep(0.05)
        f_updated_at = r.updated_at
        r.save()
        self.assertLess(f_updated_at, r.updated_at)


if __name__ == "__main__":
    unittest.main()
