#!/usr/bin/python3
"""Unittest for place Model"""
import unittest
from models.place import Place
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Unittests for testing Place Class"""
    p = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_place_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def test_attributes_exist(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))

    def test_attributes_types(self):
        """tests if the type of the attribute is right"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime)
        self.assertIsInstance(self.p.updated_at, datetime)

    def test_two_places_unique_ids(self):
        """test if two places id are unique"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_save(self):
        """test save"""
        p = Place()
        sleep(0.05)
        f_updated_at = p.updated_at
        p.save()
        self.assertLess(f_updated_at, p.updated_at)


if __name__ == '__main__':
    unittest.main()
