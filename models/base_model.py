#!/usr/bin/python3
"""
BaseModel class with info on when it was created and
updated
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    base funcionality of all models, with info
    on when the model was created and updated
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{type(self)}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        changes the 'updated_at' attribute to now.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns serializable dict of 'self'.
        Adds a '__class__' key to the dict with the
        name of the class, and the dates in the dict's
        values are made in string format.
        """
        return {"__class__": "BaseModel",
                "id": self.id,
                "created_at": self.created_at.
                isoformat("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": self.updated_at.
                isoformat("%Y-%m-%dT%H:%M:%S.%f")
                }
