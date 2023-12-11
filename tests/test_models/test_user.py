#!/usr/bin/python3
"""
Test User Class
"""

import datetime
from models.user import User
from models import storage
import unittest
import uuid


class TestUserTypes(unittest.TestCase):
    """
    testing User types
    """

    def test_object_type(self):
        """test object"""
        self.assertEqual(User, type(User()))

    def test_email_type(self):
        """test email"""
        self.assertEqual(type(User().email), str)

    def test_password_type(self):
        """test password"""
        self.assertEqual(type(User().password), str)

    def test_first_name_type(self):
        """test first name"""
        self.assertEqual(type(User().first_name), str)

    def test_last_name_type(self):
        """test last name"""
        self.assertEqual(type(User().last_name), str)

    def test_created_at_type(self):
        """test created_at"""
        self.assertEqual(type(User().created_at), datetime.datetime)

    def test_updated_type(self):
        """test updated_at"""
        self.assertEqual(type(User().updated_at), datetime.datetime)

    def test_id_type(self):
        """test id"""
        self.assertEqual(type(User().id), str)


class Test_methods(unittest.TestCase):
    """
    Test User methods
    """

    def setUp(self):
        """Default setup test"""
        self.user1 = User()

    def test_str(self):
        """test __str__"""
        expected_output = "[User] ({}) {}".format(
            self.user1.id, self.user1.__dict__)
        self.assertEqual(str(self.user1), expected_output)

    def test_save(self):
        """test __save__method"""
        previous_updated_at = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(previous_updated_at, self.user1.updated_at)

    def test_to_dict(self):
        """test to_dict"""
        user1_json = self.user1.to_dict()
        self.assertEqual(user1_json['updated_at'],
                         self.user1.updated_at.isoformat())
        self.assertEqual(user1_json['created_at'],
                         self.user1.created_at.isoformat())
        self.assertEqual(user1_json['__class__'], 'User')

    def test_init_with_kwargs(self):
        """ Test the __init__ with kwargs """
        usr_dict = {
            'id': str(uuid.uuid4()),
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-02T00:00:00.000000',
            'name': 'User Model'
        }
        usr = User(**usr_dict)
        self.assertEqual(usr.id, usr_dict['id'])
        self.assertEqual(usr.created_at,
                         datetime.datetime.strptime
                         (usr_dict['created_at'],
                          '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(usr.updated_at,
                         datetime.datetime.strptime
                         (usr_dict['updated_at'],
                          '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(usr.name, usr_dict['name'])


class Test_attributes(unittest.TestCase):
    """Test attributes"""

    def test_id_creation(self):
        """
        test the created id
        """
        user1 = User()
        self.assertEqual(len(user1.id),
                         len(str(uuid.uuid4())))

    def test_unique_id(self):
        """
        Test if id created is unique
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at(self):
        """
        test the created_at
        """
        temp_obj = User()
        current_time = datetime.datetime.now()
        acceptable_range = datetime.timedelta(minutes=1)
        self.assertLessEqual(current_time - temp_obj.created_at,
                             acceptable_range)

    def test_updated_at(self):
        """
        test the updated_at
        """
        temp_obj = User()
        current_time = datetime.datetime.now()
        acceptable_range = datetime.timedelta(minutes=1)
        self.assertLessEqual(current_time - temp_obj.updated_at,
                             acceptable_range)


class Test_save_in_storage(unittest.TestCase):
    """
    Test that instances are saved in storage
    """

    def test_new_instance_stored(self):
        """
        Test that new instances are in storage
        """
        self.assertIn(User(), storage.all().values())
