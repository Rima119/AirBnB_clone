#!/usr/bin/python3
"""Test cases for FileStorage class"""
import unittest
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from time import sleep


class FileStorageTests(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.file_sto = FileStorage()

    def tearDown(self):
        """Tears down test methods"""
        pass

    def test_instantiation(self):
        """Test instantiation of storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"), True)

    def test_all(self):
        """Test the all method"""
        st = FileStorage()
        objs = st.all()
        self.assertIsNotNone(objs)
        self.assertIsInstance(objs, dict)
        self.assertFalse(objs == {})

    def test_field_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(self.file_sto, "__init__"))
        self.assertTrue(hasattr(self.file_sto, "all"))
        self.assertTrue(hasattr(self.file_sto, "new"))
        self.assertTrue(hasattr(self.file_sto, "save"))
        self.assertTrue(hasattr(self.file_sto, "reload"))

    def test_save(self):
        """test if JSON exists"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Halo"
        sleep(0.05)
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Alx")
        self.assertIsInstance(storage.all(), dict)
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertLess(self.my_model.created_at, self.my_model.updated_at)

    def test_reload(self):
        """Test the reload method"""
        test_1 = BaseModel()
        test_1.save()
        test_1.name = "Alx"
        test_1.number = 1
        test_1.save()
        self.assertTrue(os.path.exists("file.json"))
        dic = {}
        with open('file.json', 'r') as fjson:
            dic = json.loads(fjson.read())
        test_1_key = test_1.__class__.__name__ + '.' + test_1.id
        self.assertDictEqual(test_1.to_dict(), dic[test_1_key])

    def test_new(self):
        """ Test the new method"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "12345"
        user.name = "Kolo"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])


if __name__ == '__main__':
    unittest.main()
