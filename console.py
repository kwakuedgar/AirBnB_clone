#!/usr/bin/python3
"""
Console module
"""

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """
    cmd interface for the project.
    """

    prompt = '(hbnb) '

    def default(self, line):
        """
        <Class_name>.method_name(<args>)
        """
        methods = [self.do_show, self.do_all, self.do_destroy,
                   self.do_update, self.do_count]
        starts = ['show(', 'all(', 'destroy(', 'update(', 'count(']
        cmd_parts = line.split('.')
        if len(cmd_parts) == 2:
            class_name, method_args = cmd_parts
            for i in range(len(starts)):
                if method_args.startswith(starts[i])\
                        and method_args.endswith(')'):
                    rest_of_args = method_args[len(starts[i]):-1]
                    rest_of_args = re.sub(",", " ", rest_of_args)
                    line = class_name + " " + rest_of_args
                    methods[i](line)
                    return
        super().default(line)

    def emptyline(self):
        """Do nothing with an empty line"""
        pass

    def do_EOF(self, line):
        """
        Exiting the program
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit interpreter
        """
        return True

    def do_create(self, class_name=None):
        """
        Creates a new instance of class_name
        """
        if class_name:
            try:
                cls = globals()[class_name]
                obj = cls()
                storage.save()
                print(obj.id)
            except Exception as e:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def handle_args(self, args, expected_args_num):
        """
        Take args and expected args to validate input
        (1st arg is always the class name -if found-)
        (2nd arg is always the id -if found-)
        (3rd arg is always the attribute name -if found-)
        (4th arg is always the attribute value -if found-)
        """
        if len(args) == 0:
            print("** class name missing **")
            return 0
        else:
            class_name = args[0]
            try:
                cls = globals()[class_name]
            except Exception as e:
                print("** class doesn't exist **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 1:
                print("** instance id missing **")
                return 0
        if expected_args_num > 0:
            obj_id = args[1]
            key = f'{class_name}.{obj_id}'
            all_objs = storage.all()
            if key not in all_objs.keys():
                print("** no instance found **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 2:
                print("** attribute name missing **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 3:
                print("** value missing **")
                return 0
        return 1

    def do_show(self, line):
        """
         represents an instance
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 2)
        if flag:
            all_objs = storage.all()
            key = f'{args[0]}.{args[1]}'
            print(str(all_objs[key]))

    def do_destroy(self, line):
        """
         deletes an instance based on the class id
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 2)
        if flag:
            all_objs = storage.all()
            key = f'{args[0]}.{args[1]}'
            del all_objs[key]
            storage.save()

    def do_all(self, line):
        """
         Prints string representation of all instances
        """
        flag = 1
        obj_list = []
        all_obj = storage.all()
        if not line:
            for value in all_obj.values():
                obj_list.append(str(value))
            print(obj_list)
            flag = 0
        else:
            class_name = shlex.split(line)[0]
            try:
                cls = globals()[class_name]
            except Exception as e:
                print("** class doesn't exist **")
                flag = 0
        if flag:
            for key, value in all_obj.items():
                if key.split('.')[0] == class_name:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, line):
        """
         Updates an instance based on class name and id
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 4)
        if flag:
            all_obj = storage.all()
            key = f'{args[0]}.{args[1]}'
            last_arg = args[3]
            if last_arg.startswith('{') and last_arg.endswith('}'):
                attr_dict = eval(last_arg)
                if isinstance(attr_dict, dict):
                    for attr_name, attr_value in attr_dict.items():
                        setattr(all_obj[key], attr_name, attr_value)
                    all_obj[key].save()
            else:
                attr_name = args[2]
                attr_value = last_arg.strip('"')
                setattr(all_obj[key], attr_name, attr_value)
                all_obj[key].save()

    def do_count(self, line):
        """
        print the number of instances for the given class
        """
        count = 0
        if line:
            class_name = shlex.split(line)[0]
            all_obj = storage.all()
            for key in all_obj.keys():
                if key.split('.')[0] == class_name:
                    count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
