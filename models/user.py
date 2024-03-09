#!/usr/bin/python3
'''User subclass of parent class BaseModel'''

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''subclass of BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
