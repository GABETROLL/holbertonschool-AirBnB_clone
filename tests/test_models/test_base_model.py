#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.base_model import datetime
from models.base_model import uuid4


class TestConstructor(unittest.TestCase):
    def test_no_arguments(self):
        b = BaseModel()
        self.assertLess(b.created_at, datetime.now())

    def test_kwargs(self):
        b = BaseModel(__class__=int)
        self.assertEqual(b.__class__, BaseModel)

        b = BaseModel(__class__=BaseModel)
        self.assertEqual(b.__class__, BaseModel)

        b = BaseModel(id=complex(3, 0.14))
        self.assertEqual(b.id, complex(3, 0.14))

        b = BaseModel(id="God bless you")
        self.assertEqual(b.id, "God bless you")

        id_ = str(uuid4())
        b = BaseModel(id=str(id_))
        self.assertEqual(b.id, id_)

        b = BaseModel(created_at=False)
        self.assertEqual(b.created_at, False)

        b = BaseModel(created_at=datetime(1970, 1, 1, 0, 0, 0, 0))
        self.assertEqual(b.created_at, datetime(1970, 1, 1, 0, 0, 0, 0))

        now = datetime.now()
        b = BaseModel(created_at=now)
        self.assertEqual(b.created_at, now)

        b = BaseModel(updated_at=int)
        self.assertEqual(b.updated_at, int)

        b = BaseModel(updated_at=datetime(1987, 7, 27))
        self.assertEqual(b.updated_at, datetime(1987, 7, 27))

        b = BaseModel(random_attribute="God loves you!!")
        self.assertIn("random_attribute", b.to_dict())
        self.assertEqual(b.random_attribute, "God loves you!!")

        now = datetime.now()
        attr_dictionary = {"id": str(uuid4()), "created_at": now,
                           "updated_at": now}
        b = BaseModel(**attr_dictionary)
        self.assertDictEqual(b.__dict__, attr_dictionary)

        now = datetime.now()
        attr_dictionary = {"id": str(uuid4()), "created_at": now,
                           "updated_at": now, "__class__": object}
        b = BaseModel(**attr_dictionary)
        attr_dictionary.pop("__class__")
        self.assertDictEqual(b.__dict__, attr_dictionary)
        self.assertEqual(b.__class__, BaseModel)

        now = datetime.now()
        attr_dictionary = {"random_attribute": "idk"}
        b = BaseModel(**attr_dictionary)
        self.assertIn("random_attribute", b.to_dict())
        self.assertEqual(b.to_dict()["random_attribute"], "idk")


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
