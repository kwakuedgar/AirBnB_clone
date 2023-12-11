#!/usr/bin/python3
"""
tests for Review class
"""

import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel
import datetime
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test default attributes of Review"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


class TestReviewMethods(unittest.TestCase):
    """
    Test Review
    """

    def test_str(self):
        """
        Test __str__ method of Review
        """
        review = Review()
        expected_output = "[Review] ({}) {}".format(
            review.id, review.__dict__)
        self.assertEqual(str(review), expected_output)


class TestReviewStorage(unittest.TestCase):
    """
    Test storage of Review
    """

    def test_new_instance_stored(self):
        """
        Test new instance of Review
        """
        review = Review()
        storage.new(review)
        self.assertIn(review, storage.all().values())


if __name__ == '__main__':
    unittest.main()
