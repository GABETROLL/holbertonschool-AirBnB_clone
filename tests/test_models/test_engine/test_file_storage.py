import unittest
from models.base_model import BaseModel
from models.engine import FileStorage
from json import dumps


class TestAll(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        self.assertEqual(test_instance.all(), FileStorage._FileStorage__objects)
    
    def test_objects_type(self):
        test_instance = FileStorage()

        for obj in test_instance.all().values():
            self.assertIsInstance(obj, dict)
        # all model objects in FileStorage.all()'s dictionary should
        # be the dictionary representation of those models.

    def test_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.all("never gonna give you up")


class TestNew(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new()

    def test_correct_args_and_type(self):
        """
        Test that FileStorage().new(obj)
        adds the obj to FileStorage.__objects
        with f"{type(obj).__name__}.{obj.id}"
        as the key, and the obj as the value
        """
        test_instance = FileStorage()
        test_base_model_dict = BaseModel().to_dict()
        test_instance.new(test_base_model_dict)

        file_storage_objs = test_instance.all()
        dict_key = f"BaseModel.{test_base_model_dict['id']}"

        self.assertIn(dict_key, file_storage_objs)
        self.assertEqual(file_storage_objs[dict_key], test_base_model_dict)

    def test_incorrect_type(self):
        test_instance = FileStorage()

        test_base_model = "AAAAAAAAAAAAAA"

        with self.assertRaises(TypeError):
            test_instance.new(test_base_model)

    def test_more_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new("I don't know", complex(float(), int()))


class TestSave(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        test_instance.save()

        with open(FileStorage._FileStorage__file_path, "r") as file:
            expected_output = dumps(test_instance.all())
            self.assertEqual(file.read(), expected_output)

    def test_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.save("hi")
