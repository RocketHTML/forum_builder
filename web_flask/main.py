#!/usr/bin/python3
"""
    This is a script that starts a Flask web application
"""

from flask import Flask, render_template
import models
from models.base_model import BaseModel
from models.user import User
from models.transcript import Transcript
from models.comment import Comment
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def landing_page():
    return("Hello World")

@app.route('/blog')
def blog():
    return("Hello World")

@app.route('/app')
def interface():
    return("Hello World")