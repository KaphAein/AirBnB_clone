#!/usr/bin/python3

'''BaseModel that defines all common attributes/methods for other classes'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    '''BaseModel Class for all classes'''''

    def __init__(self, *args, **kwargs):
        '''serialization and deserialization of class'''
        if kwargs:
            for key, value in kwargs.items:
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        '''print: [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''updates the updated_at with the current datetime'''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''
        ret_dict = {**self.__dict__}
        ret_dict['__class__'] = type(self).__name__
        ret_dict['created_at'] = self.created_at.isoformat()
        ret_dict['updated_at'] = self.updated_at.isoformat()
        return ret_dict
