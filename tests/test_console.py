#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import os
import sys


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        del cls.consol

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_prompt_string(self):
        """test prompt of the command"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """test empty line of the command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_help_quit(self):
        """test help quit"""
        q = ("exit the program")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(q, f.getvalue().strip())

    def test_help_create(self):
        """test help create"""
        c = ("creates a new instance of BaseMode")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_EOF(self):
        """test help EOF"""
        e = ("end of file")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(e, f.getvalue().strip())

    def test_help_show(self):
        """test help show"""
        s = ("prints the string representation of an instance")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(s, f.getvalue().strip())

    def test_help_destroy(self):
        """test help destroy"""
        d = ("deletes an instance based on the class name and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(d, f.getvalue().strip())

    def test_help_all(self):
        """test help all"""
        a = ("prints all string representation of all instances")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(a, f.getvalue().strip())

    def test_help_count(self):
        """test help count"""
        c = ("retrieve the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_update(self):
        """test help update"""
        u = ("updates an instance based on the class name and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(u, f.getvalue().strip())

    def test_help(self):
        """help test"""
        h = ("Documented commands (type help <topi)\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, f.getvalue().strip())

    def test_quit_exits(self):
        """test quit"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_EOF_exits(self):
        """test EOF"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create(self):
        """test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create nananana")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="alx@g.com" password="123"')

    def test_show(self):
        """test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show nananana")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel 123nana")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy Zip")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 123nana")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_all(self):
        """test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all nananana")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update nananana")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User 123nana")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            obj = f.getvalue()
        obj_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + obj_id)
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + obj_id + " Name")
            self.assertEqual("** value missing **\n", f.getvalue())

    def test_class_all(self):
        """test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("nanana.all()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.all()")
            self.assertEqual("[]\n", f.getvalue())

    def test_class_count(self):
        """test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("nanana.count()")
            self.assertEqual("0\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.count()")
            self.assertEqual("53\n", f.getvalue())

    def test_class_show(self):
        """test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("nanana.show()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("BaseModel.show(123-nan)")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_class_destroy(self):
        """test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("Zip.destroy()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.destroy(123-nana)")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_class_update(self):
        """test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("nanana.update()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(123-nana)")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            obj = f.getvalue()
        obj_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + obj_id + ")")
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + obj_id + ", name)")
            self.assertEqual("** value missing **\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
