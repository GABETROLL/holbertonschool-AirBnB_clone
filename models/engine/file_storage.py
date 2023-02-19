#!/usr/bin/python3
"""Before the class and importing json"""


import json
from models.base_model import BaseModel


class FileStorage:
    """Initializing the Filestorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returning the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in the object to match the name"""
        cls_name = type(obj).__name__
        key_obj = "{}.{}".format(cls_name, obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """serializes the objects to JSON files"""
        firstobj = self.__objects
        objdict = {obj: firstobj[obj].to_dict() for obj in firstobj.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dir = json.loads(f.read())
                for key, value in obj_dir.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
