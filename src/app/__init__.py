__author__ = 'dsk'
from flask import Flask

app = Flask(__name__)
client = app.test_client()
from app.modules.user.controllers import *