#!/usr/bin/python3
"""
This module is for BaseModel class
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        construction of instances

        Args:
        *args: Unused positional arguments.
        **kwargs: Keyword arguments used for recreating an instance from
        dictionary representation.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints: [<class name>] (<self.id>) <self.__dict__>
        """
        name = self.__class__.__name__
        return f'[{name}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        temp_dic = self.__dict__.copy()
        temp_dic['created_at'] = temp_dic['created_at'].isoformat()
        temp_dic['updated_at'] = temp_dic['updated_at'].isoformat()
        temp_dic['__class__'] = self.__class__.__name__
        return temp_dic
