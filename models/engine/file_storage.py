#!/usr/bin/python3
"""Before the class and importing json"""

import json
# from models.base_model import BaseModel



class FileStorage:
    """Initializing the Filestorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returning the dictionary of model
        object dictionaries
        """
        return self.__objects

    def new(self, obj):
        """
        Adds in the object dictionary 'obj'
        with its class name and id into
        'FileStorage.__objects'.
        """
        if not isinstance(obj, dict):
            raise TypeError("new 'obj' must be a model in its dictionary representation.")

        key_obj = "{}.{}".format(obj["__class__"], obj["id"])
        self.__objects[key_obj] = obj

    def save(self):
        """
        Serializes the objects to JSON file
        'FileStorage.__file_path'.
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to
        'FileStorage.__objects'.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                obj_dir = json.loads(file.read())
                self.__objects.update(obj_dir)
        except FileNotFoundError:
            pass
