#!/usr/bin/python3
'''
    Implementation of the Comment class
'''

from models.base_model import BaseModel
import os

class Comment(BaseModel):
    '''
        Definition of the User class
    '''
    user_id = ''
    transcript_id = ''
    word_number = ''

    @property
    def user(self):
        user_dict = models.storage.all("User")
        for user in user_dict.values():
            if self.user_id == user.id:
                return user

    @property
    def transcript(self):
        transcript_dict = models.storage.all("User")
        for transcript in transcript_dict.values():
            if self.transcript_id == transcript.id:
                return transcript