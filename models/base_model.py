#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        dateToStr = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # self.__dict__.update(kwargs)
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    v = datetime.strptime(v, dateToStr)
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        _dict = self.__dict__.copy()
        _dict.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["created_at"] = self.created_at.isoformat()
        _dict.pop("_sa_instance_state", None)
        return _dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
