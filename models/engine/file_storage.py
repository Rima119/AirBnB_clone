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


class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            obj_key = f"{type(obj).__name__}.{obj.id}"
            FileStorage.__objects[obj_key] = obj

    def save(self):
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            lp = {i: j.to_dict() for i, j in FileStorage.__objects.items()}
            json.dump(lp, file)

    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            pass
        else:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
