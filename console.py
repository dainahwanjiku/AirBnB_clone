#!/usr/bin/python3
"""Program entry"""

import cmd
from models.__init__ import storage
from models.base_model import BaseModel
import shlex
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
          }


class HBNBCommand(cmd.Cmd):
    """The console class"""
    prompt = '(hbnb) '
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        exit()

    def do_help(self, arg):
        """Display help docs"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing...Override cmds
        emptyline method"""
        pass

    def do_create(self, args):
        """ Create an object"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        nw_instance = HBNBCommand.classes[args]()
        storage.save()
        print(nw_instance.id)
        storage.save()

    def do_show(self, arg):
        """print str rep of an instance"""
        ls = shlex.split(arg)
        if len(ls) == 0:
            print("** class name missing **")
            return False
        if ls[0] in classes:
            if len(ls) > 1:
                k = ls[0] + "." + ls[1]
                if k in storage.all():
                    print(storage.all()[k])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete instances"""
        ls = shlex.split(arg)
        if len(ls) == 0:
            print("** class name missing **")
        elif ls[0] in classes:
            if len(ls) > 1:
                k = ls[0] + "." + ls[1]
                if k in storage.all():
                    storage.all().pop(k)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """prints all"""
        ls = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    ls.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                ls.append(str(v))

        print(ls)

    def do_update(self, args):
        """updates instances"""
        kwargs = ''
        cls_name = kwargs
        cls_id = cls_name
        atr_name = cls_id
        atr_val = atr_name

        # use partition for splitting --> returns tuple
        args = args.partition(" ")
        if args[0]:
            cls_name = args[0]
        else:
            print("** class name missing **")
            return
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            cls_id = args[0]
        else:
            print("** instance id missing **")
            return

        k = cls_name + "." + cls_id

        if k not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] is '\"':
                q = args.find('\"', 1)
                atr_name = args[1:q]
                args = args[q + 1:]

            args = args.partition(' ')

            if not atr_name and args[0] is not ' ':
                atr_name = args[0]
            if args[2] and args[2][0] is '\"':
                atr_val = args[2][1:args[2].find('\"', 1)]

            if not atr_val and args[2]:
                atr_val = args[2].partition(' ')[0]

            args = [atr_name, atr_val]

        nw_dict = storage.all()[k]

        for i, atr_name in enumerate(args):
            if (i % 2 == 0):
                atr_val = args[i + 1]
                if not atr_name:
                    print("** attribute name missing **")
                    return
                if not atr_val:
                    print("** value missing **")
                    return
                if atr_name in HBNBCommand.types:
                    atr_val = HBNBCommand.types[atr_name](atr_val)

                nw_dict.__dict__.update({atr_name: atr_val})

        nw_dict.save()

    def count(self, args):
        """Count instances"""
        cnt = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
