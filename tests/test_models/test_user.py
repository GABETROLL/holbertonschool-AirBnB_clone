#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_init(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)
   
    def test_email(self):
        """ Checking pass email """
        user1 = User()
        self.assertEqual(str, type(User.email))
        self.assertTrue(hasattr(user1, "email"))

    def test_password(self):
        """ Checking pass password """
        user1 = User()
        self.assertEqual(str, type(User.password))
        self.assertTrue(hasattr(user1, "password"))

    def test_first_name(self):
        """ Checking pass first name """
        user1 = User()
        self.assertEqual(str, type(User.first_name))
        self.assertTrue(hasattr(user1, "first_name"))

    def test_last_name(self):
        """ Checking pass last name """
        user1 = User()
        self.assertEqual(str, type(User.last_name))
        self.assertTrue(hasattr(user1, "last_name"))
