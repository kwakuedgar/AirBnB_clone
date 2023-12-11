#!/usr/bin/python3

"""
FileStorage module
"""

import json
from os.path import exists


class FileStorage:
    """
    FileStorage class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects with key class name
        <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to JSON file
        """
        obj_dic = {}
        for key, value in FileStorage.__objects.items():
            obj_dic[key] = value.to_dict()
        json_objs = json.dumps(obj_dic, default=str)
        with open(FileStorage.__file_path, 'w') as f:
            return f.write(json_objs)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if not exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            json_objs = f.read()
            obj_dic = json.loads(json_objs)
            from models.amenity import Amenity
            from models.base_model import BaseModel
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User
            for key, value in obj_dic.items():
                class_name = value['__class__']
                if class_name in locals():
                    model_class = locals()[class_name]
                    FileStorage.__objects[key] = model_class(**value)
