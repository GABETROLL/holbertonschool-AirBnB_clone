#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.base_model import datetime


class TestConstructor(unittest.TestCase):
    def test_no_arguments(self):
        b = BaseModel()
        self.assertLess(b.created_at, datetime.now())


class TestToString(unittest.TestCase):
    def test_no_methods(self):
        b = BaseModel()

        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        
class TestSave(unittest.TestCase):
    def test_no_arguments(self):
        b = BaseModel()
        old_time = b.updated_at

        b.save()
        new_time = b.updated_at

        self.assertLess(old_time, new_time)

    def test_arguments(self):
        b = BaseModel()

        with self.assertRaises(TypeError):
            b.save("hi")


class TestToDict(unittest.TestCase):
    def test_items(self):
        b = BaseModel()
        result = b.to_dict()

        self.assertDictEqual(result, {"__class__": "BaseModel",
                                         "id": str(b.id),
                                         "created_at": b.created_at.isoformat(),
                                         "updated_at": b.updated_at.isoformat()
                                         })