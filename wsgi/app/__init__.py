from flask import Flask
#
app = Flask(__name__)

app.secret_key = ''

from app import views
from app import simple
from app import database
