#!usr/bin/python3
"""Class File Storage"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances.
    ATTRIBUTES:
    __file_path is a private class attribute (str) path to the JSON file
    __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)
    PUBLIC INSTANCE METHODS
    all():
    new(obj):
    save():
    reload():"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with
        key <obj class name>.id """
        key_obj = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            lp = {i: j.to_dict() for i, j in FileStorage.__objects.items()}
            json.dump(lp, file)

    def reload(self):
        """ deserializes the JSON file to __object"""
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(classes[value['__class__']](**value))
