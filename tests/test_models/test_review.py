#!/usr/bin/python3
"""Tests of the review class"""

import models
import unittest
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """All the tests for the review calss"""

    def test_place_id_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.text))