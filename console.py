#!/usr/bin/python3
from models.base_model import *
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """end of file"""
        print("")
        return True

    def do_emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """creates a new instance of BaseMode"""
        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """prints the string representation of an instance
        based on the class name and id"""
        if not (args):
            print("** class name missing **")
            return
        args = args.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if args[1] == value.id:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if args[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """prints all string representation of all instances based or not
        on the class name"""
        if args not in HBNBCommand.classes and len(args) != 0:
            print("** class doesn't exist **")
        else:
            args = arg.split()
            instance_list = []
            for key, value in storage.all().items():
                object_name = value.__class__.__name__
                if object_name == args[0]:
                    instance_list += [value.__str__()]
            print(instance_list)

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding
        or updating attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if args[0] in classes:
            if len(args) == 1:
                print("** instance id missing **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            for object_id in storage.all().kays():
                if object_id == args[1]:
                    setattr(storage.all()[object_id], args[2], args[3])
                    storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
