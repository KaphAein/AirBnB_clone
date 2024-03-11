#!/usr/bin/python3
'''
serializes instances to a JSON file
and deserializes JSON file to instances
'''

import json
from models.base_model import BaseModel
from json.decoder import JSONDecodeError
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    Object relation mapping to interface or database
    '''
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        ser = {}
        for key, val in self.__objects.items():
            ser[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(ser, f)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file'''
        try:
            des = {}
            with open(self.__file_path, 'r', encoding="UTF*") as f:
                des = json.load(f)
            for key, val in des.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects = obj
        except (FileNotFoundError, JSONDecodeError):
            pass
