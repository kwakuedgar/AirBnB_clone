#!/usr/bin/python3
"""
tests for State class
"""

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestStateAttributes(unittest.TestCase):
    """
    Test attributes of the State
    """
    def test_name_type(self):
        """
        Test name
        """
        state = State()
        self.assertEqual(type(state.name), str)


class TestStateMethods(unittest.TestCase):
    """
    Test methods of State
    """

    def test_str(self):
        """
        Test __str__ method of State
        """
        state = State()
        expected_output = "[State] ({}) {}".format(
            state.id, state.__dict__)
        self.assertEqual(str(state), expected_output)


class TestStateStorage(unittest.TestCase):
    """
    Test storage State
    """

    def test_new_instance_stored(self):
        """
        Test new instance of State
        """
        state = State()
        storage.new(state)
        self.assertIn(state, storage.all().values())


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test default attributes of State class"""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))


if __name__ == '__main__':
    unittest.main()
