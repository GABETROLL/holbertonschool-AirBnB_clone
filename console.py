#!/usr/bin/python3
"""Before the module and the class"""


import cmd

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """the hbnb class"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """the end of file"""
        return True

    def help_EOF(self):
        """command of help end of file"""
        return True

    def do_quit(self, arg):
        """exiting the program"""
        exit()

    def help_quit(self):
        """help quitting"""
        print("Quit command to exit the program")
        return True

    def emptyline(self):
        """the empty line"""
        pass

    def do_create(self, line):
        """creating a new instance of BaseModel\
        , saving to JSON file and printing out\
        the id"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line not in classes:
                print("** class doesn't exist **")
            else:
                str = line + "()"
                base_inst = eval(str)
                base_inst.save()
                print(base_inst.id)

    def do_show(self, line):
        """printing the representation\
        of a string based on the class name\
        and id"""
        list_of_str = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif list_of_str[0] not in classes:
            print("** class doesn't exist **")
        elif len(list_of_str) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = list_of_str[0] + "." + list_of_str[1]
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """deleting the instance based on the class\
            name and id"""
        list_of_str = line.split()
        if len(line) == 0:
            print("** class name missing **")
        if list_of_str[0] not in classes:
            print("** class doesn't exist **")
        elif len(list_of_str) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = list_of_str[0] + "." + list_of_str[1]
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """printing the string representation of all\
        instances based or not on the same class"""
        list_of_str = line.split()
        obj = storage.all()
        for key in obj.keys():
            if len(list_of_str) >= 1:
                if list_of_str[0] not in classes:
                    print("** class doesn't exist **")
                    break
                if obj[key].__class__.__name__ == list_of_str[0]:
                    print(obj[key])
            else:
                print(obj[key])

    def do_update(self, line):
        """updating the instance based on the\
        class and id, by adding or updating\
        attribute"""
        list_of_str = line.split()
        if len(list_of_str) == 0:
            print("** class name missing **")
        elif list_of_str[0] not in classes:
            print("** class doesn't exist **")
        elif len(list_of_str) == 1:
            print("** instance id missing **")
        else:

            obj_key = list_of_str[0] + "." + list_of_str[1]
            all_obj = storage.all()
            the_instance = 0
            for key, value in all_obj.items():
                if key == obj_key:
                    the_instance = value
            if not the_instance:
                print("** no instance found **")
            elif len(list_of_str) == 2:
                print("** attribute name missing **")
            elif len(list_of_str) == 3:
                print("** value missing **")
            else:
                setattr(the_instance, list_of_str[2], list_of_str[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
