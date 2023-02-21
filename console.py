#!/usr/bin/python3
"""
Creating the command interpreter console
"""


import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import shlex


classGroup = {"Amenity": Amenity, "BaseModel": BaseModel,
              "City": City, "Place": Place, "Review": Review,
              "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """
    Class Command interpreter
    """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def do_quit(self, line):
        """Quits command that exits the program """
        exit()

    def help_quit(self):
        """help_quit this action is provided by default by cmd"""
        print("Quit command to exit the program\n")
        return True

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")
        return True

    def emptyline(self):
        """Built in method that prints the prompt again"""
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, line):
        """Deletes an instance base on the class and id"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints string representations of instances"""
        className_line = shlex.split(line)
        obj_list = []
        if len(className_line) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif className_line[0] in classGroup:
            for key in models.storage.all():
                if className_line[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates or Adds an attribute to an instance of a class
        instance is identified by class name and id
        only one attribute and value can be updated per call
        """
        if not line:
            print("** class name missing **")
            return False

        args = line.split()

        if args[0] not in classGroup.keys():
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False

        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value

        if not instance_found:
            print("** no instance found **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        setattr(instance_found, args[2], args[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
