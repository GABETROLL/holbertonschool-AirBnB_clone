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

    Uses **kwargs to set the attributes of 'self',
    except '__class__'.
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if not kwargs:
            return

        for attr, value in kwargs.items():
            if attr == "__class__":
                continue

            result = value

            if attr in ("created_at", "updated_at") and \
                    type(value) == str:
                result = datetime.fromisoformat(value)

            self.__setattr__(attr, result)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

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
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__

        if "updated_at" in result:
            result["updated_at"] = self.updated_at.isoformat()
        if "created_at" in result:
            result["created_at"] = self.created_at.isoformat()

        return result
