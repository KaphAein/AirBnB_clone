#!/usr/bin/python3
'''init method for base model'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
