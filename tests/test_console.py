#!/usr/bin/python3
"""
Unit tests for the console.py functionality
"""
import unittest
from console import HBNBCommand


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
