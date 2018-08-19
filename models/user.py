#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel
import os

class User(BaseModel):
    '''
        Definition of the User class
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    usage_total = 0
    usage_this_month = 0