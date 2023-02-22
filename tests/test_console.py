#!/usr/bin/python3
"""
Unit tests for the console.py functionality
"""
import unittest
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestWrongSyntax(unittest.TestCase):
    """
    Makes sure that bad syntax doesn't affect any
    storage nor instances.
    """
    def test_arong_syntax(self):
        """
        The 'HBNBCommand.create' shouldn't save anything
        to the 'FileStorage' if the class name is missing,
        and just the parenthesis of the class' __init__
        are in the line.

        (and should also print: "*** Unknown syntax: <the line>")
        """
        storage = FileStorage()
        test_instance = HBNBCommand()

        for bad_line in ("()", ";", "^%&^", "** cLasS mISsiNG **", "?",
                         "# this isn't a comment!!!", "<Ctrl + D>"):
            # (that "<Ctrl + D>" up there isn't actually the REAL
            # <Ctrl + D>, it's only its string representation, and
            # therefore an impostor)

            # And that comment isn't a comment

            # (i think)
            previous_storage = storage.all()
            test_instance.do_create(bad_line)
            storage_after = storage.all()

            self.assertDictEqual(previous_storage, storage_after)

class TestDoEOF(unittest.TestCase):
    """
    Tests the 'HBNBCommand.do_EOF' method.
    """
    def test_worng_arguments(self):
        """
        Tests if TypeError is raised when the wrong
        amount of arguments are fed into
        'HBNBCommand.do_EOF'.
        """
        test_instance = HBNBCommand()

        with self.assertRaises(TypeError):
            test_instance.do_EOF()

        with self.assertRaises(TypeError):
            test_instance.do_EOF("two", "arguments")
    
    def test_output(self):
        """
        Tests if 'HBNBCommand.do_EOF' returns True,
        and causes the cmd to stop when inputting
        <Ctrl + D>.
        """
        test_instance = HBNBCommand()

        self.assertEqual(test_instance.do_EOF("any"), True)


class TestEmptyLine(unittest.TestCase):
    """
    Tests 'HBNBCommand.emptyline'.
    """
    def test_output(self):
        """
        Makes sure 'HBNBCommand.do_EOF' returns False.
        """
        test_instance = HBNBCommand()
        self.assertEqual(test_instance.emptyline(), False)


class TestDoCreate(unittest.TestCase):
    """
    Tests 'HBNBCommand.do_create, which is
    supposed to create new BaaseModel instances
    (or the instances of classes that inherit from
    'BaseModel') and makes sure that constructing
    the objects works.
    """
    def test_no_class_name(self):
        """
        "create" followed by nothing line should
        not save any new objects into the FileStorage
        object collection, nor the file.

        (and also should print: "** class name missing **")
        """
        storage = FileStorage()
        test_instance = HBNBCommand()

        previous_storage = storage.all()
        test_instance.do_create("create")
        storage_after = storage.all()

        self.assertDictEqual(previous_storage, storage_after)

    def test_correct_type(self):
        """
        The 'HBNBCommand.create' method should create a new
        instance of 'BaseModel' (or 'BaseModel's children)
        and call its 'save' method, which saves
        itself into the 'FileStorage' class, through
        the 'storage' variable.
        """
        storage = FileStorage()
        test_instance = HBNBCommand()

        previous_storage = storage.all()
        test_instance.do_create("BaseModel()")
        storage_after = storage.all()

        difference = {name: obj for name, obj in storage_after.items() if not (name in previous_storage)}

        self.assertEqual(len(difference), 1)
        new_key = difference.keys()[0]
        self.assertEqual(type(new_key), str)
        self.assertTrue(new_key.startswith("BaseModel"))


class TestDoAll(unittest.TestCase):
    pass