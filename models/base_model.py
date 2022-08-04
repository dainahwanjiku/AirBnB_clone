#!/usr/bin/python3
""" 
BaseModel that defines all common attributes/methods for other classes.
"""

import uuid
from json import JSONEncoder
import models
from datetime import datetime


class BaseModel:
    """ 
    base model
    """

    def __init__(self, *args, **kwargs):
        """initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                        setattr(self, key, value)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return dictionary representaton of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """return the string formated message when instance is called"""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)

class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, o):
        """ default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
