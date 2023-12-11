#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
import os


class TestFileStorage(unittest.TestCase):
    """
    tests for the FileStorage class
    """

    def setUp(self):
        """
        set up instances for all tests
        """
        self.obj_base = BaseModel()
        self.obj_usr = User()
        self.obj_city = City()
        self.obj_place = Place()
        self.obj_state = State()
        self.obj_review = Review()
        self.obj_amenity = Amenity()

    def test_type_file_path(self):
        """ Tests the type of the file path """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_type_obj_dict(self):
        """ Tests the type of __objects"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all_return_type(self):
        """ Tests the all method"""
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """
        Tests if a new instance is correctly added to __objects
        """
        self.assertIn("BaseModel." + self.obj_base.id, storage.all().keys())
        self.assertIn(self.obj_base, storage.all().values())
        self.assertIn("User." + self.obj_usr.id, storage.all().keys())
        self.assertIn(self.obj_usr, storage.all().values())
        self.assertIn("City." + self.obj_city.id, storage.all().keys())
        self.assertIn(self.obj_city, storage.all().values())
        self.assertIn("Place." + self.obj_place.id, storage.all().keys())
        self.assertIn(self.obj_place, storage.all().values())
        self.assertIn("State." + self.obj_state.id, storage.all().keys())
        self.assertIn(self.obj_state, storage.all().values())
        self.assertIn("Review." + self.obj_review.id, storage.all().keys())
        self.assertIn(self.obj_review, storage.all().values())
        self.assertIn("Amenity." + self.obj_amenity.id, storage.all().keys())
        self.assertIn(self.obj_amenity, storage.all().values())

    def test_save(self):
        """
        Test and saves instance to the storage
        """
        storage.save()
        json_read = ""
        with open("file.json", "r") as f:
            json_read = f.read()
            self.assertIn("BaseModel." + self.obj_base.id, json_read)
            self.assertIn("User." + self.obj_usr.id, json_read)
            self.assertIn("City." + self.obj_city.id, json_read)
            self.assertIn("Place." + self.obj_place.id, json_read)
            self.assertIn("State." + self.obj_state.id, json_read)
            self.assertIn("Review." + self.obj_review.id, json_read)
            self.assertIn("Amenity." + self.obj_amenity.id, json_read)
        os.remove('file.json')

    def test_reload(self):
        """
        Test reloading instance from the storage
        """
        storage.save()
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel." + self.obj_base.id, all_objs)
        self.assertIn("User." + self.obj_usr.id, all_objs)
        self.assertIn("City." + self.obj_city.id, all_objs)
        self.assertIn("Place." + self.obj_place.id, all_objs)
        self.assertIn("State." + self.obj_state.id, all_objs)
        self.assertIn("Review." + self.obj_review.id, all_objs)
        self.assertIn("Amenity." + self.obj_amenity.id, all_objs)

    def test_no_file(self):
        """
        Testing what happens when there's no file called (file.json)
        """
        if os.path.exists('file.json'):
            os.remove('file.json')
        try:
            storage.reload()
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
