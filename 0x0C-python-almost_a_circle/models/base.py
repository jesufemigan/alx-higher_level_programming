#!/usr/bin/python3
'''A module for the base class'''


from json import dumps, loads


class Base:
    '''A class Base which is the base for all other classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="uft-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def from_json_string(json_string):
        '''from json string'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create new class'''
        if cls is Rectangle:
            my_class = Rectangle(2, 3)
        elif cls is Square:
            my_class = Square(8)
        else:
            my_class = None
        my_class.update(**dictionary)
        return my_class

    @classmethod
    def load_from_file(cls):
        '''loads from file'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save to a csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y] for o in
                             list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
            with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
                writter = csv.writter(f)
                writter = writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''load from csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open(f"{cls.__name__}.csv", "r", newline="",
                  encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[3]}
                else:
                    d = {"id": row[0], "size": row[1], "x": row[2],
                         "y": row[3]}
                ret.append(cls.create(**d))
        return ret
