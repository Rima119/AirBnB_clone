#!/usr/bin/python3
"""Console Module"""
from numpy import mat
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
            }

    def default(self, arg):
        """"""
        args_dic = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = arg.split(".")
        match[1] = ".".join(match[1:])
        if len(match) > 1:
            command = match[1].split("(")
            if command[0] in args_dic.keys():
                if command[0] == "update":
                    cg = str(command[1].strip(" ").split(")")[0]).split(",")
                    j = 0
                    if "{" not in command[1]:
                        for i in cg:
                            if "\"" in i and j != len(i):
                                cg[j] = i.split("\"")[1]
                            j += 1
                        call = "{} {}".format(match[0], " ".join(cg))
                        return args_dic[command[0]](call)
                    else:
                        while j < len(cg):
                            cg[j] = cg[j].replace("\"", "").replace(" ", "").\
                                    replace("'", "").replace("{", "").\
                                    replace("}", "")
                            j += 1
                        for i in cg[1:]:
                            call = "{} {}".format(match[0], cg[0] + " " +
                                                  " ".join(i.split(":")))
                            args_dic[command[0]](call)
                        return 0
                com_arg = command[1].split(")")[0]
                if com_arg != "":
                    com_arg = com_arg.split("\"")[1]
                call = "{} {}".format(match[0], com_arg)
                return args_dic[command[0]](call)
        print("Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """end of file"""
        print("")
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """creates a new instance of BaseMode"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, args):
        """prints the string representation of an instance
        based on the class name and id"""
        args = args.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        args = args.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """prints all string representation of all instances based or not
        on the class name"""
        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance_list = []
            for v in storage.all().values():
                if len(args) > 0 and args[0] == v.__class__.__name__:
                    instance_list.append(v.__str__())
                elif len(args) == 0:
                    instance_list.append(v.__str__())
            print(instance_list)

    def do_update(self, args):
        """updates an instance based on the class name and id by adding
        or updating attribute"""
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if "{" in args[2]:
                            print(args[2])
                        if len(args) > 3:
                            lp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                            j = 1
                            for i in args[3]:
                                if i not in lp:
                                    j = 0
                                    break
                            if j:
                                args[3] = int(args[3])
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_count(self, args):
        """retrieve the number of instances of a class"""
        a = 0
        args = args.split()
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                a = a + 1
        print(a)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
