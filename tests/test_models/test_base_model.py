#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.base_model import datetime


class TestConstructor(unittest.TestCase):
    def no_arguments(self):

        b = BaseModel()
        self.assertEqual(b.created_at, datetime.now())
