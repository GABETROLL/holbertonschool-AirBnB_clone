#!/usr/bin/python3
"""Before the class and importing json"""

import json

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
        self.__objects[key_obj] = obj.to_dict()

    def save(self):
        """serializes the objects to JSON files"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dir = json.loads(f.read())
                self.__objects.update(obj_dir)
        except FileNotFoundError:
            pass
