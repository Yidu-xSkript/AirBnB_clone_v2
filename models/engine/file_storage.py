#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, _class=None):
        """Returns a dictionary of models currently in storage"""
        if _class is not None:
            if type(_class) == str:
                _class = eval(_class)
            _class_dict = {}
            for k, v in self.__objects.items():
                if type(v) == _class:
                    _class_dict[k] = v
            return _class_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[obj.__class__.__name__ + '.' + obj.__dict__['id']] = obj

    def save(self):
        """Saves storage dictionary to file"""
        to_JSON = {obj: self.__objects[obj].to_dict()
                   for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as fp:
            json.dump(to_JSON, fp)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, "r") as fp:
                _dict = json.load(fp)
                for o in _dict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
