#!/usr/bin/python3
"""Console Module"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd


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
                        if len(args) > 3:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
