#!/usr/bin/python3
"""
tests for Amenity class
"""

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""

    def test_attributes(self):
        """Test default attributes of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))


class TestAmenityAttributes(unittest.TestCase):
    """
    Test attributes of Amenity class
    """

    def test_name_type(self):
        """
        Test name
        """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)


class TestAmenityMethods(unittest.TestCase):
    """
    Test methods
    """
    def test_str(self):
        """
        Test __str__
        """
        amenity = Amenity()
        expected_output = "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_output)


class TestAmenityStorage(unittest.TestCase):
    """
    Test storage
    """

    def test_new_instance_stored(self):
        """
        Test new instance
        """
        amenity = Amenity()
        storage.new(amenity)
        self.assertIn(amenity, storage.all().values())


if __name__ == '__main__':
    unittest.main()
