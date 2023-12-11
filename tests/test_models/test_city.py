#!/usr/bin/python3
"""
tests for City class
"""

import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestCity(unittest.TestCase):
    """Test for City class"""

    def test_attributes(self):
        """Test default attributes of City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))


class TestCityAttributes(unittest.TestCase):
    """
    Test attributes
    """

    def test_name_type(self):
        """
        Test name attribute
        """
        city = City()
        self.assertEqual(type(city.name), str)


class TestCityMethods(unittest.TestCase):
    """
    Test City class
    """

    def test_str(self):
        """
        Test  __str__ of the City
        """
        city = City()
        expected_output = "[City] ({}) {}".format(
            city.id, city.__dict__)
        self.assertEqual(str(city), expected_output)


class TestCityStorage(unittest.TestCase):
    """
    Test storage of the City
    """

    def test_new_instance_stored(self):
        """
        Test new instance of City
        """
        city = City()
        storage.new(city)
        self.assertIn(city, storage.all().values())


if __name__ == '__main__':
    unittest.main()
