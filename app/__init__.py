from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)

from app import views, models
import os
from config import basedir
