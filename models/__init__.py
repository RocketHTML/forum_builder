#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel
from models.user import User
from models.transcript import Transcript
from models.comment import Comment
import os

classes = {"User": User, "BaseModel": BaseModel,
           "Transcript": Transcript, "Comment": Comment}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    # from models.engine.db_storage import DBStorage
    # storage = DBStorage()
    pass
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()